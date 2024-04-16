import re


def highlight(code):
    syntax_colors = {"F": "pink", "L": "red", "R": "green", "\d": "orange"}

    for k, v in syntax_colors.items():
        code = re.sub(rf"({k}+)", rf'<span style="color: {v}">\g<1></span>', code)

    return code
