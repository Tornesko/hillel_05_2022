FILENAME = 'rockyou.txt'

results = []
with open(FILENAME, encoding="latin-1") as f:
    a = input('Do you want to add lines with \"user\" to list?\nYes-y\nNo-n\n')
    if a == 'y' or a == 'Y':
        for cnt, line in enumerate(f.readlines()):
            if "user" in line:
                results.append(line.replace("\n", ""))
    elif a == 'n' or a == 'N':
        pass
    else:
        print("you entered invalid value")
print(results, '\n', len(results))
