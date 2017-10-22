import sys
import pymysql as sql
import datetime as dt


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


def replace(item):
    tokens = {'&lt;': '<', '&gt;': '>', '<>': ''}

    for key in tokens:
        item = item.replace(key, tokens[key])

    return item


def main():

    #TODO create connection
    with sql.connect(host='vm-database', port=3306, user='', passwd='', db='mysql') as db:
        cur = db.cursor()

        #TODO
        cur.execute('')

        w = list(cur.fetchall())

    for record in w:
        record = replace(record)

    with open(str(dt.date) + ' ChatHist', mode='w') as file:
        file.writelines(w)


main()
