T = int(input("Number of test cases: "))

results = []

for x in range(T):
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


    def sameDayLogin():
        global friendLists
        # this list will contain all of the users login days
        friendLists = []

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

    def simontaniousDays():
        global count
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
        
        results.append(count)
        print(f'Case #{x+1}: {count}')

    simontaniousDays()

    # Here I create a text file containing the output for every test case
    def txt_file_output():
        if x+1 == T:
            # Open a file in write mode
            with open('output.txt', 'w') as file:   
                for r in range(len(results)):
                    # write data to the file
                    file.write(f'Case #{r+1}: {results[r]}\n')
            file.close() 

    txt_file_output()