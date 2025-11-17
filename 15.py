
with open("hiscore.txt", "r") as f:
    lines = f.readlines()
    print(lines)
with open("hiscore.txt", "w") as f:
    for line in lines:
        if line.strip() != "":
            f.write(line)
