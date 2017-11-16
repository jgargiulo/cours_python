import os

def list_files(path, ext):
    res = []
    for r, d, fs in os.walk(path):
        for f in fs:
            if f.endswith(ext): 
                res.append(r + "/" + f)

    return res

# str -> [str]
def find_term(file_to_parse, term):
    words = []
    with open(file_to_parse, "r") as f:
        for line in f:
            if term in line: 
                line = line.strip()
                words.append( line.split(":")[1].strip() ) 

    return words

def find_list(file_to_parse, term):
    words = []
    found = False
    with open(file_to_parse, "r") as f:
        for line in f:
            if found and line.strip().startswith("-"):
                print(line.strip())
                words.append(line.strip())
            else:
                found = False
            if term in line: 
                found = True

    return words

if __name__ == "__main__":

    fs = list_files(".", "yml")

    for f in fs:
        print("--------")
        print(f)
        for i in find_term(f, "image"):
            print("  " + i)

    for f in fs:
        print("--------")
        print(f)
        print(find_list(f, "ports"))
