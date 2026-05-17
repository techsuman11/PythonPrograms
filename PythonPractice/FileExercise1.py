with open("input.txt","w") as f:
    f.write("6,8\n7,6\n2,8\n9,5\n9,6")

def countNum(num):
    count = 0
    with open("input.txt","r") as f:
        for line in f:
            numbers=line.split(",")
            for number in range(len(numbers)):
                if int(numbers[number]) == num:
                    count += 1

    return count

print(countNum(6))

