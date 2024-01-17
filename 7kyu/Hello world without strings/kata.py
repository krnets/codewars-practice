def hello_world():
    return (chr(44) + chr(32)).join(map(str.title, hello_world.__name__.split(chr(95)))) + chr(33)
