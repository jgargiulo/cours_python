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


def tree2(path):
    for root, _, files in os.walk(path):
        depth = root.count(os.sep)
        print(depth * '| ' + '+ ' + os.path.basename(root))
        for f in files:
            print((depth + 1) * '| ' + '- ' + f)
