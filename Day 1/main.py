file = open("input.txt")
calorie_list = list()
calories = 0
for line in file:
    if line == "\n":
        calorie_list.append(calories)
        calories = 0
        continue
    else:
        calories += int(line)
file.close()
print("Most calories:", max(calorie_list))
calorie_list.sort(reverse=True)
print("Sum of top 3:", sum(calorie_list[0:3]))




