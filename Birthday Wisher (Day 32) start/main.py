import smtplib

email = "ssg137173@gmail.com"
password = "Randomtester@1234"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,
                        to_addrs="suriyagganesh97@gmail.com",
                        msg="Subject:test\n\nanother test mail with subject")
