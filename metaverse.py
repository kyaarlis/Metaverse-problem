import math

# T = int(input("Test case num: "))
friendsAndDays = input("Num of friends in your group and total days: ")

inputs = friendsAndDays.split()

# Total number of friends
N = int(inputs[0])
# Total number of days
M = int(inputs[1])

frequency = []
Pn = []

def loginDayFrequency():
    for x in range(N):
        frequency = int(input(f'P {x+1}: '))

        print('Friend', x+1 , 'logs in every', frequency, 'days')

        Pn.append(frequency)

loginDayFrequency()
print(' ')

totalDaysLoggenIn = 0

def loginDaysForEachUser(Pn, M):
    for x in range(len(Pn)):
        totalDaysLoggedIn =  math.ceil(M / Pn[x])
        
        print('Friend', x+1 , 'logged in', totalDaysLoggedIn, 'days in total')
        
loginDaysForEachUser(Pn, M)

friendLists = []


def sameDayLogin():
    original_value = 1
    x = original_value

    for i in range(N):    

        global friend
        friend = [] 
        for j in range(M):
            while x < M:
                x += Pn[i]
                if x <= M:
                    friend.append(x)
                break
        if x >= M:
            x = original_value

        friendLists.append(friend)    
                      
sameDayLogin()

print(friendLists)

def simontaniousDays():
    count = 1

    for i in friendLists:
        for j in friend:
            if i == j:
                count+=1

    print(f'Both friend same day login happened {count} times')

simontaniousDays()
            
 