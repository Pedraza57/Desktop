calculation_to_units = 24
name_of_units = 'hours'

def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days*calculation_to_units} {name_of_units}'

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you enter a 0, plase enter a valid positive number")
        else:
            print("you enter a negative number, no convertion for you")
    except ValueError:
        print("your input is not a valid number. dont ruin the program")
    

while user_input != 'exit': 
    user_input = input('Hey user, enter a number of days and i will convert it to hours!\n')
    validate_and_execute()
    