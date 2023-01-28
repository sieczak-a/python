
import requests
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
import os

# Setting the date to 30 days ago
date_30_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y.%m.%d")

# Creating the index pattern to delete
index_name = "fluentd-" + date_30_days_ago

es_url = "https://elasticsearch:9200"

username = ""
password = os.environ["ELK_USER_PASSWORD"]

# DELETE request 
delete_index = requests.delete(es_url + "/" + index_name, auth=HTTPBasicAuth(username, password), verify=False)

if delete_index.status_code == 200:
    print("Index deleted")
else:
    print("Something went wrong")
