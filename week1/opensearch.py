from flask import g, current_app
from opensearchpy import OpenSearch

# Create an OpenSearch client instance and put it into Flask shared space for use by the application
def get_opensearch():
    if 'opensearch' not in g:
        host = 'localhost'
        port = 9200
        with open("secrets.txt") as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
            print(f"USERNAME={username}, PASSWORD={password}")
        auth = (username, password)        
        # auth = ('admin', 'admin')
        g.opensearch = OpenSearch(
            hosts=[{'host': host, 'port': port}],
            http_compress=True,  # enables gzip compression for request bodies
            http_auth=auth,
            # client_cert = client_cert_path,
            # client_key = client_key_path,
            use_ssl=True,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )
        # print ("Hello")
        # print(g.opensearch.cat.indices())

    return g.opensearch