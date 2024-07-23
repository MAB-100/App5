import requests
import send_email

api_key = "39b707878e344e8c9e77b5e33cfa2dff"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-23&" \
    "sortBy=publishedAt&apiKey=39b707878e344e8c9e77b5e33cfa2dff"


request = requests.get(url)


content = request.json()

body = ""

for articles in content['articles']:
    if articles['title'] != None:
        body = body + articles['title'] + "\n" + articles['description'] + "\n\n"


body = body.encode("utf-8")
send_email(message=body)