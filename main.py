import smtplib
import datetime as dt
import random
import pandas

# ----------------- Global variables --------------------------#
MY_EMAIL = "Youremail@gmail.com"
PASSWORD = "yourpassword"

now = dt.datetime.now()
month = now.month
day = now.day

birthdays_data = pandas.read_csv("birthdays.csv")
birthdays = birthdays_data.to_dict(orient="records")

# ---------------- main logic for birthday email ---------------- #
for birthday in birthdays:
    if birthday["month"] == month and birthday["day"] == day:
        value = random.randint(1, 3)
        with open(f"letter_templates/letter_{value}.txt") as letter_temp:
            letter = letter_temp.read()
            letter = letter.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject: Happy Birthday\n\n{letter}"
            )




