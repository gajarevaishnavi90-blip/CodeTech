total = 0
count = 0

with open("data/students.txt") as f:
    for line in f:
        name, marks = line.strip().split(",")
        print(name, "->", marks)
        total += int(marks)
        count += 1

print("Average marks:", total / count)