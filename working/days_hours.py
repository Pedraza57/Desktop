calculation_to_units = 24
name_of_units = 'hours'

def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days*calculation_to_units} {name_of_units}'

def validate_and_execute():
    try:
        user_input_number = int(x)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you enter a 0, plase enter a valid positive number")
        else:
            print("you enter a negative number, no convertion for you")
    except ValueError:
        print("your input is not a valid number. dont ruin the program")
    
user_input = ''
while user_input != 'exit': 
    user_input = input('Hey user, enter number of days as a comma seperated list and i will convert it to hours!\n')
    for x in set(user_input.split(',')):
        validate_and_execute() 


