from datetime import datetime


def calculate_age():
    if cdate > datetime(cdate.year, bdate.month, bdate.day):
        age = cdate.year - bdate.year
        next_year = True
    else:
        age = cdate.year - bdate.year - 1
        next_year = False
    print("\nYou are {} years old.".format(age))
    return next_year


def time_2next_birthday():
    time2bday = datetime(cdate.year + next_year, bdate.month, bdate.day) - cdate
    days = time2bday.days
    hours, remainder = divmod(time2bday.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print ('\nYou have ' + str(days) + ' days,'),
    print (str(hours) + ' hours,'),
    print (str(minutes) + ' minutes, and'),
    print (str(seconds) + ' seconds'),
    print ('left until your next birthday!!!')


bdateInput = input('\nPlease enter the date of your birth in the format "mm/dd/yyyy" and include quote marks: ')


bdate = datetime.strptime(bdateInput, '%m/%d/%Y')


cdate = datetime.now()


next_year = calculate_age()


time_2next_birthday()
