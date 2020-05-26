Game code
print('Made by Apurwa Gupta')
lose = 'The computer wins'
win = ' You win :)'
lives = 5
score = 0
draw = 0
computer_lives = 7
import random
rock_paper_scissor = ('Rock','Paper','Scissor','exit','rules','display lives','display score','display draw') 
while True:
    print ('Fill in the below information to begin')
    username = input('Please enter your username:  ')
    password = input('Please enter your password:  ')
    searchfile = open("accounts.csv","r")
    import time
    time.sleep(0.5)
    print ('Loading...')
    time.sleep(0.5)
    print ('Loading...')
    time.sleep(0.5)
    print ('Loading...')
    for line in searchfile:
        if username and password in line:
            print ('Access granted, Enjoy the game !')
            print ('Rules')
            print ('Point 1 : ')
            print ('You start with',lives,'in the beginning')
            print ('If you win, you get an extra life, if you lose one life is lost,')
            print ('if you draw life remains the same')
            print ('Point 2 : ')
            print ('To the see game rule again, type rules')
            print ('Point 3 : ')
            print ('To exit the game at any point, type exit')
            print ('GOOD LUCK !!')
            while True:
                
                rps = input ('Rock, Paper, Scissor ?')
                rps = rps.strip().title()
                if rps not in rock_paper_scissor:
                    print ('Invalid input, please try again')
                    continue
                computer = ('Rock','Paper','Scissor')
                computer = random.choice(computer)
                #Rock if statements
                if rps == 'Rock' and computer == 'Paper':
                    print ('The computer choose',computer)
                    print ("")
                    print (lose)
                    print ("")
                    lives -=1
                if rps == 'Rock' and computer == 'Scissor':
                    print ('The computer choose',computer)
                    print ("")
                    print (win)
                    print ("")
                    score+=1
                #Paper if statements
                if rps == 'Paper' and computer == 'Rock':
                    print ('The computer choose',computer)
                    print ("")
                    print (win)
                    print ("")
                    computer_lives -=1
                if rps == 'Paper' and computer == 'Scissor':
                    print ('The computer choose',computer)
                    print ("")
                    print (lose)
                    print ("")
                    lives-=1
                #Scissor if statements
                if rps == 'Scissor' and computer == 'Paper':
                    print ('The computer choose',computer)
                    print ("")
                    print (win)
                    print ("")
                    computer_lives -=1
                    score+=1
                if rps == 'Scissor' and computer == 'Rock':
                    print ('The computer choose',computer)
                    print ("")
                    print (lose)
                    print ("")
                    lives+=1
                #Duplicates
                if rps == 'Rock' and computer == 'Rock':
                    print ('The computer choose',computer)
                    print ("")
                    print ('Draw')
                    print ("")
                    draw+=1
                if rps == 'Paper' and computer == 'Paper':
                    print ('The computer choose',computer)
                    print ("")
                    print ('Draw')
                    print ("")
                    draw+=1
                if rps == 'Scissor' and computer == 'Scissor':
                    print ('The computer choose',computer)
                    print ("")
                    print ('Draw')
                    print ("")
                    draw+=1
                if rps == 'rules':
                    print ('Game Rules : ')
                    print ('1. Rock looses against paper and beats scissor')
                    print ('2. Paper looses against scissor and beats rock')
                    print ('3. Scissor looses against rock and beats paper')
                if rps == 'display lives':
                    print (lives)
                if rps == 'display score':
                    print (score)
                if rps == 'display draw':
                    print (draw)
                #Lives
                if lives == 0 and rps == 'test':
                    print ('Thanks for playing')
                    print ('You have run out of lives')
                    print ('You won',score,'times')
                    print ('You draw',draw,'times')
                    stop = input ('Press enter to exit')
                    exit()
                if computer_lives == 0:
                    print ('Thanks for playing')
                    print ('The computer lost all its lives, You win')
                    print ('You won',score,'times')
                    print ('You draw',draw,'times')
                    stop = input ('Press enter to exit')
                    exit()
            #exit
                if rps == 'exit':
                    break
            else:
                print('Your username or password is incorrect.')
