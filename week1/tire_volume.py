import math
#input from user
 # Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime
width=int(input('What is the width of the tire in millimeters? '))
ratio=int(input('What is the aspect ratio of the tire? '))
diameter=int(input('What is the diameter of the tire in inches? '))

#calculate
volume=((math.pi*width**2*ratio)*(width*ratio + 2540*diameter))/10000000000
print(f'The approximate volume is {volume:.2f}liters.')
#display values

#Gets the current date from the computer’s operating system.
#Opens a text file named volumes.txt for appending.
#Appends to the end of the volumes.txt file one line of text that contains the following five values:
    #current date
    #width of the tire
    #aspect ratio of the tire
    #diameter of the wheel
    #volume of the tire



# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
with open("volumes.txt", "at") as volume_file:
    print(current_date_and_time, file=volume_file,end=', ')   
    print(width, file=volume_file,end=', ')
    print(ratio, file=volume_file,end=', ')
    print(diameter, file=volume_file,end=', ')
    print(f'{volume:.2f}', file=volume_file)


# Use an f-string to print only the date
# part of the current date and time.
#print(f"{current_date_and_time:%Y-%m-%d}{width}{ratio}{diameter}{volume:.2f}")