from registration import signin, login, search, commitGroup,commitPOI,commitRate
import sys
from firstTopResults import topResults
from ratings import first_rate
from FA import FairenessAverage
from LMW import LeastMostWithout
import numpy as np


#Create a Group
def createGroup():
    listUserID = list()
    listUsers = list()

    #LOGIN
    userID, username = login()
    listUserID.append(userID)
    listUsers.append(username)

    #Number of people and name for the group
    groupName = input("How do you want to call the group?\n")
    numUsers = int(input("How many people do you want to add into your group?\n"))

#for each user we obtain ID and the username
    for i in range(0, numUsers):

        userID,username= search()
        listUserID.append(userID)
        listUsers.append(username)

    print("\nYour group is composed by: ")
    for i in range(0, len(listUsers)):
        print(listUsers[i])

    print("\n\n")
    ratingsArraylists=list()


#for each user we ask ratings and we append this ratings in a list
    [listPOI, listCat, listID] = topResults()
    for i in range(0, len(listUsers)):
        print("Hey ",listUsers[i], " you are invited to join the group ", groupName, ". Do you want to join? (Y/N)" )
        response = input()
        response= 'y'
        if response=='y':
            userID,username= login()
            if(userID==listUserID[i]):
                ratingsArray=list(first_rate(username,listPOI, listCat))
                #print(type(ratingsArray))
                #print(ratingsArray)
                ratingsArraylists.append(ratingsArray)

#we convert the ratingsArrayLists in array
    ratingsArrayPOI = np.array(ratingsArraylists)
    print(ratingsArrayPOI)


    #fairenessAverage algorithm
    final_listA = FairenessAverage(ratingsArrayPOI, listPOI, listUsers)
    print("The ordered list with FairenessAverage is this:")
    for i in range(0, len(listPOI)):
        print(i + 1, '.', final_listA[i])

    print('\n\n')

#LeastMostWithout algorithm
    final_listB, len_POIModified = LeastMostWithout(ratingsArrayPOI, listPOI, listUsers)
    print("The ordered list with LeastMostWithout is this:")
    for i in range(0, len_POIModified):
        print(i + 1, '.', final_listB[i])

    groupID= commitGroup(listUserID,groupName)
    commitPOI(listID,listPOI)
    commitRate(groupID,listUserID,listID,ratingsArrayPOI)

#Menu where you choose if you want to register a user , to create a group or to exit
def menu():
    ans=True
    while ans:
        print ("""
        1.Register a user
        2.Create a group
        3.Exit/Quit
        """)
        ans=input("What would you like to do? ")
        if ans=="1":
          print("\n Registration")
          signin()
        elif ans=="2":
            createGroup()
          # print("\n Log in")
          # name= login()
        elif ans=="3":
          print("\n Goodbye")
          sys.exit()
        elif ans !="":
          print("\n Not Valid Choice Try again")


