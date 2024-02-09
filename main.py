import smtplib




import datetime as dt
import random

with open("quotes.txt") as file:
    lines = file.readlines()
    motiv = random.choice(lines)


now = dt.datetime.now()
today = now.weekday()



if today == 4:
    email = "gocmenkaanmert12@gmail.com"
    password = "tvsiblmtjwsedgnj"


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="gocmenmertkaan@gmail.com",
                            msg=f"Subject:Hey motivation time\n\n{motiv}"
        )











