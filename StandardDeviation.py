import math
import csv

with open("NuMbEr.csv",newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]

total = 0
n = len(data)

for i in data:
    total += int(i)

mean = total/n

squaredList = []

for i in data:
    a = int(i)-mean
    a = a**2
    squaredList.append(a)

sum = 0

for i in squaredList:
    sum += i

result = sum/n
final_result = math.floor(math.sqrt(result))    

print("The standard deviationn is ",final_result)



