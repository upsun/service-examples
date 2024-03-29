package examples

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
	psh "github.com/platformsh/config-reader-go/v2"
	libpq "github.com/platformsh/config-reader-go/v2/libpq"
)

func UsageExamplePostgreSQL() string {

	// Create a NewRuntimeConfig object to ease reading the Platform.sh environment variables.
	// You can alternatively use os.Getenv() yourself.
	config, err := psh.NewRuntimeConfig()
	checkErr(err)

	// The 'database' relationship is generally the name of the primary SQL database of an application.
	// It could be anything, though, as in the case here where it's called "postgresql".
	credentials, err := config.Credentials("postgresql")
	checkErr(err)

	// Retrieve the formatted credentials.
	formatted, err := libpq.FormattedCredentials(credentials)
	checkErr(err)

	// Connect.
	db, err := sql.Open("postgres", formatted)
	checkErr(err)

	defer db.Close()

	// Creating a table.
	sqlCreate := "CREATE TABLE IF NOT EXISTS PeopleGo (" +
		"id SERIAL PRIMARY KEY," +
		"name VARCHAR(30) NOT NULL," +
		"city VARCHAR(30) NOT NULL);"

	_, err = db.Exec(sqlCreate)
	checkErr(err)

	// Insert data.
	sqlInsert := "INSERT INTO PeopleGo(name, city) VALUES" +
		"('Neil Armstrong', 'Moon')," +
		"('Buzz Aldrin', 'Glen Ridge')," +
		"('Sally Ride', 'La Jolla');"

	_, err = db.Exec(sqlInsert)
	checkErr(err)

	table := "<table>" +
		"<thead>" +
		"<tr><th>Name</th><th>City</th></tr>" +
		"</thead>" +
		"<tbody>"

	var id int
	var name string
	var city string

	// Read it back.
	rows, err := db.Query("SELECT * FROM PeopleGo")
	if err != nil {
		panic(err)
	} else {
		for rows.Next() {
			err = rows.Scan(&id, &name, &city)
			checkErr(err)
			table += fmt.Sprintf("<tr><td>%s</td><td>%s</td><tr>\n", name, city)
		}
		table += "</tbody>\n</table>\n"
	}

	_, err = db.Exec("DROP TABLE PeopleGo;")
	checkErr(err)

	return table
}
