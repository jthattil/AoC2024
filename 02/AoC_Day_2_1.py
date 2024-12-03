import re
# Define Input File
list_of_lines = open("input.txt","r").readlines()
# list_of_lines = input.readlines()

safe_reports = 0
for x in list_of_lines:
    split_int = [int(y) for y in x.split()]
    test_frame = []
    length = len(split_int)
    for i,k in zip(split_int[:length-1], split_int[1:length]):
        if ((k - i) > 0 and (k - i) <4) or ((k - i) < 0 and (k - i) >-4): 
            test_frame.append(k - i)
            
        else: 
            test_frame = []
            break
    all_negative = (sum(1 for i in test_frame if i < 0) == len(test_frame))
    all_positive = (sum(1 for i in test_frame if i > 0) == len(test_frame))
    if (all_negative or all_positive) and len(test_frame)==len(split_int)-1:
        safe_reports += 1
    print(len(test_frame),"   ",test_frame, "", safe_reports,"",all_positive,"",all_negative)
    
    




# print(list_of_lines)