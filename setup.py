from Dice_Simulator import banner,dice

banner()

while True:
    try:
        dice(input("Please Enter Number of dice rolled : "))
    except:
        print('Wrong input .Please enter a number!')