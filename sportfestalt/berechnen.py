#!/usr/bin/env python3

import cgi, hashlib, libs.functions
form = cgi.FieldStorage()

from libs.config import *
from libs.schueler import *

# Formulardaten abfragen
login = form.getvalue('login')
password = form.getvalue('password')
jgstufe = form.getvalue('jgstufe')

print(HEADER)

if login in ["admin", "sportlehrer"] and USERS[login] == password:

    print("<section>")
    print("<article>")
    # Connect to the database
    try:
        connection = libs.functions.connection()
        cursor = connection.cursor()
        if jgstufe == "Alle":
            sql = "SELECT * FROM Schueler;"
        elif jgstufe == "Klasse 5":
            sql = "SELECT * FROM Schueler WHERE stufe = '5';"
        elif jgstufe == "Klasse 6":
            sql = "SELECT * FROM Schueler WHERE stufe = '6';"
        elif jgstufe == "Klasse 7":
            sql = "SELECT * FROM Schueler WHERE stufe = '7';"
        elif jgstufe == "Klasse 8":
            sql = "SELECT * FROM Schueler WHERE stufe = '8';"
        elif jgstufe == "Klasse 9":
            sql = "SELECT * FROM Schueler WHERE stufe = '9';"
        elif jgstufe == "Klasse 10":
            sql = "SELECT * FROM Schueler WHERE stufe = '10';"
        cursor.execute(sql)
        daten = cursor.fetchall()
        connection.close()
        print("<p>Daten erfolgreich aus der Datenbank gelesen!</p>")
    except:
        print("<p>Fehler beim Einlesen der Daten aus der Datenbank</p>")
    for dsatz in daten:
        #print(str(dsatz).translate(HTML))
        try:
            schueler = Schueler(int(dsatz['schnr']),dsatz['nname'],dsatz['vname'],dsatz['klasse'],int(dsatz['stufe']),
                                dsatz['geschlecht'])
            if dsatz['lauf'] is None:
                lauf = None
            else:
                lauf = float(dsatz['lauf'])
            schueler.setLauf(lauf)
            if dsatz['sprung1'] is None:
                sprung1 = None
            else:
                sprung1 = float(dsatz['sprung1'])
            if dsatz['sprung2'] is None:
                sprung2 = None
            else:
                sprung2 = float(dsatz['sprung2'])
            if dsatz['sprung3'] is None:
                sprung3 = None
            else:
                sprung3 = float(dsatz['sprung3'])
            schueler.setSprung(sprung1, sprung2, sprung3)
            if dsatz['wurfstoss1'] is None:
                wurfstoss1 = None
            else:
                wurfstoss1 = float(dsatz['wurfstoss1'])
            if dsatz['wurfstoss2'] is None:
                wurfstoss2 = None
            else:
                wurfstoss2 = float(dsatz['wurfstoss2'])
            if dsatz['wurfstoss3'] is None:
                wurfstoss3 = None
            else:
                wurfstoss3 = float(dsatz['wurfstoss3'])
            schueler.setWurfstoss(wurfstoss1, wurfstoss2, wurfstoss3)
            schueler.setAll()
            # print("Lauf - Zeit:", schueler.getLauf(), "Punkte:", schueler.getPunktelauf(), "Note:",
            #       schueler.getNotelauf())
            # print("Sprung: - Weite:", schueler.getBestsprung(), "Punkte:", schueler.getPunktesprung(), "Note:",
            #       schueler.getNotesprung())
            # print("Wurfstoss: - Weite:", schueler.getBestwurfstoss(), "Punkte:", schueler.getPunktewurfstoss(), "Note:",
            #       schueler.getNotewurfstoss())
            # print("Mehrkampf:", schueler.getPunktemehrkampf())
            # print("<p>",str(dsatz['vname']).translate(HTML), str(dsatz['nname']).translate(HTML),
            #      dsatz['klasse'], "erfolgreich berechnet und eingetragen!","<p>")
            sql = "UPDATE Schueler SET "
            if schueler.getPunktelauf() is None:
                sql += "punktelauf = NULL, "
            else:
                sql += "punktelauf = '"+str(schueler.getPunktelauf())+"', "
            if schueler.getNotelauf() is None:
                sql += "notelauf = NULL, "
            else:
                sql += "notelauf = '"+str(schueler.getNotelauf())+"', "
            if schueler.getBestsprung() is None:
                sql += "bestsprung = NULL, "
            else:
                sql += "bestsprung = '"+str(schueler.getBestsprung())+"', "
            if schueler.getPunktesprung() is None:
                sql += "punktesprung = NULL, "
            else:
                sql += "punktesprung = '"+str(schueler.getPunktesprung())+"', "
            if schueler.getNotesprung() is None:
                sql += "notesprung = NULL, "
            else:
                sql += "notesprung = '"+str(schueler.getNotesprung())+"', "
            if schueler.getBestwurfstoss() is None:
                sql += "bestwurfstoss = NULL, "
            else:
                sql += "bestwurfstoss = '"+str(schueler.getBestwurfstoss())+"', "
            if schueler.getPunktewurfstoss() is None:
                sql += "punktewurfstoss = NULL, "
            else:
                sql += "punktewurfstoss = '"+str(schueler.getPunktewurfstoss())+"', "
            if schueler.getNotewurfstoss() is None:
                sql += "notewurfstoss = NULL, "
            else:
                sql += "notewurfstoss = '"+str(schueler.getNotewurfstoss())+"', "
            if schueler.getPunktemehrkampf() is None:
                sql += "punktemehrkampf = NULL "
            else:
                sql += "punktemehrkampf = '"+str(schueler.getPunktemehrkampf())+"' "
            sql += "WHERE schnr = '"+str(schueler.getSchnr())+"';"
            connection = libs.functions.connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            connection.close()
            print("<p>",str(dsatz['vname']).translate(HTML), str(dsatz['nname']).translate(HTML),
                 dsatz['klasse'], "erfolgreich berechnet und eingetragen!","<p>")
        except:
            print("<p style='color: red;'>","Fehler beim Berechnen und Eintragen des Schülers",
                  str(dsatz['vname']).translate(HTML),str(dsatz['nname']).translate(HTML),dsatz['klasse'],"</p>")
    print("             <form action='http://sportfestserver/cgi-bin/sportfest.py' method='post'>")
    print("             <input type='hidden' name = 'login' value = {} >".format(login))
    print("             <input type='hidden' name = 'password' value = {} >".format(password))
    print("             <p align='center'><button> Zurück zur Hauptseite! </button></p>".translate(HTML))
    print("             </form>")
    print("</article>")
    print("</section>")
else:
    print(LOGINFEHLER)


print(FOOTER)