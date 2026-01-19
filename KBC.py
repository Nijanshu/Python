name=input('Enter your name ')
print('Welcome to the Game',name)

Questions=["Where is Taj Mahal?",'Where is Qutab Minar?','Where is Gateway of India?']
Answers=['Agra','Delhi','Mumbai']

money=0

for i in range(len(Questions)):
    while True:  # This loop will continue until the correct answer is given
        print(Questions[i])
        ans = input('Answer: ').lower()
        if ans == Answers[i].lower():
            print('Congratulations! You won Rs', 1000*(i+1))
            money = (i+1)*1000
            break  # Exit the while loop and move to the next question
        else:
            print('Sorry, your answer is not correct, please try again.')


print("You have won Rs", money)
