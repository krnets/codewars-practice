import os

def mkdirp(*directories):
    os.makedirs(os.path.join(*directories), exist_ok=True)
