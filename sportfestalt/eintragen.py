#!/usr/bin/env python3

def createsql(klasse, sportart, geschlecht):
    sql = "SELECT schnr, nname, vname, bemerkung"
    if sportart == "Sprint":
        sql += ", lauf"
    elif sportart == "Sprung":
        sql += ", sprung1, sprung2, sprung3"
    elif sportart in ["Wurf", "Kugel"]:
        sql += ", wurfstoss1, wurfstoss2, wurfstoss3"
    sql += " FROM Schueler WHERE klasse = '{}' AND geschlecht = '{}'".format(klasse, geschlecht)
    return sql


import cgi, hashlib, libs.functions
form = cgi.FieldStorage()

from libs.config import *

login = form.getvalue('login')
password = form.getvalue('password')
klasse = form.getvalue('klasse')
sportart = form.getvalue('sportart')
geschlecht = form.getvalue('geschlecht')
test = form.getvalue('test')
if geschlecht == "M":
    ue = "Jungen"
    ge = "männlich"
elif geschlecht == "W":
    ue = "M&auml;dchen"
    ge = "weiblich"


print(HEADER)



if login in USERS.keys() and USERS[login] == password:
    if test == 'True':
        connection = libs.functions.connection()
        cursor = connection.cursor()
        sql = createsql(klasse, sportart, ge)
        cursor.execute(sql)
        daten = cursor.fetchall()
        connection.close()
        for dsatz in daten:
            # Eingetragene Daten von Sprint übernehmen
            if sportart == "Sprint":
                feld = "lauf" + str(dsatz['schnr'])
                wert = form.getvalue('{}'.format(feld))
                if wert is not None:
                    try:
                        x = float(wert)
                        connection = libs.functions.connection()
                        cursor = connection.cursor()
                        sql1 = "UPDATE Schueler SET lauf = '{}' WHERE schnr = '{}';".format(wert, dsatz['schnr'])
                        cursor.execute(sql1)
                        connection.commit()
                        connection.close()
                    except:
                        print("Fehlerhaftes Zahlformat!")
                else:
                    connection = libs.functions.connection()
                    cursor = connection.cursor()
                    sql1 = "UPDATE `Schueler` SET `lauf` = NULL WHERE `Schueler`.`schnr` = {};".format(dsatz['schnr'])
                    cursor.execute(sql1)
                    connection.commit()
                    connection.close()

            # Eingetragene Daten von Sprung übernehmen
            elif sportart == "Sprung":
                feld1 = "sprung1-" + str(dsatz['schnr'])
                wert1 = form.getvalue('{}'.format(feld1))
                if wert1 is not None:
                    try:
                        x = float(wert1)
                        connection = libs.functions.connection()
                        cursor = connection.cursor()
                        sql1 = "UPDATE Schueler SET sprung1 = '{}' WHERE schnr = '{}';".format(wert1,dsatz['schnr'])
                        cursor.execute(sql1)
                        connection.commit()
                        connection.close()
                    except:
                        print("Fehlerhaftes Zahlformat!")
                else:
                    connection = libs.functions.connection()
                    cursor = connection.cursor()
                    sql1 = "UPDATE `Schueler` SET `sprung1` = NULL WHERE `Schueler`.`schnr` = {};".format(dsatz['schnr'])
                    cursor.execute(sql1)
                    connection.commit()
                    connection.close()

                feld2 = "sprung2-" + str(dsatz['schnr'])
                wert2 = form.getvalue('{}'.format(feld2))
                if wert2 is not None:
                    try:
                        x = float(wert2)
                        connection = libs.functions.connection()
                        cursor = connection.cursor()
                        sql2 = "UPDATE Schueler SET sprung2 = '{}' WHERE schnr = '{}';".format(wert2, dsatz['schnr'])
                        cursor.execute(sql2)
                        connection.commit()
                        connection.close()
                    except:
                        print("Fehlerhaftes Zahlformat!")
                else:
                    connection = libs.functions.connection()
                    cursor = connection.cursor()
                    sql1 = "UPDATE `Schueler` SET `sprung2` = NULL WHERE `Schueler`.`schnr` = {};".format(dsatz['schnr'])
                    cursor.execute(sql1)
                    connection.commit()
                    connection.close()

                feld3 = "sprung3-" + str(dsatz['schnr'])
                wert3 = form.getvalue('{}'.format(feld3))
                if wert3 is not None:
                    try:
                        x = float(wert3)
                        connection = libs.functions.connection()
                        cursor = connection.cursor()
                        sql3 = "UPDATE Schueler SET sprung3 = '{}' WHERE schnr = '{}';".format(wert3, dsatz['schnr'])
                        cursor.execute(sql3)
                        connection.commit()
                        connection.close()
                    except:
                        print("Fehlerhaftes Zahlformat!")
                else:
                    connection = libs.functions.connection()
                    cursor = connection.cursor()
                    sql1 = "UPDATE `Schueler` SET `sprung3` = NULL WHERE `Schueler`.`schnr` = {};".format(dsatz['schnr'])
                    cursor.execute(sql1)
                    connection.commit()
                    connection.close()

            # Eingetragene Daten von Wurf und Stoß übernehmen
            elif sportart in ["Wurf", "Kugel"]:
                feld1 = "wurfstoss1-" + str(dsatz['schnr'])
                wert1 = form.getvalue('{}'.format(feld1))
                if wert1 is not None:
                    try:
                        x = float(wert1)
                        connection = libs.functions.connection()
                        cursor = connection.cursor()
                        sql1 = "UPDATE Schueler SET wurfstoss1 = '{}' WHERE schnr = '{}';".format(wert1,dsatz['schnr'])
                        cursor.execute(sql1)
                        connection.commit()
                        connection.close()
                    except:
                        print("Fehlerhaftes Zahlformat!")
                else:
                    connection = libs.functions.connection()
                    cursor = connection.cursor()
                    sql1 = "UPDATE `Schueler` SET `wurfstoss1` = NULL WHERE `Schueler`.`schnr` = {};".format(dsatz['schnr'])
                    cursor.execute(sql1)
                    connection.commit()
                    connection.close()

                feld2 = "wurfstoss2-" + str(dsatz['schnr'])
                wert2 = form.getvalue('{}'.format(feld2))
                if wert2 is not None:
                    try:
                        x = float(wert2)
                        connection = libs.functions.connection()
                        cursor = connection.cursor()
                        sql2 = "UPDATE Schueler SET wurfstoss2 = '{}' WHERE schnr = '{}';".format(wert2, dsatz['schnr'])
                        cursor.execute(sql2)
                        connection.commit()
                        connection.close()
                    except:
                        print("Fehlerhaftes Zahlformat!")
                else:
                    connection = libs.functions.connection()
                    cursor = connection.cursor()
                    sql1 = "UPDATE `Schueler` SET `wurfstoss2` = NULL WHERE `Schueler`.`schnr` = {};".format(dsatz['schnr'])
                    cursor.execute(sql1)
                    connection.commit()
                    connection.close()

                feld3 = "wurfstoss3-" + str(dsatz['schnr'])
                wert3 = form.getvalue('{}'.format(feld3))
                if wert3 is not None:
                    try:
                        x = float(wert3)
                        connection = libs.functions.connection()
                        cursor = connection.cursor()
                        sql3 = "UPDATE Schueler SET wurfstoss3 = '{}' WHERE schnr = '{}';".format(wert3, dsatz['schnr'])
                        cursor.execute(sql3)
                        connection.commit()
                        connection.close()
                    except:
                        print("Fehlerhaftes Zahlformat!")
                else:
                    connection = libs.functions.connection()
                    cursor = connection.cursor()
                    sql1 = "UPDATE `Schueler` SET `wurfstoss3` = NULL WHERE `Schueler`.`schnr` = {};".format(dsatz['schnr'])
                    cursor.execute(sql1)
                    connection.commit()
                    connection.close()

            bem = "bemerkung" + str(dsatz['schnr'])
            bewert = form.getvalue('{}'.format(bem))
            if bewert is not None:
                connection = libs.functions.connection()
                cursor = connection.cursor()
                sql3 = "UPDATE Schueler SET bemerkung = '{}' WHERE schnr = '{}';".format(bewert, dsatz['schnr'])
                cursor.execute(sql3)
                connection.commit()
                connection.close()
            else:
                connection = libs.functions.connection()
                cursor = connection.cursor()
                sql1 = "UPDATE `Schueler` SET `bemerkung` = NULL WHERE `Schueler`.`schnr` = {};".format(dsatz['schnr'])
                cursor.execute(sql1)
                connection.commit()
                connection.close()

    connection = libs.functions.connection()
    cursor = connection.cursor()
    sql = createsql(klasse, sportart, ge)
    cursor.execute(sql)
    connection.close()

    print("         <section>")
    print("             <article>")
    print("             <h1>Ergebnisse eintragen: Klasse: {} - Sportart: {} - Geschlecht: {}</h1>".format(klasse, sportart, ue))
    print("             <p>Bei Bemerkung K für krank, E für entschuldigt bzw. A für Attest eintragen!</p>".translate(HTML))
    print("             <p>Bei ungültigen Versuchen das jeweilige Feld bitte leer lassen!</p>".translate(HTML))
    print("             <form action='http://sportfestserver/cgi-bin/eintragen.py' method='post'>")
    print("             <input type='hidden' name = 'login' value = '{}' >".format(login))
    print("             <input type='hidden' name = 'password' value = '{}' >".format(password))
    print("             <input type='hidden' name = 'klasse' value = '{}' >".format(klasse))
    print("             <input type='hidden' name = 'sportart' value = '{}' >".format(sportart))
    print("             <input type='hidden' name = 'geschlecht' value = '{}' >".format(geschlecht))
    print("             <input type='hidden' name = 'test' value = 'True' >")
    print("             <table border='1' width='95%'>")
    # Erzeugen der Sprinttabelle
    if sportart == "Sprint":
        print("                 <tr><th align='left'>Name</th>"
              "<th align='left'>Vorname</th>"
              "<th align='left'>Zeit</th>"
              "<th align='left'>Bemerkung</th></tr>")
        for dsatz in cursor:
            zeile = "                     <tr><td>{}</td><td>{}</td>".format(dsatz['nname'],dsatz['vname'])
            if dsatz['lauf'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='30' step='0.1' minsize='1'> </td>"\
                    .format("lauf"+str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='30' step='0.1' value='{}' size='1'> </td>"\
                    .format("lauf" + str(dsatz['schnr']), dsatz['lauf'] )
            if dsatz['bemerkung'] is None:
                zeile += "<td><input name='{}' size='1'> </td></tr>"\
                    .format("bemerkung"+str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' size='1' value='{}'> </td></tr>"\
                    .format("bemerkung" + str(dsatz['schnr']), dsatz['bemerkung'] )
            print(zeile.translate(HTML))
    # Erzeugen der Weitsprungtabelle
    elif sportart == "Sprung":
        print("                 <tr><th align='left'>Name</th>"
              "<th align='left'>Vorname</th>"
              "<th align='left'>Versuch 1</th>"
              "<th align='left'>Versuch 2</th>"
              "<th align='left'>Versuch 3</th>"
              "<th align='left'>Bemerkung</th></tr></tr>")
        for dsatz in cursor:
            zeile = "                     <tr><td>{}</td><td>{}</td>".format(dsatz['nname'],dsatz['vname'])
            if dsatz['sprung1'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='8' step='0.01'> </td>"\
                    .format("sprung1-"+str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='8' step='0.01' value='{}' size='1'> </td>"\
                    .format("sprung1-" + str(dsatz['schnr']), dsatz['sprung1'])
            if dsatz['sprung2'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='8' step='0.01'> </td>"\
                    .format("sprung2-"+str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='8' step='0.01' value='{}' size='1'> </td>"\
                    .format("sprung2-" + str(dsatz['schnr']), dsatz['sprung2'])
            if dsatz['sprung3'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='8' step='0.01'> </td>"\
                    .format("sprung3-"+str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='8' step='0.01' value='{}' size='1'> </td>"\
                    .format("sprung3-" + str(dsatz['schnr']), dsatz['sprung3'])
            if dsatz['bemerkung'] is None:
                zeile += "<td><input name='{}' size='1'> </td></tr>"\
                    .format("bemerkung"+str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' size='1' value='{}'> </td></tr>"\
                    .format("bemerkung" + str(dsatz['schnr']), dsatz['bemerkung'] )
            print(zeile.translate(HTML))
    # Erzeugen der Wurftabelle
    elif sportart == "Wurf":
        print("                 <tr><th align='left'>Name</th>"
              "<th align='left'>Vorname</th>"
              "<th align='left'>Versuch 1</th>"
              "<th align='left'>Versuch 2</th>"
              "<th align='left'>Versuch 3</th>"
              "<th align='left'>Bemerkung</th></tr></tr>")
        for dsatz in cursor:
            zeile = "                     <tr><td>{}</td><td>{}</td>".format(dsatz['nname'], dsatz['vname'])
            if dsatz['wurfstoss1'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='100' step='0.5'> </td>" \
                    .format("wurfstoss1-" + str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='100' step='0.5' value='{}' size='1'> </td>" \
                    .format("wurfstoss1-" + str(dsatz['schnr']), dsatz['wurfstoss1'])
            if dsatz['wurfstoss2'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='100' step='0.5'> </td>" \
                    .format("wurfstoss2-" + str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='100' step='0.5' value='{}' size='1'> </td>" \
                    .format("wurfstoss2-" + str(dsatz['schnr']), dsatz['wurfstoss2'])
            if dsatz['wurfstoss3'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='100' step='0.5'> </td>" \
                    .format("wurfstoss3-" + str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='100' step='0.5' value='{}' size='1'> </td>" \
                    .format("wurfstoss3-" + str(dsatz['schnr']), dsatz['wurfstoss3'])
            if dsatz['bemerkung'] is None:
                zeile += "<td><input name='{}' size='1'> </td></tr>"\
                    .format("bemerkung"+str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' size='1' value='{}'> </td></tr>"\
                    .format("bemerkung" + str(dsatz['schnr']), dsatz['bemerkung'] )
            print(zeile.translate(HTML))
    # Erzeugen der Stosstabelle
    elif sportart == "Kugel":
        print("                 <tr><th align='left'>Name</th>"
              "<th align='left'>Vorname</th>"
              "<th align='left'>Versuch 1</th>"
              "<th align='left'>Versuch 2</th>"
              "<th align='left'>Versuch 3</th>"
              "<th align='left'>Bemerkung</th></tr></tr>")
        for dsatz in cursor:
            zeile = "                     <tr><td>{}</td><td>{}</td>".format(dsatz['nname'], dsatz['vname'])
            if dsatz['wurfstoss1'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='20' step='0.01'> </td>" \
                    .format("wurfstoss1-" + str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='20' step='0.01' value='{}' size='1'> </td>" \
                    .format("wurfstoss1-" + str(dsatz['schnr']), dsatz['wurfstoss1'])
            if dsatz['wurfstoss2'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='20' step='0.01'> </td>" \
                    .format("wurfstoss2-" + str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='20' step='0.01' value='{}' size='1'> </td>" \
                    .format("wurfstoss2-" + str(dsatz['schnr']), dsatz['wurfstoss2'])
            if dsatz['wurfstoss3'] is None:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='20' step='0.01'> </td>" \
                    .format("wurfstoss3-" + str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' type='number' lang='en' min='0' max='20' step='0.01' value='{}' size='1'> </td>" \
                    .format("wurfstoss3-" + str(dsatz['schnr']), dsatz['wurfstoss3'])
            if dsatz['bemerkung'] is None:
                zeile += "<td><input name='{}' size='1'> </td></tr>"\
                    .format("bemerkung"+str(dsatz['schnr']))
            else:
                zeile += "<td><input name='{}' size='1' value='{}'> </td></tr>"\
                    .format("bemerkung" + str(dsatz['schnr']), dsatz['bemerkung'] )

            print(zeile.translate(HTML))

    print("             </table>")
    print("             <p align='center'><button> Daten eintragen! </button></p>")
    print("             </form>")
    print("             <form action='http://sportfestserver/cgi-bin/sportfest.py' method='post'>")
    print("             <input type='hidden' name = 'login' value = {} >".format(login))
    print("             <input type='hidden' name = 'password' value = {} >".format(password))
    print("             <p align='center'><button> Zurück zur Hauptseite! </button></p>".translate(HTML))
    print("             </form>")
    print("             </article>")
    print("         </section>")
else:
    print(LOGINFEHLER)


print(FOOTER)