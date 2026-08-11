# remove white space from string
# name = name.strip()

# enter user bill and add 15% additional tax to the bill amount.
bill=float(input("enter your bull - "))

total = bill + (bill/100*15)
print (f'your total bill with additional chargers {total}')

# seperate name to first and last name 
name= input('enter name : ')

name = name.strip()
first , last = name.split(' ')
print(f'first bame is {first} and last name is {last}')
