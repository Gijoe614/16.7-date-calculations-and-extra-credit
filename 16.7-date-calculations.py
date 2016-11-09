
from datetime import datetime

print('This program will get and print the current date and the day of the week.\n\n')


today = datetime.today()


print ('Today is: ' + today.strftime("%A, %B %d, %Y"))
