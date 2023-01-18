import smtplib
import datetime as dt
import random

if dt.datetime.now().weekday() == 0:
    with open("quotes.txt") as quote:
        messages = quote.readlines()
        message = random.choice(messages)

        my_email = "mudassirameen104@gmail.com"
        password = "qcmgxsmpppdfilnt"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="thekkmart1@gmail.com",
                msg=f"Subject:Hello Monday\n\n{message}."
            )


# import datetime

# now = datetime.datetime.now()
# now.day
# now.month
# now.year
# now.minute
# now.hour
# now.second
# now = datetime.datetime(year=2010, month=10, day=12)
# print(now.weekday())