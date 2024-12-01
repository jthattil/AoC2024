import re
# Define Input File
list_of_lines = open("01/input.txt","r").readlines()
# list_of_lines = input.readlines()

left_list = []
right_list = []
total_similarity = 0
for x in list_of_lines:
    #for y in line_int:
    split_int = [int(y) for y in x.split()]
    left_list.append(split_int[0])
    right_list.append(split_int[1])

left_list.sort()
right_list.sort()

for l in left_list:
    occurrences = right_list.count(l)
    if occurrences > 0: 
        print(l,"  ",occurrences)
    total_similarity = total_similarity + (l * occurrences)


print("Total Distance is :",total_similarity)


# print(list_of_lines)