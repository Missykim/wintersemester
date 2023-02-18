from datetime import datetime, timedelta

current_date= datetime.now()

print('todays:' + str(current_date))

total=float(input( 'What is your total? '))

today=datetime.now(tz=None)  
#datetime.day()
day_of_week = current_date.weekday()
print(f'The day of the week is {day_of_week}')
tax= total *.06

if day_of_week == 1 :
    discount=(total *.1) 
    new_total= total - new_total
    subtotal=new_total + tax
elif day_of_week ==  2 :
    print(f'Yes, we got it right.')
    new_total=(total *.1 )
    new_total= total - new_total
    subtotal=new_total + tax
else:
    subtotal=total + tax
 
print(f'Your tax is {tax:.2f}.')
print( f'Your total is {subtotal:.2f} ' ) 


if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * DISC_RATE, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount