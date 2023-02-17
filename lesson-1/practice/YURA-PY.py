magic_number = 50
switcher = True
while switcher:
     user_number = input("Eneter your number : ")
     user_number_number_typed = int(user_number)
     if magic_number == user_number_number_typed:
         print("Impassible")
         switcher = False
     elif magic_number < user_number_number_typed:
         print("Ur number bigger than mine")
     elif magic_number > user_number_number_typed:
         print("Ur number less than mine")
