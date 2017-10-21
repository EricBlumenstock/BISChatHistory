import sys
import pymysql as sql

def filetokenreplace(path):

    tokens = {'&lt;': '<', '&gt;': '>', '<>': ''}
    w = list()

    with open(path, mode='r') as file:

        for line in file:
            for key in tokens:
                line = line.replace(key, tokens[key])
            w.append(line)

    with open(path, mode='w') as file:
        file.writelines(w)

    filetokenreplace()


def main():
    filetokenreplace(sys.argv[1])

    sql.connect()


main()
