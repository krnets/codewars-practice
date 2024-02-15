def sequence(phrase):
    buttons = ("1", "ABC2", "DEF3", "GHI4", "JKL5", "MNO6", "PQRS7", "TUV8", "WXYZ9", "*0")
    keys_pressed = ""
    prev_key_index = -1

    for c in phrase.upper():
        if c == "#":
            keys_pressed += "#"
        else:
            for i, button in enumerate(buttons):
                if c == " ":
                    keys_pressed += "0"
                    prev_key_index = i
                    break
                elif c in button:
                    if prev_key_index == i:
                        keys_pressed += "p"
                    keys_pressed += str(str((i + 1) % 10) * (button.index(c) + 1))
                    prev_key_index = i
                    break
    return keys_pressed
