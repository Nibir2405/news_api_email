import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "navidulislam2002@gmail.com"
    password = "gazzbfyhfjhaunwu"

    receiver = "nibirislam56@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email was sent")