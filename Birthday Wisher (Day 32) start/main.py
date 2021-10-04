import smtplib
import datetime as dt
import random
email = "ssg137173@gmail.com"
password = "Randomtester@1234"
today = dt.datetime.now().today().weekday()

if today == 0:
    with open("quotes.txt", "r") as quotes_data:
        data = quotes_data.readlines()
        quote = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="suriyagganesh97@gmail.com",
                            msg=f"Subject:Quote\n\n{quote}")
