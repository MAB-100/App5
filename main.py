import requests
import send_email

topic = "tesla"
api_key = "39b707878e344e8c9e77b5e33cfa2dff"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-06-23&sortBy=publishedAt&apiKey=39b707878e344e8c9e77b5e33cfa2dff&language=en"


request = requests.get(url)


content = request.json()

body = ""

for articles in content['articles'][:20]:
    if articles['title'] != None:
        body = "Subject: Today's news" + "\n" + body + articles['title'] + "\n" + articles['description'] +"\n" + articles["url"] + "\n\n"



body = body.encode("utf-8")
send_email(message=body)