import smtplib

gmail_user = 'valentin.rudloff.perso@gmail.com'
gmail_password = 'pam1249CS1110ragot&'

sent_from = gmail_user
to = ['me@gmail.com', 'bill@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, what'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')