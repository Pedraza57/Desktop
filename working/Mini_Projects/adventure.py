name = input("Type your name. ")
print(f"Welcome {name} to this adventure!!")

answer = input("Your on a dirt road, it has come to and end and you can go (left / right)? ").lower()

if answer == 'left':
    print("you have now two options fight a snake or an aligator.")
    answer = input("aligator or snake? ")
    if answer == 'aligator':
        print("aligator has had a good dinner :)")
    else:
        print("You won the fight against the snake, but the venom killed you.")

if answer == 'right':
    print("Right was correct way.")
    answer = input('Do you want to swim or cross? ')
    if answer == 'cross':
        print("you have cross the bridge and fell to your dead!!")
    else:
        print('you survive against all odds and swam to safety!!//')

print("Thank you for playing!!")