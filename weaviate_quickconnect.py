import weaviate
from weaviate.classes.init import Auth
import os

# Best practice: store your credentials in environment variables
#wcd_url = os.environ["https://hox91tyxqqkyeyjj8hzhq.c0.us-west3.gcp.weaviate.cloud"]
#https://hox91tyxqqkyeyjj8hzhq.c0.us-west3.gcp.weaviate.cloud
#wcd_api_key = os.environ["YAXy0K34OEhyelQA8vShofC5rVt3UHhCsxT9"]
#wcd_api_key= os.environ["yzgpMpZGzvvuMiOuI71xQivdYgn6gDzpz5ou"]

client = weaviate.connect_to_weaviate_cloud(
    cluster_url='https://hox91tyxqqkyeyjj8hzhq.c0.us-west3.gcp.weaviate.cloud',                                    # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key('yzgpMpZGzvvuMiOuI71xQivdYgn6gDzpz5ou'),             # Replace with your Weaviate Cloud key
)

print(client.is_ready())  # Should print: `True`

client.close()  # Free up resources