
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###


list = [1, 3, 17, 9, 15, 2, 4, 1, 10, 12]
next = 1 
count = 0


for num in list[1:]:
    odd_count = 0
    even_count = 0
    if num % 2 == 0:
        if next % 2 ==0:
            even_count += 1
            next += 1 
    elif num % 2 != 0:
        if next % 2 != 0:
           odd_count += 1
           next += 1 
    else:
        next +=1
    print(even_count, odd_count)        