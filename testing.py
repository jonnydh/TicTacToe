gameboard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def get_available_spaces():
    available_spaces = []
    index = 0
    for space in gameboard:
        if space == " ":
            available_spaces.append(index)
        index += 1
    return available_spaces


def output_available_spaces(spaces):
    output = ""
    index = 0
    for space in spaces:
        if index < len(spaces) - 2:
            output += f"{str(space)}, "
        elif index < len(spaces) - 1:
            output += f"{str(space)} or "
        else:
            output += str(space)
        index += 1
    print(output)


spaces = get_available_spaces()
output_available_spaces(spaces)
