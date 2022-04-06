#!/usr/bin/env python3

import cgi, hashlib, libs.functions, random, os

random.seed()

form = cgi.FieldStorage()

from libs.config import *

print(HEADER)
print("<section>")
print("<article>")
print("<h1>Zufallsdaten eintragen</h1>")
try:
    connection = libs.functions.connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM Schueler"
    cursor.execute(sql)
    daten = cursor.fetchall()
    connection.close()
    print("<p>Daten erfolgreich aus der Datenbank gelesen!</p>")
except:
    print("<p>Fehler beim Einlesen der Daten aus der Datenbank</p>")

for dsatz in daten:
    if dsatz['geschlecht'] == "männlich":
        if dsatz['stufe'] == 5:
            lauf = random.randint(75, 110) / 10
            sprung1 = random.randint(200, 400) / 100
            sprung2 = random.randint(200, 400) / 100
            sprung3 = random.randint(200, 400) / 100
            wurfstoss1 = random.randint(24, 80) / 2
            wurfstoss2 = random.randint(24, 80) / 2
            wurfstoss3 = random.randint(24, 80) / 2
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                       " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                       "WHERE schnr = '{}';"\
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                #print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 6:
            lauf = random.randint(70, 110) / 10
            sprung1 = random.randint(220, 410) / 100
            sprung2 = random.randint(220, 410) / 100
            sprung3 = random.randint(220, 410) / 100
            wurfstoss1 = random.randint(36, 90) / 2
            wurfstoss2 = random.randint(36, 90) / 2
            wurfstoss3 = random.randint(36, 90) / 2
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 7:
            lauf = random.randint(100, 150) / 10
            sprung1 = random.randint(230, 420) / 100
            sprung2 = random.randint(230, 420) / 100
            sprung3 = random.randint(230, 420) / 100
            wurfstoss1 = random.randint(40, 100) / 2
            wurfstoss2 = random.randint(40, 100) / 2
            wurfstoss3 = random.randint(40, 100) / 2
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 8:
            lauf = random.randint(100, 140) / 10
            sprung1 = random.randint(240, 460) / 100
            sprung2 = random.randint(240, 460) / 100
            sprung3 = random.randint(240, 460) / 100
            wurfstoss1 = random.randint(440, 900) / 100
            wurfstoss2 = random.randint(440, 900) / 100
            wurfstoss3 = random.randint(440, 900) / 100
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 9:
            lauf = random.randint(130, 182) / 10
            sprung1 = random.randint(270, 500) / 100
            sprung2 = random.randint(270, 500) / 100
            sprung3 = random.randint(270, 500) / 100
            wurfstoss1 = random.randint(600, 1000) / 100
            wurfstoss2 = random.randint(600, 1000) / 100
            wurfstoss3 = random.randint(600, 1000) / 100
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 10:
            lauf = random.randint(126, 176) / 10
            sprung1 = random.randint(280, 520) / 100
            sprung2 = random.randint(280, 520) / 100
            sprung3 = random.randint(280, 520) / 100
            wurfstoss1 = random.randint(660, 1040) / 100
            wurfstoss2 = random.randint(660, 1040) / 100
            wurfstoss3 = random.randint(660, 1040) / 100
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
    else:
        if dsatz['stufe'] == 5:
            lauf = random.randint(75, 110) / 10
            sprung1 = random.randint(180, 370) / 100
            sprung2 = random.randint(180, 370) / 100
            sprung3 = random.randint(180, 370) / 100
            wurfstoss1 = random.randint(14, 54) / 2
            wurfstoss2 = random.randint(14, 54) / 2
            wurfstoss3 = random.randint(14, 54) / 2
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                       " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                       "WHERE schnr = '{}';"\
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                #print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 6:
            lauf = random.randint(73, 108) / 10
            sprung1 = random.randint(190, 380) / 100
            sprung2 = random.randint(190, 380) / 100
            sprung3 = random.randint(190, 380) / 100
            wurfstoss1 = random.randint(16, 60) / 2
            wurfstoss2 = random.randint(16, 60) / 2
            wurfstoss3 = random.randint(16, 60) / 2
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 7:
            lauf = random.randint(110, 160) / 10
            sprung1 = random.randint(210, 410) / 100
            sprung2 = random.randint(210, 410) / 100
            sprung3 = random.randint(210, 410) / 100
            wurfstoss1 = random.randint(20, 70) / 2
            wurfstoss2 = random.randint(20, 70) / 2
            wurfstoss3 = random.randint(20, 70) / 2
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 8:
            lauf = random.randint(108, 158) / 10
            sprung1 = random.randint(220, 420) / 100
            sprung2 = random.randint(220, 420) / 100
            sprung3 = random.randint(220, 420) / 100
            wurfstoss1 = random.randint(400, 770) / 100
            wurfstoss2 = random.randint(400, 770) / 100
            wurfstoss3 = random.randint(400, 770) / 100
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 9:
            lauf = random.randint(140, 200) / 10
            sprung1 = random.randint(230, 430) / 100
            sprung2 = random.randint(230, 430) / 100
            sprung3 = random.randint(230, 430) / 100
            wurfstoss1 = random.randint(450, 800) / 100
            wurfstoss2 = random.randint(450, 800) / 100
            wurfstoss3 = random.randint(450, 800) / 100
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
        elif dsatz['stufe'] == 10:
            lauf = random.randint(138, 198) / 10
            sprung1 = random.randint(240, 440) / 100
            sprung2 = random.randint(240, 440) / 100
            sprung3 = random.randint(240, 440) / 100
            wurfstoss1 = random.randint(480, 810) / 100
            wurfstoss2 = random.randint(480, 810) / 100
            wurfstoss3 = random.randint(480, 810) / 100
            try:
                connection = libs.functions.connection()
                cursor = connection.cursor()

                sql = "UPDATE Schueler SET lauf = '{}', sprung1 = '{}', sprung2 = '{}', sprung3 = '{}'," \
                      " wurfstoss1 = '{}',  wurfstoss2 = '{}',  wurfstoss3 = '{}' " \
                      "WHERE schnr = '{}';" \
                    .format(lauf, sprung1, sprung2, sprung3, wurfstoss1, wurfstoss2, wurfstoss3, dsatz['schnr'])
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                connection.close()
                print(dsatz['schnr'], "erfolgreich eingetragen!<br>")
            except:
                print("Fehler beim Eintragen von ", dsatz['schnr'])
print("</article>")
print("</section>")
print(FOOTER)