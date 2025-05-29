# News API Emailer

This Python project fetches the latest news articles about a specific topic using the NewsAPI and sends a summary of the top articles to a specified email address.

## Features

- Retrieves news articles for a given topic from NewsAPI.
- Formats the articles' titles, descriptions, and URLs.
- Sends the news summary via email using Gmail's SMTP server.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. Clone or download this repository.
2. Install required packages:
   ```sh
   pip install requests
   ```
3. Update the email credentials and receiver address in send_email.py as needed.

## Usage

1. Set your desired topic in main.py by modifying the topic variable.
2. Run the script:
   ```sh
   python main.py
   ```
3. The script will fetch the latest news and send an email with the top articles.

## Files

1. main.py: Fetches news and sends the email.
2. send_email.py: Handles sending emails via SMTP.
3. readme.md: Project documentation.

## Notes

1. Make sure to enable "App Passwords" or "Less secure app access" for your Gmail account to allow SMTP access.

2. Keep your email credentials secure and do not share them publicly.
