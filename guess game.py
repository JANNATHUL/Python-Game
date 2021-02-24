import random
print('enter ur name')
myname=input()
print('welcome '+myname)
r=random.randint(1,20)
print('want to guess the number..(s/n)')
play=input()
while play == 's' or play == 'S':
    print('guess a number from 1 to 20')
    for i in range(5):
        try:
            guess = input()
            if r== int(guess):
                print('congrats... u found')
                print('the number is '+ str(r) +' you found in '+ str(i+1)+' guess')
                break
            elif int(guess) > 0 and r > int(guess):
                print('guessed number is low... guess again')
                continue
            elif int(guess) < 21 and r < int(guess):
                print('guessed number is high... guess again')
                continue
            else:
                print('guess a number in between 1-20')
                continue
        except ValueError:
            print('enter integer value from 1 to 20')
            continue
        print('Not found... better luck next time..')
    print('want to continue.. enter (s / n)')
    play=input()
print('catch u later..')
