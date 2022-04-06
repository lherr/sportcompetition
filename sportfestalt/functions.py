import pymysql.cursors

def connection():
    return pymysql.connect(host='localhost',
                    user='sportfestadmin',
                    password='Sportfest',
                    db='Sportfest',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)