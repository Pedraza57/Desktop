
def days_to_units(num_of_days, convertion_unit):#func days to convert and time_unit
    if convertion_unit == 'hours':
        return f'{num_of_days} days are {num_of_days*24} hours'
    elif convertion_unit == 'minutes':
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsuported unit"

def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary['days']) #change input to digit from key days
        if user_input_number > 0: #calling function(first parameter num of days, value of units dic)
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary['units'])
            print(calculated_value)
        elif user_input_number == 0:
            print("you enter a 0, plase enter a valid positive number")
        else:
            print("you enter a negative number, no convertion for you")
    except ValueError:
        print("your input is not a valid number. dont ruin the program")
    
user_input = '' # to start the while True
while user_input != 'exit':  #to end the program
    user_input = input('Hey user, enter number of days and convertion units\n') #input by user 
    days_and_unit = user_input.split(':') #input answer seperated by ':'
    days_and_unit_dictionary = {"days": days_and_unit[0], "units": days_and_unit[1]} #making the dictionary and which values to pull from 
    print(days_and_unit) #showing what we have 
    print(days_and_unit_dictionary) #showing the dictionarys set
    validate_and_execute() #executing the second function 


