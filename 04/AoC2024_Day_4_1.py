# Define Input File
with open("input.txt","r") as input_file:
    list_of_lines = input_file.read().splitlines() 

# Create list matrix
char_matrix = []
#total_lines = len(list_of_lines)-1
test_list = ["X", "M", "A", "S"]
matches = 0

for i in range(len(list_of_lines)):
    #print(list_of_lines[i])
    temp_char_list = []
    temp_char_list = [char for char in list_of_lines[i]]
    temp_char_list.insert(0,'')
    temp_char_list.append('')
    char_matrix.append(temp_char_list)
print(char_matrix)
empty_list_item = ['' for x in range(len(char_matrix[0]))]
char_matrix.insert(0,empty_list_item)
char_matrix.append(empty_list_item)

total_lines = len(char_matrix)-1
char_length = len(temp_char_list)-1

line_current_index = 0
for line in char_matrix:
    # reset char index for new line
    char_current_index = 0

    print(line)
    
    for char in line:
        up_check = []
        down_check = []
        left_check = []
        right_check = []
        left_up_check = []
        right_up_check = []
        left_down_check = []
        right_down_check = []
        check_list = []
        if char != 'X':
            char_current_index += 1
            continue
        else:
            for i in range(0,4):
                print("Line Current Index: ", line_current_index,"  Char Current Index: ",char_current_index,"  Min:",min(line_current_index+i,total_lines),"  Total Matches: ",matches)
                up_check.append(char_matrix[max(line_current_index-i,0)][char_current_index]) #up check
                down_check.append(char_matrix[min(line_current_index+i,total_lines)][char_current_index]) #down check
                left_check.append(char_matrix[line_current_index][max(char_current_index-i,0)]) #left check
                right_check.append(char_matrix[line_current_index][min(char_current_index+i,char_length)]) #right check
                left_up_check.append(char_matrix[max(line_current_index-i,0)][max(char_current_index-i,0)]) #left up check
                right_up_check.append(char_matrix[max(line_current_index-i,0)][min(char_current_index+i,char_length)]) #right up check
                left_down_check.append(char_matrix[min(line_current_index+i,total_lines)][max(char_current_index-i,0)]) #left down check
                right_down_check.append(char_matrix[min(line_current_index+i,total_lines)][min(char_current_index+i,char_length)]) #right down check
            if up_check == test_list: 
                print("Up ",up_check)
                matches+= 1
            if down_check == test_list: 
                print("Down ",down_check)
                matches+= 1
            if left_check == test_list: 
                print("Left ",left_check)
                matches+= 1
            if right_check == test_list: 
                print("Right ",right_check)
                matches+= 1
            if left_up_check == test_list: 
                print("Left Up ",left_up_check)
                matches+= 1
            if right_up_check == test_list: 
                print("Right Up ",right_up_check)
                matches+= 1
            if left_down_check == test_list: 
                print("Left Down ",left_down_check)
                matches+= 1
            if right_down_check == test_list: 
                print("Right Down ",right_down_check)
                matches+= 1
        
        
        char_current_index += 1
    
    #increment line index
    line_current_index += 1


print("Total Matches: ",matches)