#"""When you physically exercise to strengthen your heart, you
#should maintain your heart rate within a range for at least 20
#minutes. To find that range, subtract your age from 220. This
#difference is your maximum heart rate per minute. Your heart
#simply will not beat faster than this maximum (220 - age).
#When exercising to strengthen your heart, you should keep your
#heart rate between 65% and 85% of your heart’s maximum rate.
#"""
import math
from math import floor, ceil
age=int(input("What is your age? "))
 
max_HR = 220 - age 
min_BPM = max_HR * .65
max_BPM = max_HR * .85 
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {min_BPM:.0f} and {max_BPM:.0f} beats per minute.")