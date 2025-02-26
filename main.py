import requests

api_key = "fcfc505613eb4fbd879d70c754743880"

url = "https://newsapi.org/v2/everything?q=tesla&from=2025-01-26&sortBy=publishedAt&apiKey=fcfc505613eb4fbd879d70c754743880"

#Make a request
request = requests.get(url)

#Get data from json file
content = request.json()

#Access the article's title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])