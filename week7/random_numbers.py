
import random

def main():
    #Creates a list named numbers like this:
    numbers_list=[16.2, 75.1, 52.3]
    #Prints the numbers list
    print(numbers_list)
    #Calls the append_random_numbers function with only one argument to add one number to numbers
    append_random_numbers(numbers_list)
  
    #Prints the numbers list
    print(numbers_list)
    #Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    append_random_numbers(numbers_list,2)
    #Prints the numbers list
    print(numbers_list)

#Prints the numbers list
#append_random_numbers
def append_random_numbers(numbers_list,quantity=1):
    #Has two parameters: a list named numbers_list and an integer named quantity. The parameter quantity has a default value of 1
    
#Computes quantity pseudo random numbers by calling the random.uniform function.
    for _ in range (quantity):
        random_number=random.uniform(1,100)
        #Rounds the quantity pseudo random numbers to one digit after the decimal.
        random_number = round(random_number, 1)
        #Appends the quantity pseudo random numbers onto the end of the numbers_list.
        numbers_list.append(random_number)


if __name__ == "__main__":
    main()