def which_note(key_press_count):
    piano = (["A", "A#", "B"]
             + ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"] * 7
             + ["C"])
    return piano[(key_press_count - 1) % 88]
