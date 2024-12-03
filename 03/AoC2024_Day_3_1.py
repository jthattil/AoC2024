import re
# Define Input File
input = open("input.txt","r").read()
# list_of_lines = input.readlines()

results = 0
pattern = re.compile('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')

#matches.append(re.findall(pattern, input).split('( | ) | , '))
matches = re.findall(pattern, input)
value_multiplier = 1
for i in matches:

    if i == 'do()':
        value_multiplier = 1
        print(i)
        continue
    elif i == 'don\'t()':
        value_multiplier = 0
        print(i)
        continue
    elif 'mul' in i:
        values = i.replace("mul(","")
        values = values.replace(")","")
        values = re.split(',',values)
        values = [int(item) for item in values]
        results += (values[0]*values[1]*value_multiplier)
        print(values,"/t",results)
        continue
    else:
        print("failed")
        break
print(results)
