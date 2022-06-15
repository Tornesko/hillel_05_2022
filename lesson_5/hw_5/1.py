import operator

LOGGING = True

team: list[dict] = [
    {"name": "John", "age": 20, "number": 6},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]

list_num = [dct["number"] for dct in team]


def repr_players(
    players: list[dict], rotation: bool = False, key: str = "number"
) -> None:  
    if rotation is True:
        team.sort(key=operator.itemgetter(f"{key}"))

    print("TEAM:")
    for player in players:
        print(
            f"\t{player['number']} " f"Name:"
            f" {player['name']}, Age: {player['age']}"
        )
    print("\n")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <- ***")


def add_player(num: int, name: str, age: int) -> None:
    player = {"name": name, "number": num, "age": age}
    if player["number"] not in list_num:
        team.append(player)
        list_num.append(player["number"])
        log(message=f"Adding {player['name']}")
    else:
        log(message="Player by this number already exists")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def update_player(players: list[dict], num: int, name: str, age: int) -> None:
    if num in list_num:
        for i, d in enumerate(players):
            if d["number"] == num:
                players[i]["name"] = name
                players[i]["age"] = age
                log(message=f"Player №{num} has updated")

            else:
                pass
    else:
        log(message=f"Player with this number {num} doesn't exist")


#                        TESTS
# __________________________________________________________
add_player(num=7, name="Cris", age=31)
# ______________________________________
# -> -> -> Adding Cris <- <- <- ***
# ______________________________________
add_player(num=7, name="Bob", age=39)
# __________________________________________________________
# -> -> -> Player by this number already exists <- <- <- ***
# __________________________________________________________

repr_players(team)  # without sort
# ______________________________________
#   TEAM:
# 	6 Name: John, Age: 20
# 	3 Name: Mark, Age: 33
# 	12 Name: Cavin, Age: 17
# 	7 Name: Cris, Age: 31
# ______________________________________

repr_players(team, True)  # sort by number(default)
# ______________________________________
#  TEAM:
# 	3 Name: Mark, Age: 33
# 	6 Name: John, Age: 20
# 	7 Name: Cris, Age: 31
# 	12 Name: Cavin, Age: 17
# ______________________________________
repr_players(team, True, "name")  # sort by name
# ______________________________________
#  TEAM:
# 	12 Name: Cavin, Age: 17
# 	7 Name: Cris, Age: 31
# 	6 Name: John, Age: 20
# 	3 Name: Mark, Age: 33
# ______________________________________
repr_players(team, True, "age")  # sort by age
# ______________________________________
#  TEAM:
# 	12 Name: Cavin, Age: 17
# 	6 Name: John, Age: 20
# 	7 Name: Cris, Age: 31
# 	3 Name: Mark, Age: 33
# ______________________________________

update_player(team, num=24, name="Frodo", age=51)
# _______________________________________________________________
# -> -> -> Player with this number 24 doesn't exist <- <- <- ***
# _______________________________________________________________

update_player(team, num=7, name="Frodo", age=51)
# __________________________________________________________
# -> -> -> Player №7 has updated <- <- <- ***
# __________________________________________________________
repr_players(team)  # after update
# ______________________________________
#  TEAM:
# 	12 Name: Cavin, Age: 17
# 	6 Name: John, Age: 20
# 	7 Name: Frodo, Age: 51
# 	3 Name: Mark, Age: 33
# ______________________________________
