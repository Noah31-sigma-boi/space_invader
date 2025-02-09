
tiles = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turn_player = 0
icon = None
end = False

def tableau():
    print("",tiles[0],"|",tiles[1],"|",tiles[2])
    print("---+---+---")
    print("",tiles[3],"|",tiles[4],"|",tiles[5])
    print("---+---+---")
    print("", tiles[6],"|",tiles[7],"|",tiles[8])

tableau()

while turn_player != 9 and end == False:
    case = int(input("case -> "))
    if case > 9:
        print("tile out of range. Take an other one")
        case = int(input("case -> "))

    if turn_player % 2 == 0:
        icon = "o"

    else:
        icon = "x"

    if tiles[case-1] == " ":
        tiles[case - 1] = icon
    else:
        turn_player -=1
        print("You cannot take this tile (unavailable). Take an other one")

    if tiles[0] == tiles[1] == tiles[2] != " " or tiles[3] == tiles[4] == tiles[5] != " " or tiles[6] == tiles[7] == tiles[8] != " " or tiles[0] == tiles[3] == tiles[6] != " " or tiles[1] == tiles[4] == tiles[7] != " " or tiles[2] == tiles[5] == tiles[8] != " " or tiles[0] == tiles[4] == tiles[8] != " " or tiles[2] == tiles[4] == tiles[6] != " ":
        print("We have a winner !")
        if icon == "o":
            print("player 1")
        else:
            print("player 2")
        end = True
    else:
        turn_player += 1
    tableau()