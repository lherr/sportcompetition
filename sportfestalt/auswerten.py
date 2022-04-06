#!/usr/bin/env python3

import cgi, hashlib, libs.functions, os, time
form = cgi.FieldStorage()

from libs.config import *
from libs.schueler import *

# Formulardaten abfragen
login = form.getvalue('login')
password = form.getvalue('password')
jgstufe = form.getvalue('jgstufe')
art = form.getvalue('art')
geschlecht = form.getvalue('geschlecht')
if geschlecht == "M":
    ue = "Jungen"
    ge = "männlich"
elif geschlecht == "W":
    ue = "Mädchen"
    ge = "weiblich"

print(HEADER)

if login in ["admin", "sportlehrer"] and USERS[login] == password:


    print("<section>")
    print("<article>")
    print("<h1>Auswertung - {} - {}</h1>".format(jgstufe, ue).translate(HTML))
    lt = time.localtime()
    jahr, monat, tag = lt[0:3]
    stunde, minute, sekunde = lt[3:6]
    print("<p align='center'>{0:02d}.{1:02d}.{2:4d} - {3:02d}:{4:02d}:{5:02d}</p>".
          format(tag, monat, jahr, stunde, minute, sekunde))

    # Connect to the database
    if art == 'G':
        try:
            ergebnisliste = open("daten/Latex/ergebnisse.tex", "w")
            ergebnisliste.write(LATEXHEADER)
        except:
            print("Fehler beim Öffnen der Datei!".translate(HTML))
        ergebnisliste.write("\\subsection*{Auswertung - " + str(jgstufe) + " - " + str(ue).translate(LATEX) + "}\n")
        ergebnisliste.write("\\begin{footnotesize}\n")
        ergebnisliste.write("\\begin{tabular}{|p{2.5cm}|p{2.5cm}|p{0.8cm}|p{0.8cm}|p{0.8cm}|p{0.8cm}|p{0.8cm}|"
                            "p{0.8cm}|p{0.8cm}|p{0.8cm}|p{0.8cm}|}\n\\hline ")
        print("<table border='1' width='95%'>")
        tabellenkopf = "<tr><th align='left'>Name</th>"
        tabellenkopf += "<th align='left'>Vorname</th>"
        tabellenkopf += "<th align='left'>Sprint</th>"
        tabellenkopf += "<th align='left'>Punkte</th>"
        tabellenkopf += "<th align='left'>Sprung</th>"
        tabellenkopf += "<th align='left'>Punkte</th>"
        ergebnisliste.write("Name & Vorname & Sprint & Pkt. & Sprung &")
        if jgstufe in ["Klasse 5", "Klasse 6", "Klasse 7"]:
            tabellenkopf += "<th align='left'>Wurf</th>"
            tabellenkopf += "<th align='left'>Punkte</th>"
            ergebnisliste.write(" Pkt. & Wurf & Pkt. & ")
        else:
            tabellenkopf += "<th align='left'>Stoß</th>".translate(HTML)
            tabellenkopf += "<th align='left'>Punkte</th>"
            ergebnisliste.write(" Pkt. & Stoß & Pkt. & ".translate(LATEX))
        tabellenkopf += "<th align='left'>Mehrkampf</th>"
        tabellenkopf += "<th align='left'>Platz</th>"
        tabellenkopf += "<th align='left'>Bemerkung</th></tr>"
        ergebnisliste.write("Mehrk. & Platz & Bem. \\\\ \n \\hline \n")
        print(tabellenkopf)
        sieger = []
        try:
            connection = libs.functions.connection()
            cursor = connection.cursor()
            if jgstufe == "Klasse 5":
                sql = "SELECT * FROM Schueler WHERE stufe = '5' AND geschlecht = '{}' ORDER BY punktemehrkampf DESC;".format(ge)
            elif jgstufe == "Klasse 6":
                sql = "SELECT * FROM Schueler WHERE stufe = '6' AND geschlecht = '{}' ORDER BY punktemehrkampf DESC;".format(ge)
            elif jgstufe == "Klasse 7":
                sql = "SELECT * FROM Schueler WHERE stufe = '7' AND geschlecht = '{}' ORDER BY punktemehrkampf DESC;".format(ge)
            elif jgstufe == "Klasse 8":
                sql = "SELECT * FROM Schueler WHERE stufe = '8' AND geschlecht = '{}' ORDER BY punktemehrkampf DESC;".format(ge)
            elif jgstufe == "Klasse 9":
                sql = "SELECT * FROM Schueler WHERE stufe = '9' AND geschlecht = '{}' ORDER BY punktemehrkampf DESC;".format(ge)
            elif jgstufe == "Klasse 10":
                sql = "SELECT * FROM Schueler WHERE stufe = '10' AND geschlecht = '{}' ORDER BY punktemehrkampf DESC;".format(ge)
            cursor.execute(sql)
            daten = cursor.fetchall()
            connection.close()
            print("<p>Daten erfolgreich aus der Datenbank gelesen!</p>")
        except:
            print("<p>Fehler beim Einlesen der Daten aus der Datenbank</p>")

        platz = 0
        nummer = 0
        lastmehrkampf = -1
        for dsatz in daten:
            nummer += 1
            if dsatz['punktemehrkampf'] is not None:
                if int(dsatz['punktemehrkampf']) != lastmehrkampf:
                    platz = nummer
                lastmehrkampf = int(dsatz['punktemehrkampf'])
            else:
                platz ="-"

            zeile = "<tr>"
            zeile += "<td>"+str(dsatz['nname']).translate(HTML)+"</td>"
            ergebnisliste.write(str(dsatz['nname'].translate(LATEX))+" & ")
            zeile += "<td>" + str(dsatz['vname']).translate(HTML) + "</td>"
            ergebnisliste.write(str(dsatz['vname'].translate(LATEX)) + " & ")
            if dsatz['lauf'] is None:
                zeile += "<td></td>"
                ergebnisliste.write(" & ")
            else:
                zeile += "<td>" + str(dsatz['lauf']) + "</td>"
                ergebnisliste.write(str(dsatz['lauf']) + " & ")
            if dsatz['punktelauf'] is None:
                zeile += "<td></td>"
                ergebnisliste.write(" & ")
            else:
                zeile += "<td>" + str(dsatz['punktelauf']) + "</td>"
                ergebnisliste.write(str(dsatz['punktelauf']) + " & ")
            if dsatz['bestsprung'] is None:
                zeile += "<td></td>"
                ergebnisliste.write(" & ")
            else:
                zeile += "<td>" + str(dsatz['bestsprung']) + "</td>"
                ergebnisliste.write(str(dsatz['bestsprung']) + " & ")
            if dsatz['punktesprung'] is None:
                zeile += "<td></td>"
                ergebnisliste.write(" & ")
            else:
                zeile += "<td>" + str(dsatz['punktesprung']) + "</td>"
                ergebnisliste.write(str(dsatz['punktesprung']) + " & ")
            if dsatz['bestwurfstoss'] is None:
                zeile += "<td></td>"
                ergebnisliste.write(" & ")
            else:
                zeile += "<td>" + str(dsatz['bestwurfstoss']) + "</td>"
                ergebnisliste.write(str(dsatz['bestwurfstoss']) + " & ")
            if dsatz['punktewurfstoss'] is None:
                zeile += "<td></td>"
                ergebnisliste.write(" & ")
            else:
                zeile += "<td>" + str(dsatz['punktewurfstoss']) + "</td>"
                ergebnisliste.write(str(dsatz['punktewurfstoss']) + " & ")
            if dsatz['punktemehrkampf'] is None:
                zeile += "<td></td>"
                ergebnisliste.write(" & ")
            else:
                zeile += "<td>" + str(dsatz['punktemehrkampf']) + "</td>"
                ergebnisliste.write(str(dsatz['punktemehrkampf']) + " & ")
            zeile += "<td> {} </td>".format(platz)
            ergebnisliste.write(str(platz) + " & ")
            if dsatz['bemerkung'] is None:
                zeile += "<td></td></tr>"
                ergebnisliste.write(" \\\\ \n \hline \n")
            else:
                zeile += "<td>" + str(dsatz['bemerkung']) + "</td></tr>"
                ergebnisliste.write(str(dsatz['bemerkung']) + " \\\\ \n \hline \n")
            print(zeile)
            if platz in [1, 2, 3]:
                sieger.append([str(dsatz['vname'].translate(LATEX)),str(dsatz['nname'].translate(LATEX)),\
                               str(dsatz['punktemehrkampf']), dsatz['klasse'], str(dsatz['stufe']), str(platz)])
        print("</table>")
        ergebnisliste.write("\\end{tabular} ")
        ergebnisliste.write("\n \n \\medskip \n \n")
        uhrzeit = "{0:02d}.{1:02d}.{2:4d} - {3:02d}:{4:02d}:{5:02d}".format(tag, monat, jahr, stunde, minute, sekunde)
        ergebnisliste.write(uhrzeit)
        ergebnisliste.write("\n \\end{footnotesize} \n")
        ergebnisliste.write(LATEXFOOTER)
        ergebnisliste.close()
        os.system("cd daten/ && cd Latex/ && pdflatex ergebnisse.tex >> tex.log && cd .. && cd ..")
        os.system("cp daten/Latex/ergebnisse.pdf /var/www/html/downloads/ergebnisse.pdf")
        try:
            urkunde = open("daten/Latex/urkunde.tex", "w")
            urkunde.write(URKUNDENHEADER)
        except:
            print("Fehler beim Öffnen der Datei!".translate(HTML))
        for wert in sieger:
            urkunde.write(URKUNDE1)
            urkunde.write("{\\huge " + wert[0] + " " + wert[1]+ "} \n \n \\vspace*{1cm}")
            urkunde.write("{\\LARGE Klasse " + wert[3] + "} \n \n \\vspace*{1 cm} \n ")
            urkunde.write("\n{\Large belegte beim} \n \n \\vspace*{1,5 cm}")
            urkunde.write("{\\Huge Leichtathletik-Sportfest "+ str(jahr) +"} \n \n \\vspace*{1 cm}")
            urkunde.write("{\\Large in der Klassenstufe "+ wert[4] + " " + ge.translate(LATEX) +"} ")
            urkunde.write("\n \n \\bigskip \n {\\LARGE im Dreikampf} \n \n \\bigskip \n")
            if wert[4] in ['5','6','7']:
                urkunde.write("\n {\\LARGE Sprint - Wurf - Weit} \n \n")
            else:
                urkunde.write("\n {\\LARGE Sprint - Kugel - Weit} \n \n")
            urkunde.write("\\bigskip \n \n {\Large mit "+ wert[2] +" Punkte den} \n \n \\vspace*{1 cm} \n \n")
            urkunde.write("{\\fontseries{b} \n \\fontsize{40}{50} \n \\selectfont \n "+wert[5]+". Platz}")
            urkunde.write(URKUNDE2)
            datum = "{0:02d}.{1:02d}.{2:4d}".format(tag, monat, jahr)
            urkunde.write("{\\large Glauchau, "+datum+"}")
            urkunde.write(URKUNDE3)
            urkunde.write("\\pagebreak")
        urkunde.write("\\end{document}")
        urkunde.close()
        os.system("cd daten/ && cd Latex/ && pdflatex urkunde.tex >> urkundetex.log && cd .. && cd ..")
        os.system("cp daten/Latex/urkunde.pdf /var/www/html/downloads/urkunde.pdf")
        print("""
                    <ul>
                        <li><a href='http://sportfestserver/downloads/ergebnisse.pdf'><strong>Download der Liste als PDF</strong>
                        </a></li>
                        <li><a href='http://sportfestserver/downloads/urkunde.pdf'><strong>Download der Urkunden als PDF</strong>
                        </a></li>
                    </ul>
                    """)
    elif art == "K":
        try:
            ergebnisliste = open("daten/Latex/ergebnisse.tex", "w")
            ergebnisliste.write(LATEXHEADER)
        except:
            print("Fehler beim Öffnen der Datei!".translate(HTML))
        ergebnisliste.write("\\subsection*{Auswertung - " + str(jgstufe) + " - " + str(ue).translate(LATEX) + "}\n")
        ergebnisliste.write("\\begin{footnotesize}\n")
        try:
            connection = libs.functions.connection()
            cursor = connection.cursor()
            if jgstufe == "Klasse 5":
                sql = "SELECT * FROM Schueler WHERE stufe = '5' AND geschlecht = '{}' ORDER BY nname, vname;".format(ge)
            elif jgstufe == "Klasse 6":
                sql = "SELECT * FROM Schueler WHERE stufe = '6' AND geschlecht = '{}' ORDER BY nname, vname;".format(ge)
            elif jgstufe == "Klasse 7":
                sql = "SELECT * FROM Schueler WHERE stufe = '7' AND geschlecht = '{}' ORDER BY nname, vname;".format(ge)
            elif jgstufe == "Klasse 8":
                sql = "SELECT * FROM Schueler WHERE stufe = '8' AND geschlecht = '{}' ORDER BY nname, vname;".format(ge)
            elif jgstufe == "Klasse 9":
                sql = "SELECT * FROM Schueler WHERE stufe = '9' AND geschlecht = '{}' ORDER BY nname, vname;".format(ge)
            elif jgstufe == "Klasse 10":
                sql = "SELECT * FROM Schueler WHERE stufe = '10' AND geschlecht = '{}' ORDER BY nname, vname;".format(ge)
            cursor.execute(sql)
            daten = cursor.fetchall()
            connection.close()
            #print("<p>Daten erfolgreich aus der Datenbank gelesen!</p>")
        except:
            print("<p>Fehler beim Einlesen der Daten aus der Datenbank</p>")
        klassen = []
        for dsatz in daten:
            if dsatz['klasse'] not in klassen:
                klassen.append(dsatz['klasse'])

        klassen.sort()

        for klasse in klassen:
            print("<p><strong><i>Klasse",klasse,"</i></strong></p>")
            print("<table border='1' width='95%'>")
            ergebnisliste.write("\\subsubsection*{Klasse " + klasse + "} \n \n \\bigskip")
            ergebnisliste.write("\\begin{tabular}{|p{2.5cm}|p{2.5cm}|p{0.8cm}|p{0.8cm}|p{0.8cm}|p{0.8cm}|p{0.8cm}|"
                                "p{0.8cm}|p{2cm}|}\n\\hline ")
            tabellenkopf = "<tr><th align='left'>Name</th>"
            tabellenkopf += "<th align='left'>Vorname</th>"
            tabellenkopf += "<th align='left'>Sprint</th>"
            tabellenkopf += "<th align='left'>Note</th>"
            tabellenkopf += "<th align='left'>Sprung</th>"
            tabellenkopf += "<th align='left'>Note</th>"
            ergebnisliste.write("Name & Vorname & Sprint & Note & Sprung &")
            if jgstufe in ["Klasse 5", "Klasse 6", "Klasse 7"]:
                tabellenkopf += "<th align='left'>Wurf</th>"
                tabellenkopf += "<th align='left'>Note</th>"
                ergebnisliste.write(" Note & Wurf & Note & ")
            else:
                tabellenkopf += "<th align='left'>Stoss</th>"
                tabellenkopf += "<th align='left'>Note</th>"
                ergebnisliste.write(" Note & Stoß & Note & ".translate(LATEX))
            ergebnisliste.write(" Bemerkung \\\\ \n \\hline \n")
            tabellenkopf += "<th align='left'>Bemerkung</th></tr>"
            print(tabellenkopf)
            for dsatz in daten:
                if dsatz['klasse'] == klasse:
                    zeile = "<tr>"
                    zeile += "<td>"+str(dsatz['nname']).translate(HTML)+"</td>"
                    ergebnisliste.write(str(dsatz['nname'].translate(LATEX)) + " & ")
                    zeile += "<td>" + str(dsatz['vname']).translate(HTML) + "</td>"
                    ergebnisliste.write(str(dsatz['vname'].translate(LATEX)) + " & ")
                    if dsatz['lauf'] is None:
                        zeile += "<td></td>"
                        ergebnisliste.write(" & ")
                    else:
                        zeile += "<td>" + str(dsatz['lauf']) + "</td>"
                        ergebnisliste.write(str(dsatz['lauf']) + " & ")
                    if dsatz['notelauf'] is None:
                        zeile += "<td></td>"
                        ergebnisliste.write(" & ")
                    else:
                        zeile += "<td>" + str(dsatz['notelauf']) + "</td>"
                        ergebnisliste.write(str(dsatz['notelauf']) + " & ")
                    if dsatz['bestsprung'] is None:
                        zeile += "<td></td>"
                        ergebnisliste.write(" & ")
                    else:
                        zeile += "<td>" + str(dsatz['bestsprung']) + "</td>"
                        ergebnisliste.write(str(dsatz['bestsprung']) + " & ")
                    if dsatz['notesprung'] is None:
                        zeile += "<td></td>"
                        ergebnisliste.write(" & ")
                    else:
                        zeile += "<td>" + str(dsatz['notesprung']) + "</td>"
                        ergebnisliste.write(str(dsatz['notesprung']) + " & ")
                    if dsatz['bestwurfstoss'] is None:
                        zeile += "<td></td>"
                        ergebnisliste.write(" & ")
                    else:
                        zeile += "<td>" + str(dsatz['bestwurfstoss']) + "</td>"
                        ergebnisliste.write(str(dsatz['bestwurfstoss']) + " & ")
                    if dsatz['notewurfstoss'] is None:
                        zeile += "<td></td>"
                        ergebnisliste.write(" & ")
                    else:
                        zeile += "<td>" + str(dsatz['notewurfstoss']) + "</td>"
                        ergebnisliste.write(str(dsatz['notewurfstoss']) + " & ")
                    if dsatz['bemerkung'] is None:
                        zeile += "<td></td></tr>"
                        ergebnisliste.write(" \\\\ \n \hline \n")
                    else:
                        zeile += "<td>" + str(dsatz['bemerkung']) + "</td></tr>"
                        ergebnisliste.write(str(dsatz['bemerkung']) + " \\\\ \n \hline \n")
                    print(zeile)
            print("</table>")
            ergebnisliste.write("\\end{tabular} \n \n \\bigskip")
        ergebnisliste.write("\n \n \\medskip \n \n")
        uhrzeit = "{0:02d}.{1:02d}.{2:4d} - {3:02d}:{4:02d}:{5:02d}".format(tag, monat, jahr, stunde, minute,
                                                                            sekunde)
        ergebnisliste.write(uhrzeit)
        ergebnisliste.write("\n \\end{footnotesize} \n")
        ergebnisliste.write(LATEXFOOTER)
        ergebnisliste.close()
        os.system("cd daten/ && cd Latex/ && pdflatex ergebnisse.tex >> tex.log && cd .. && cd ..")
        os.system("cp daten/Latex/ergebnisse.pdf /var/www/html/downloads/ergebnisse.pdf")
        print("""
                            <ul>
                                <li><a href='http://sportfestserver/downloads/ergebnisse.pdf'><strong>Download der Liste als PDF</strong>
                                </a></li>
                            </ul>
                            """)

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