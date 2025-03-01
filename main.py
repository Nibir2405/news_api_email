import requests
from send_email import send_email



api_key = "fcfc505613eb4fbd879d70c754743880"

topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2025-02-01&sortBy=publishedAt&apiKey=fcfc505613eb4fbd879d70c754743880&language=en"


# Make a request
request = requests.get(url)

# Get data from json file
content = request.json()



# To store article's title and description

email_body = "" + "Subject:Today's news" + "\n"
# Access the article's title and description
for article in content["articles"][:20]:
    if article is not None:

        email_body =  email_body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n" + "-" * 20 + "\n"

send_email(message=email_body)
