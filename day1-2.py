with open("day2.txt") as my_file:
    array = my_file.readlines()

depth = 0
hori = 0
aim = 0
for i in array:
  if i.split(' ')[0] == "up":
    aim = aim - int(i.split(' ')[1])
  if i.split(' ')[0] == "down":
    aim = aim + int(i.split(' ')[1])
  if i.split(' ')[0] == "forward":
    hori = hori + int(i.split(' ')[1])
    depth = depth + (aim * int(i.split(' ')[1]))
print(depth*hori)

with open("day1.txt") as my_file:
    array2 = my_file.readlines()

total = 0
arr2 = [0 for i in range(10000)] 
index = 0
x = len(array2)
for i in range(x-1):
  sum2=0
  for k in range(3):
    if i+k < x:
      sum2 = sum2 + int(array2[i+k])
    else:
      sum2 = 0
  arr2[index] = sum2
  index += 1
total = 0
for i in range(len(arr2)-1):
  if int(arr2[i]) < int(arr2[i+1]):
    total += 1
print(total)
