package examples

import (
	"fmt"

	psh "github.com/platformsh/config-reader-go/v2"
	gosolr "github.com/platformsh/config-reader-go/v2/gosolr"
	solr "github.com/rtt/Go-Solr"
)

func UsageExampleSolr() string {

	// Create a NewRuntimeConfig object to ease reading the Platform.sh environment variables.
	// You can alternatively use os.Getenv() yourself.
	config, err := psh.NewRuntimeConfig()
	checkErr(err)

	// Get the credentials to connect to the Solr service.
	credentials, err := config.Credentials("solr")
	checkErr(err)

	// Retrieve Solr formatted credentials.
	formatted, err := gosolr.FormattedCredentials(credentials)
	checkErr(err)

	// Connect to Solr using the formatted credentials.
	connection := &solr.Connection{URL: formatted}

	// Add a document and commit the operation.
	docAdd := map[string]interface{}{
		"add": []interface{}{
			map[string]interface{}{"id": 123, "name": "Valentina Tereshkova"},
		},
	}

	respAdd, err := connection.Update(docAdd, true)
	checkErr(err)

	// Select the document.
	q := &solr.Query{
		Params: solr.URLParamMap{
			"q": []string{"id:123"},
		},
	}

	resSelect, err := connection.CustomSelect(q, "query")
	checkErr(err)

	// Delete the document and commit the operation.
	docDelete := map[string]interface{}{
		"delete": map[string]interface{}{
			"id": 123,
		},
	}

	resDel, err := connection.Update(docDelete, true)
	checkErr(err)

	message := fmt.Sprintf("Adding one document - %s<br>"+
		"Selecting document (1 expected): %d<br>"+
		"Deleting document - %s<br>",
		respAdd, resSelect.Results.NumFound, resDel)

	return message
}
