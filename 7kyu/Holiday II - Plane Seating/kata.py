def plane_seat(a):
    row, col = int(a[:-1]), a[-1]
    if col not in "ABCDEFGHK" or not 1 <= row <= 60:
        return "No Seat!!"
    section = ("Front", "Middle", "Back")[(row > 20) + (row > 40)]
    cluster = ("Left", "Middle", "Right")[(col > "C") + (col > "F")]
    return f"{section}-{cluster}"
