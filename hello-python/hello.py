    
    
    
message = input("Enter a comma separated list of numbers: ")
numbers = message.split(",")

total = 0.0
for x in range(len(numbers)):
    f = float(numbers[x])
    total += f * f


print("Sum of squares: ", total)