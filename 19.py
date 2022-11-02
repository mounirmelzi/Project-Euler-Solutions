
# Project Euler 19
# Counting Sundays !!

# DAYS = 
#       1: Monday
#       2: Tuesday
#       3: Wednesday
#       4: Thursday
#       5: Friday
#       6: Saturday
#       7: Sunday


def main():
    year = 1900
    month = 1
    date = 1
    day = 1
    sundays = 0

    while year < 2001:
        if day == 7 and date == 1 and year > 1900:
            sundays += 1

        # nember of days in month
        m30 = {4, 6, 9, 11}
        month_days = 30 if month in m30 else 31
        if month == 2:
            month_days = 29 if leap_year(year) else 28

        # update days
        if day == 7:
            day = 1
        else:
            day += 1

        # update year
        if month == 12 and date == 31:
            year += 1

        # update month and date
        if date == month_days:
            if month == 12:
                month = 1
            else:
                month += 1
            date = 1
        else:
            date += 1


    print(sundays)



def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False





if __name__ == '__main__':
    main()
