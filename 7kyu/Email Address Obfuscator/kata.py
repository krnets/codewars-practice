# def obfuscate(email):
#     user_name, fqdn = email.split("@")
#     return " [dot] ".join(user_name.split('.')) + " [at] " + " [dot] ".join(fqdn.split("."))

import re

# def obfuscate(email):
#     return re.sub(r"(@|\.)", lambda m: (" [at] ", " [dot] ")[m.group() == "."], email)


def obfuscate(email):
    return email.translate(str.maketrans({"@": " [at] ", ".": " [dot] "}))
