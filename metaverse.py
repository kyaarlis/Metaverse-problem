import math

T = int(input("Test case num: "))
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

    for i in range(len(friendLists[0])):

        current_num = friendLists[0][i]

        # Flag to keep track of whether the number is found in all lists
        found_in_all_lists = True

        for j in range(1, len(friendLists)):

            if current_num not in friendLists[j]:
                found_in_all_lists = False
                break
         # Increment count if the current number is found in all lists
        if found_in_all_lists:
            count += 1

    # print(f'All friend same day login happened {count} times')
    print(f'Case #{T}: {count}')

simontaniousDays()
            
 