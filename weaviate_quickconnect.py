import weaviate
from weaviate.classes.init import Auth
import os

# Best practice: store your credentials in environment variables
#wcd_url = os.environ["https://hox91tyxqqkyeyjj8hzhq.c0.us-west3.gcp.weaviate.cloud"]
#https://hox91tyxqqkyeyjj8hzhq.c0.us-west3.gcp.weaviate.cloud
#wcd_api_key = os.environ["sandbox uri"]
#wcd_api_key= os.environ["creds"]

client = weaviate.connect_to_weaviate_cloud(
    cluster_url='sandbox url',                                    # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key('credentials'),             # Replace with your Weaviate Cloud key
)

print(client.is_ready())  # Should print: `True`

client.close()  # Free up resources
