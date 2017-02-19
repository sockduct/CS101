def IsLeapYear(year):
    if (year % 4) != 0:
        return 0
    else:
        if (year % 100) != 0:
            return 1
        else:
            if (year % 400) != 0:
                return 0
            else:
                return 1

def DaysBeforeDate(year,month,day):
    daysOfMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    daysOfMonths[1] = daysOfMonths[1] + IsLeapYear(year)

    month = month - 1  # Adjust month to match array
    days = 0
    count = 0
    while count < month:
        days = days + daysOfMonths[count]
        count = count + 1
    days = days + day - 1

    return days

def DaysAfterDate(year,month,day):
    # Per requirements, don't exclude birth date
    # e.g. Born on 1/1, Date is 2/28, days between should be 58 not 57
    days = 365 + IsLeapYear(year)
    return days - DaysBeforeDate(year,month,day)

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    # days after birth year
    # days for years after birth year but before input day
    # days before input day
    #
    # Special cases:
    # year1 == year2
    # Per requirements, don't exclude birth date
    # e.g. Born on 1/1, Date is 2/28, days between should be 58 not 57
    if year1 == year2:
        return (DaysBeforeDate(year2,month2,day2) - DaysBeforeDate(year1,month1,day1))
    else:
        days = DaysAfterDate(year1,month1,day1)
        count = year1 + 1
        while count < year2:
            days = days + 365 + IsLeapYear(count)
            count = count + 1
        return (days + DaysBeforeDate(year2,month2,day2))

# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

