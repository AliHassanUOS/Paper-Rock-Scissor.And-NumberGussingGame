print("ALLAH")
computer_count = 0
user_count = 0
import random

possible_output = ("rock", "paper", "scissor")


while True:


    useraction = input("Select any one thing (rock,paper,scissor) ")

    possible_output = ("rock","paper","scissor")

    computer_action = random.choice(possible_output)

    print(f"Your Choice  is {useraction} and computer select {computer_action}")

    if useraction == computer_action:
        print(f"Both Choice same action, Computer action {computer_action} and user action {useraction}, Game Tie ")

    elif useraction == "rock":
        if computer_action == "paper":
            print(f"You Loss {computer_action} covers {useraction}")
            computer_count = computer_count+1
        else:
            print(f"You win {computer_action} smashed by {useraction}")
            user_count = user_count+1

    elif useraction == "paper":
        if computer_action == "scissor":
            print(f"You loss ! {computer_action} cuts {useraction}")
            computer_count = computer_count+1

        else:
            print(f"You win ! {computer_action} covered by {useraction}")
            user_count = user_count +1

    elif useraction == "scissor":
        if computer_action == "rock":
            print(f"You loss ! {computer_action} smash {useraction} ")

            computer_count = computer_count+1

        else:
            print(f"You win {computer_action} cuts by {useraction}")
            user_count = user_count+1

    play_again = input("Play again [y,n]")
    if play_again== "n".lower():
        break


if user_count==computer_count:
    print("Both players have same score")
elif user_count > computer_count:
    print(f"User wins ! with {user_count} score and computer score is  {computer_count}")
else:
    print(f"Computer wins ! with {computer_count} score and user score is {user_count}")


print(f"Your Total score is {user_count}")
print(f"computer total count is {computer_count}")
print("Thank You for play our game ")










############################ Number Guseing game ############################################################
# import random
# print("You have only 8 chance for guess the number ")
# count = 0
# while True:
#     print("Type 00: Quit")
#     userinput = int(input("Guess the number between 1,100 "))
#     computeroutput = random.randint(1, 50)
#     if userinput == 00:
#         break
#     if userinput > computeroutput:
#         print("You entered greater number")
#         print(f"your number is {userinput} and computer number is {computeroutput}")
#     if userinput < computeroutput:
#         print("You entered less number ")
#         print(f"Your Number is {userinput} and computer number is {computeroutput}")
#     if userinput == computeroutput:
#         print("Congratulation, Your Number match with computer number")
#         print(f"Your number is {userinput} and computer number is {computeroutput}")
#         break
#     count = count+1
#     if count == 8:
#         print("You have completed your chance, Best of luck in next time ")
#         break
#     print(
#         f"You have lost {count}"
#     )
# print("Thank You for played our game ")

############################## Password Generetor in python ############################################################
# import random
#
# class passwordgeneretor(object):
#
#     def password(self):
#
#         a = "abcdefghijklmnopqrstuviwxz"
#         A ="ABCDECGHIJKLMNOPQURISTUSDFV"
#         a1 = "1234567890"
#         special = "!@#$%^&*()_+|}?><;"
#
#         combine = a+A+a1+special
#         result = "".join(random.choice(combine) for x in range(random.randint(8,10)))
#         print(result)
#
# obj = passwordgeneretor()
# obj.password()

# enterage = int(input("Enter Age in Year"))
# ans=24*365
#
# result = ans*enterage
# print(f"You have spent {result} mints in {enterage} years")

# numberinput = int(input("How many number you want to store ?"))
#
# newlist = []
# for i in range(1,numberinput+1):
#     addnum = input("Enter numbers according +92 format ")
#     lenght = len(addnum)
#     if lenght == 13:
#         newlist.append(addnum)
#     else:
#         print("Enter correct length number ")
#
#
#
# print(newlist)