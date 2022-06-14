FILENAME = "rockyou.txt"

results = []
with open(FILENAME, encoding="latin-1") as f:
    for cnt, line in enumerate(f.readlines()):
        if "user" in line:
            a = input(
                'Line with "user" just found,' 
                " add this line to list?\nYes-y\nNo-n\n"
            )
            if a == "y" or a == "Y":
                results.append(line.replace("\n", ""))
            elif a == "n" or a == "N":
                pass
            else:
                print("you entered invalid value")
print(results, "\n", len(results))
