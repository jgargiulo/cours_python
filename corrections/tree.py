import os

def tree(path, level=0, max=10):
    if level >= max:
        return

    a = list(os.scandir(path))

    for d in a:
        if d.is_dir():
            print("| " * level + "+", d.name)
            tree(path + "/" + d.name, level + 1, max)
        if d.is_file():
            print("| " * level + "-", d.name)


