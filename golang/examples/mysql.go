package examples

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
	psh "github.com/platformsh/config-reader-go/v2"
	sqldsn "github.com/platformsh/config-reader-go/v2/sqldsn"
)

func UsageExampleMySQL() string {

	// Create a NewRuntimeConfig object to ease reading the Platform.sh environment variables.
	// You can alternatively use os.Getenv() yourself.
	config, err := psh.NewRuntimeConfig()
	checkErr(err)

	// The 'database' relationship is generally the name of the primary SQL database of an application.
	// That's not required, but much of our default automation code assumes it.
	credentials, err := config.Credentials("database")
	checkErr(err)

	// Using the sqldsn formatted credentials package.
	formatted, err := sqldsn.FormattedCredentials(credentials)
	checkErr(err)

	db, err := sql.Open("mysql", formatted)
	checkErr(err)

	defer db.Close()

	// Force MySQL into modern mode.
	db.Exec("SET NAMES=utf8")
	db.Exec("SET sql_mode = 'ANSI,STRICT_TRANS_TABLES,STRICT_ALL_TABLES," +
		"NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO," +
		"NO_AUTO_CREATE_USER,ONLY_FULL_GROUP_BY'")

	// Creating a table.
	sqlCreate := "CREATE TABLE IF NOT EXISTS People (" +
		"id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY," +
		"name VARCHAR(30) NOT NULL," +
		"city VARCHAR(30) NOT NULL)"

	_, err = db.Exec(sqlCreate)
	checkErr(err)

	// Insert data.
	sqlInsert := "INSERT INTO People (name, city) VALUES" +
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

	rows, err := db.Query("SELECT * FROM People")
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

	_, err = db.Exec("DROP TABLE People;")
	checkErr(err)

	return table
}
