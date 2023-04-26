calculation_to_units = 24
name_of_units = 'hours'

def days_to_units(num_of_day):
    if num_of_day > 0:
        return f'{num_of_day} days are {num_of_day * calculation_to_units} {name_of_units}'
    elif num_of_day == 0:
        return "You enter a 0, please enter a valid positve number"
    
def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print('your input is not a valid number. Dont ruin my program')

user_input = input("Hey user, enter a number of days to convert to hours? \n")
validate_and_execute()