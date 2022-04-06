#!/usr/bin/env python3

import libs.functions


try:
    daten = open('daten/sportfest.csv','r')
    datenliste = daten.readlines()
    daten.close()
except:
    print('Datei lässt sich nicht öffnen!')

for i in range(len(datenliste)):
    datenliste[i] = datenliste[i].rstrip('\n')
    datenliste[i] = datenliste[i].split(',')

# Connect to the database
connection = libs.functions.connection()

try:
    with connection.cursor() as cursor:
        sql = "TRUNCATE `Schueler`;"
        cursor.execute(sql)
        connection.commit()
    for wert in datenliste:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `Schueler` (`vname`, `nname`, `geschlecht`, `klasse`, `stufe`) " \
                  "VALUES ('"+wert[0]+"', '"+wert[1]+"', '"+wert[2]+"', '"+wert[3]+"', '"+wert[4]+"');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
    connection.commit()
    print("Daten erfolgreich eingelesen!")
except:
    print("Fehler beim Einlesen der Daten!")
finally:
    connection.close()
