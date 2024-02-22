API_STR=""

title = "Upsun Examples"

head = """
<head>
    <title>{0}</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&family=Space+Grotesk:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/custom.css">
    <link rel="stylesheet" href="/static/highlight.css">
</head>
""".format(title)

rel_lookup = {
    "elasticsearch": "Elasticsearch",
    "chrome-headless": "Headless Chrome",
    "influxdb": "InfluxDB",
    "kafka": "Kafka",
    "mysql": "MySQL/MariaDB",
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

rt_lookup = {
    "golang": "Go",
    "java": "Java",
    "nodejs": "Node.js", 
    "php": "PHP",
    "python": "Python"
}

settings = {
    "API_STR": API_STR,
    "title": title,
    "content": {
        "head": head,
    },
    "rel_lookup": rel_lookup,
    "rt_lookup": rt_lookup
}