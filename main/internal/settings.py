API_STR="/api"

title = "Upsun Examples"

head = """
<head>
    <title>{0}</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&family=Space+Grotesk:wght@300..700&display=swap" rel="stylesheet">

</head>
""".format(title)

styles = """
<style>
    body {
        font-family: "Instrument Sans", sans-serif;
        font-optical-sizing: auto;
        font-weight: 500;
        font-style: normal;
        padding: 5rem;
    }

    h1, h2, h3 {
        font-family: "Space Grotesk", sans-serif;
        font-optical-sizing: auto;
        /* font-weight: <weight>; */
        font-style: normal;
    }
</style> 
"""

rel_lookup = {
    "elasticsearch": "Elasticsearch",
    "chrome-headless": "Headless Chrome",
    "inflxudb": "InfluxDB",
    "kafka": "Kafka",
    "mariadb": "MySQL/MariaDB",
    "memcached": "Memcached",
    "mongodb": "MongoDB",
    "opensearch": "OpenSearch",
    "oracle-mysql": "Oracle MySQL",
    "postgresql": "PostgreSQL",
    "rabbitmq": "RabbitMQ",
    "redis": "Redis",
    "solr": "Solr",
    "vault-kms": "Vault KMS"
}

settings = {
    "API_STR": API_STR,
    "title": title,
    "content": {
        "head": head,
        "styles": styles
    },
    "rel_lookup": rel_lookup
}