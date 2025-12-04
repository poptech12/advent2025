current_value=50
zero_counter=0

with open("input.txt", "r") as file:
    for line in file:
        # print ('line: '+line)
        if line[0] == 'R' :
            for _ in range(int(line[1:])) :
                current_value+=1
                if current_value % 100 == 0 :
                    zero_counter+=1
                elif current_value == 0 :
                    zero_counter+=1
        else :
            for _ in range(int(line[1:])) :
                current_value-=1
                if current_value % 100 == 0 :
                    zero_counter+=1
                elif current_value == 0 :
                    zero_counter+=1
    print('number of zeros: '+str(zero_counter))
    #7753 is not correct
    #7073 also incorrect
    #657809 also incorrect
    #6634 is correcr