# Day 10

# In this project we will firstly make a leap year finder program and after that we will call the daysInMonth funtion to tell us that in specific month how many day are in.

getyear = int(input("In which year you want day in Month : "))
getmonth = int(input("In which month you want to show days : "))

# Make some veriables that is used to find the leap year
dividedBy4 = getyear % 4
dividedBy100 = getyear % 100
dividedBy400 = getyear % 400

# Make a leap year funtion
def leapYear():
    if dividedBy4 == 0:
        if dividedBy100 != 0:
            if dividedBy400 != 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

leapYear_daysInMonth = [31 , 29 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]
noLeapYear_daysInMonth = [31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]

# Make a funtion to do get number of days in specific month
def daysInMonth(flag, month):
    if month < 1 or month > 12:
        return "Invalid Month"
    if flag == True:
        return f"There will be {leapYear_daysInMonth[month - 1]} in Year {getyear} Month {getmonth}"
    if flag == False:
        return f"There will be {noLeapYear_daysInMonth[month - 1]} in Year {getyear} Month {getmonth}"


flag = leapYear()

print(daysInMonth(flag = flag, month = getmonth))