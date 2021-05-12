def diamond(letter):
    if letter == "A":
        return "A\nA"
    diamond_top = create_diamond_top(letter)
    diamond_bottom = reverse_lines(remove_last_line(diamond_top))
    diamond_whole = diamond_top + diamond_bottom
    return diamond_whole


def remove_last_line(diamond_top):
    return "\n".join(diamond_top.splitlines()[:-1])


def reverse_lines(diamond_top):
    return "\n".join(diamond_top.splitlines()[::-1])


def create_diamond_top(letter):
    alphabet = "ABCDEFGHIKLMNOPQRSTVXYZ"
    index = alphabet.index(letter)
    diamond_top = ""
    for row_index in range(0, index + 1):
        cur_let = alphabet[row_index]
        spaces = " " * (index - row_index)
        mid_spaces = " " * (2 * row_index - 1)
        if row_index == 0:
            diamond_top += f"{spaces}{cur_let}{spaces}\n"
        else:
            diamond_top += f"{spaces}{cur_let}{mid_spaces}{cur_let}{spaces}\n"
    return diamond_top


print(diamond("A"))
print(diamond("B"))
print(diamond("C"))
print(diamond("D"))
print(diamond("E"))
print(diamond("X"))
