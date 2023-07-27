target = "Lorem ipsum dolor sit amet"
flag = 0
with open("sample1.txt", 'r') as s:
    for line in s.readlines():
        current = line.strip()
        s.close()
        if len(current) == len(target):
            j = 0
            for i in (0,len(current)):
                if target[i] != current[i]:
                    break
                j += 1
                if j == len(current):
                    flag = 1

    if flag == 1:
        print("Was present here")
    else:
        print("Not present")

with open("output.txt", mode="w") as targetfile:
    if flag:
        targetfile.write("Success")
    else:
        targetfile.write("Failed")
    targetfile.close()




