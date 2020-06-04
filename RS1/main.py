from firstTopResults import topResults
from users_registration import registration
try:
    number= int(input('Hello, how many people are there in your group?\n\n'))
    if(number>1):
        print('You have chosen Group Recommendation\n\n')
        listaNomi= registration(number)
        topResults()

    elif (number==1):
        print('You have chosen Individual Recommendation\n\n')
        name = input("What's your name?\n")
        print("Ok,", name, " rate your favourite POIs\n\n")
        topResults()

    else:
        print('Your choose is wrong')
except ValueError as err:
    print('It is an exception')
    print(err)




#print('In the group there are', number, 'people')
