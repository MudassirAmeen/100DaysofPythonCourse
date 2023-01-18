import pandas, random, datetime, smtplib


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
with open("letter_templates/letter_1.txt") as letter_1:
    letter__1 = letter_1.read()
with open("letter_templates/letter_2.txt") as letter_2:
    letter__2 = letter_2.read()
with open("letter_templates/letter_3.txt") as letter_3:
    letter__3 = letter_3.read()

total_letters = [letter__1, letter__3, letter__2]
birthdays = pandas.read_csv("birthdays.csv")
now = datetime.datetime.now()

for i in range(len(birthdays)):
    birthday_s = birthdays.loc[i]
    # 2. Check if today matches a birthday in the birthdays.csv
    if birthday_s["month"] == now.month and birthday_s["day"] == now.day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        new_letter = random.choice(total_letters)
        new_letter = new_letter.replace("[NAME]", birthday_s["name"])
        # 4. Send the letter generated in step 3 to that person's email address.

        MY_EMAIL = "mudassirameen104@gmail.com"
        MY_PASSWORD = "qcmgxsmpppdfilnt"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_s["email"],
                msg=f"Subject:Happy Birth Day 🎂🍰🍥\n\n{new_letter}"
            )

        






