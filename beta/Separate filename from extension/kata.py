import re


# def separate_filename_from_extension(file_path):
#     path = "".join(re.findall(r"\/\.?\w+", file_path))
#     return path, file_path[len(path) :]

import pathlib


def separate_filename_from_extension(file_path):
    p = pathlib.Path(file_path)
    extension = "".join(p.suffixes)
    m = len(file_path) - len(extension)
    return file_path[:m], extension
