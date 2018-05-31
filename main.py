from firstTopResults import topResults
from users_registration import registration
from ratings import first_rate

try:
    number= int(input('\n\nHello, how many people are there in your group?\n\n'))
    if(number>1):
        print('You have chosen Group Recommendation\n\n')
        listName= registration(number)
        [listPOI, listCat]= topResults()
        first_rate(listName,listPOI, listCat)
        #print("USERS LIST:", listName, '\n')
        #3
        # print("POIs LIST:", listPOI, '\n')


    elif (number==1):
        print('You have chosen Individual Recommendation\n\n')
        name = input("What's your name?\n")
        print("Ok,", name, " rate your favourite POIs\n\n")
        listPOI= topResults()

    else:
        print('Your choose is wrong')
except ValueError as err:
    print('It is an exception')
    print(err)




#print('In the group there are', number, 'people')
