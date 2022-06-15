FILENAME = 'rockyou.txt'
SEARCH_KEYWORD = "admin"


def read_lines_find_admin() -> list:
    results = []
    with open(FILENAME, encoding="utf-8") as file:
        for word in file.readlines():
            if SEARCH_KEYWORD in word:
                results.append(word)

    print(results)

read_lines_find_admin()
