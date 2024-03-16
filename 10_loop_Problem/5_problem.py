# find the first non repeated character

input_str = "sidmid"
for i in input_str:
    print(i)
    if input_str.count(i) == 1:
        print("char is: ",i)
        break 
