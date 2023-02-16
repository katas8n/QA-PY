# 1) Image the number that u want and then put it into variable (create variable with number value)
# 2) Propose user guess this number
# 3) if user_number bigger than ur , say to user : ur number bigger than mine
# 4) if user_number less than ur , say to user : ur number less than mine
# 5) if user_number equal to our , say to user : Impossible
# 5) if user_number is not a number : WTH ?
# 6) Progam works until user guess the number


# magic_number = 23

# switcher = True

# while switcher:
#     user_number = input("Eneter your number : ")

#     user_number_number_typed = int(user_number)

#     if magic_number == user_number_number_typed:
#         print("Impassible")
#         switcher = False
#     # * elif (if else)
#     elif magic_number < user_number_number_typed:
#         print("Ur number bigger than mine")
#     elif magic_number > user_number_number_typed:
#         print("Ur number less than mine")


# * ++++++++++++++++++++++++++++++++++++++++++++++

# 1) get user name , if user_name length < 2 => Incorrect data , try again
# 2) user_name length > 2 => Do you want to register here ? y/n :
# 3) if "y" -> enter your email => if email contain "@" -> it's valid , otherwise -> invalid -> try again
# 4) if "n" -> goodbye
# 5) if something else -> incorrect data try again later
# 6) Programm works until user enter correct (valid) data ;

# * +++++++++++++++++++++++++++++++++++++++++++++++

# is_running = True

# while is_running:
#     user_name = input("Enter your name : ")

#     if len(user_name) > 2:

#         user_choose = input("Do you want to register here ?")

#         # lower
#         if user_choose.lower() == "y":

#             user_email = input("Eneter your email : ")

#             i = 0

#             is_snail_exist = False

#             while i < len(user_email):
#                 char = user_email[i]

#                 if char == "@":

#                     is_snail_exist = True
#                     print("All right")

#                 i = i + 1

#             if is_snail_exist:
#                 print("Correct data")
#                 is_running = False

#             else:
#                 print("Incorrect data , enter your name again")

#         else:
#             print("Goodbye")

#     else:
#         print("Your name short that I expect")

#         is_exit = input("Do you wanna try again ? y / n : ")

#         if is_exit == "y":
#             print("Okay")

#         elif is_exit == "n":
#             is_running = False
