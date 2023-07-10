def playagain():
    while True:
        try:
            input('\nNow press ENTER to continue and be ready: ')
            start= time.time()
            inp = input('\nStart Typing--> ')
            if len(inp) == 0 or inp != a:
                print('Oops you did not type it right. Please try again')
                print(f'Your input was: ' ,inp)
                print(f'Required input: ' ,a)
            else:
                stop = time.time()
                break
        except Exception as e:
            print(e)
    t = (stop- start)
    print(f'\nHey {name},You took {t} seconds\n\nYour typing speed is {540 / t} wpm(words per minute)')
    print(f'\nThe record of Siddhant is: 6.083929999* seconds, which is 88.75841766* words per minute')
    print("\nIf you think you can beat him then PLAY AGAIN, take screenshot of it and WhatsApp it.")
    YorN()
#----------------------------------------------------------------------------------------#
def YorN():
    while True:
        try:
            again = input("\nPlease press 'Y' to PLAY AGAIN or 'N' to EXIT: ")
            if again=='Y':
                print(f"Welcome back {name}, I know you remember but still it's my job to tell you again")
                print(f'''\nYou have to enter the below phrase exactly as it is and as fast as possible, i.e. The----dog 

                The quick brown fox jumps over the lazy dog

**Note: The timer will start as soon as you press the ENTER KEY** ''')
                playagain()
            elif again=='N':
                print(f'Thanks for playing {name}, I am glad you tried it')
                input('Press Enter to exit, bye-bye: ')
                sys.exit()
            else:
                print("\nPlease Enter 'Y' or 'N' only")
        except Exception as e:
            print(e)

#-----------------------------------------------------------------------------------------#

if __name__== "__main__":

    import time, sys

    a = 'The quick brown fox jumps over the lazy dog'
    name = input("**Typing Master created by Siddhant**\n\nHi there, I am the Typing Master. Siddhant created me and today I will tell you, your typing speed.\n\nWhat's your good name? ")
    if len(name) == 0:
        name = 'Benaam'
        print("\nStrange you don't have a Name, no problem.")
    else:
        pass
    print(f'''\nHi {name}, You have to enter the below phrase exactly as it is and as fast as possible, i.e. The.....dog 

                    The quick brown fox jumps over the lazy dog

    **Note: The timer will start as soon as you press the ENTER KEY** ''')
    playagain()
     

#-----------------------------------------------------------------------#

