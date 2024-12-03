import re
# Define Input File
list_of_lines = open("input.txt","r").readlines()
# list_of_lines = input.readlines()

safe_reports = 0
for x in list_of_lines:
    split_int = [int(y) for y in x.split()]
    test_frame = []
    defects = 0
    length = len(split_int)
    for i,k in zip(split_int[:length-1], split_int[1:length]):
        test_frame.append(k - i)
    
    #print(test_frame)
    if sum(1 for i in test_frame if i < 0) < sum(1 for i in test_frame if i > 0):
        defects += sum(1 for i in test_frame if i <= 0 and i >= -3)
    else: 
        defects += sum(1 for i in test_frame if i >= 0 and i <= 3)
    
    for i in test_frame:
        if ((i == test_frame[0] or i == test_frame[-1]) and (i > 3 or i < -3)):
            defects +=1
        elif (i != test_frame[0] and i != test_frame[-1] and (i > 3 or i < -3)):
            defects += 2
        else:
            continue
    
    if (defects == 1 or defects == 0):
        safe_reports += 1
    
    
    #if (defects == 1 or defects == 0):
    print(defects,"\tLength: ", len(test_frame), "\tNegative Test: ",sum(1 for i in test_frame if i < 0),"\tPositive Test: ", sum(1 for i in test_frame if i > 0), "\tOther Test: ", sum(1 for i in test_frame if i > 3 or i < -3 or i == 0),"\t",test_frame, "", safe_reports )
print(safe_reports)    
    




# print(list_of_lines)