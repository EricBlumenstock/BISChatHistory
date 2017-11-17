import sys
import os
import pymysql as sql
import datetime as dt


def replace(item: str, tokens: dict) -> str:

    for key in tokens:
        item = item.replace(key, tokens[key])

    return item

def main():
    tokens = {'&lt;': '<', '&gt;': '>', '<>': '', '",), ("': '<hr>', ',), ("': '<hr>', """",), ('""": '<hr>', '(("': '',  '",))': ''}

    with sql.connect(host='HOST', port=3306, user='USERNAME', passwd='PASSWORD', db='mysql') as db:

        db.execute("""SELECT formatted FROM PHPLive_ChatV4.p_transcripts
        WHERE deptID IN (SELECT deptID FROM PHPLive_ChatV4.p_dept_ops WHERE opid = 28)
        ORDER BY created desc""")

        w = str(db.fetchmany(int( (sys.argv[1] if len(sys.argv) >= 2 else 10 ) )))

    w = replace(w, tokens)

    with open(os.path.expanduser("~/Desktop/" + str(dt.date.today()) + ' ChatHist.html'), mode='w', encoding='utf8') as file:
        file.writelines(w)


main()





#Unused Function
#For fixing a file provided as an argument
#fileFix(sys.argv[1])
def fileFix(path: str):

    tokens = {'&lt;': '<', '&gt;': '>', '<>': ''}
    w = list()

    with open(path, mode='r', encoding='utf8') as file:

        for line in file:
            line = replace(line, tokens)
            w.append(line)

    with open(path, mode='w', encoding='utf8') as file:
        file.writelines(w)
