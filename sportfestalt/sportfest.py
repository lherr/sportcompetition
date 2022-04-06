#!/usr/bin/env python3

import cgi, hashlib, libs.functions
form = cgi.FieldStorage()

from libs.config import *

# Logindaten abfragen
login = form.getvalue('login')
password = form.getvalue('password')
if password is None:
    password = hashlib.md5(str(form.getvalue('pass')).encode('utf-8')).hexdigest()




print(HEADER)

if login in USERS.keys() and USERS[login] == password:
    # Connect to the database
    connection = libs.functions.connection()
    cursor = connection.cursor()
    sql = "SELECT DISTINCT klasse, stufe FROM Schueler"
    cursor.execute(sql)
    connection.close()

    if login in ["admin","sportlehrer"]:
        print("         <section>")
        print("             <article>")
        print("             <h1>Ergebnisse eintragen</h1>")
        print("             <p>Wählen Sie Klasse, Sportart und Geschlecht aus!</p>".translate(HTML))
        print("             <form action='http://sportfestserver/cgi-bin/eintragen.py' method='post'>")
        print("             <input type='hidden' name = 'login' value = {} >".format(login))
        print("             <input type='hidden' name = 'password' value = {} >".format(password))
        print("""           <p>
                                <label for='klasse'>Klasse: </label>
                                <select name='klasse'> 
                                    <option>Klassen</option>""")
        for dsatz in cursor:
            print("                     <option>", dsatz['klasse'], "</option>")
        print("""				</select>
                            </p>
                            <p>
                                <label for='sportart'>Sportart: </label>
                                <select name='sportart'> 
                                    <option>Sportarten</option>
                                    <option>Sprint</option>
                                    <option>Sprung</option>
                                    <option>Wurf</option>
                                    <option>Kugel</option>
                                </select>
                            </p>
                            <p>
                                <label for='ju'>Jungen: </label>
                                <input type='radio' id='ju' name='geschlecht' value='M' checked>  
                                <label for='mae'>M&auml;dchen: </label>
                                <input type='radio' id='mae' name='geschlecht' value='W'>  
                            </p>
                            <p>
                                <button>absenden</button>
                            </p>
        """)
        print("             </form>")
        print("             <br>")
        print("             </article>")
        print("             <article>")
        print("             <h1>Auswertung</h1>")
        print("             <form action='http://sportfestserver/cgi-bin/berechnen.py' method='post'>")
        print("             <input type='hidden' name = 'login' value = {} >".format(login))
        print("             <input type='hidden' name = 'password' value = {} >".format(password))
        print("             <p><strong><i>Ergebnisse berechnen</i></strong></p>".translate(HTML))
        print("""               <p>
                                <label for='jgstufe'>Bitte auswählen: </label>
                                <select name='jgstufe'> 
                                    <option>Alle</option>
                                    <option>Klasse 5</option>
                                    <option>Klasse 6</option>
                                    <option>Klasse 7</option>
                                    <option>Klasse 8</option>
                                    <option>Klasse 9</option>
                                    <option>Klasse 10</option>
                                </select>
                                </p>
        """.translate(HTML))
        print("             <p><button> Berechnen! </button></p>")
        print("             </form>")
        print("             <form action='http://sportfestserver/cgi-bin/auswerten.py' method='post'>")
        print("             <input type='hidden' name = 'login' value = {} >".format(login))
        print("             <input type='hidden' name = 'password' value = {} >".format(password))
        print("             <p><strong><i>Auswertung anzeigen</i></strong></p>".translate(HTML))
        print("""               <p>
                                        <label for='jgstufe'>Bitte auswählen: </label>
                                        <select name='jgstufe'> 
                                            <option>Klasse 5</option>
                                            <option>Klasse 6</option>
                                            <option>Klasse 7</option>
                                            <option>Klasse 8</option>
                                            <option>Klasse 9</option>
                                            <option>Klasse 10</option>
                                        </select>
                                </p>
                                <p>
                                <label for='ge'>Gesamt: </label>
                                <input type='radio' id='ge' name='art' value='G' checked>  
                                <label for='mae'>Klassenweise: </label>
                                <input type='radio' id='kl' name='art' value='K'>  
                                </p>
                                <p>
                                <label for='ju'>Jungen: </label>
                                <input type='radio' id='ju' name='geschlecht' value='M' checked>  
                                <label for='mae'>M&auml;dchen: </label>
                                <input type='radio' id='mae' name='geschlecht' value='W'>  
                            </p>
                """.translate(HTML))
        print("             <p><button> Anzeigen! </button></p>")
        print("             </form>")
        print("<p></p>")
        print("             </article>")

        # if login == "admin":
        #     print("             <article>")
        #     print("             <h1>Administration</h1>")
        #     print("             <form action='http://sportfestserver/cgi-bin/einlesen.py' method='post'>")
        #     print("             <p><strong>Tabelle leeren und Schülerdaten einlesen</strong></p>".translate(HTML))
        #     print("             <p>Datei mit Schülerdaten auswählen:</p>".translate(HTML))
        #     print("             <p><input type='file' name = 'filepath' ></p>")
        #     print("             <p><button> einlesen </button></p>")
        #     print("             </form>")
        #     print("             </article>")
        #
        # print("         </section>")
    elif login == "sprint":
        print("         <section>")
        print("             <article>")
        print("             <h1>Ergebnisse eintragen - Sprint</h1>")
        print("             <p>Wählen Sie Klasse und Geschlecht aus!</p>".translate(HTML))
        print("             <form action='http://sportfestserver/cgi-bin/eintragen.py' method='post'>")
        print("             <input type='hidden' name = 'login' value = {} >".format(login))
        print("             <input type='hidden' name = 'password' value = {} >".format(password))
        print("             <input type='hidden' name = 'sportart' value = 'Sprint' >")
        print("""           <p>
                                        <label for='klasse'>Klasse: </label>
                                        <select name='klasse'> 
                                            <option>Klassen</option>""")
        for dsatz in cursor:
            print("                     <option>", dsatz['klasse'], "</option>")
        print("""				</select>
                                    </p>
                                    <p>
                                        <label for='ju'>Jungen: </label>
                                        <input type='radio' id='ju' name='geschlecht' value='M' checked>  
                                        <label for='mae'>M&auml;dchen: </label>
                                        <input type='radio' id='mae' name='geschlecht' value='W'>  
                                    </p>
                                    <p>
                                        <button>absenden</button>
                                    </p>
                """)
        print("             </form>")
        print("             </article>")
        print("         </section>")
    elif login == "sprung":
        print("         <section>")
        print("             <article>")
        print("             <h1>Ergebnisse eintragen - Weitsprung</h1>")
        print("             <p>Wählen Sie Klasse und Geschlecht aus!</p>".translate(HTML))
        print("             <form action='http://sportfestserver/cgi-bin/eintragen.py' method='post'>")
        print("             <input type='hidden' name = 'login' value = {} >".format(login))
        print("             <input type='hidden' name = 'password' value = {} >".format(password))
        print("             <input type='hidden' name = 'sportart' value = 'Sprung' >")
        print("""           <p>
                                        <label for='klasse'>Klasse: </label>
                                        <select name='klasse'> 
                                            <option>Klassen</option>""")
        for dsatz in cursor:
            print("                     <option>", dsatz['klasse'], "</option>")
        print("""				</select>
                                    </p>
                                    <p>
                                        <label for='ju'>Jungen: </label>
                                        <input type='radio' id='ju' name='geschlecht' value='M' checked>  
                                        <label for='mae'>M&auml;dchen: </label>
                                        <input type='radio' id='mae' name='geschlecht' value='W'>  
                                    </p>
                                    <p>
                                        <button>absenden</button>
                                    </p>
                """)
        print("             </form>")
        print("             </article>")
        print("         </section>")
    elif login == "wurf":
        print("         <section>")
        print("             <article>")
        print("             <h1>Ergebnisse eintragen - Ballweitwurf</h1>")
        print("             <p>Wählen Sie Klasse und Geschlecht aus!</p>".translate(HTML))
        print("             <form action='http://sportfestserver/cgi-bin/eintragen.py' method='post'>")
        print("             <input type='hidden' name = 'login' value = {} >".format(login))
        print("             <input type='hidden' name = 'password' value = {} >".format(password))
        print("             <input type='hidden' name = 'sportart' value = 'Wurf' >")
        print("""           <p>
                                        <label for='klasse'>Klasse: </label>
                                        <select name='klasse'> 
                                            <option>Klassen</option>""")
        for dsatz in cursor:
            if int(dsatz["stufe"]) < 8:
                print("                     <option>", dsatz['klasse'], "</option>")
        print("""				</select>
                                    </p>
                                    <p>
                                        <label for='ju'>Jungen: </label>
                                        <input type='radio' id='ju' name='geschlecht' value='M' checked>  
                                        <label for='mae'>M&auml;dchen: </label>
                                        <input type='radio' id='mae' name='geschlecht' value='W'>  
                                    </p>
                                    <p>
                                        <button>absenden</button>
                                    </p>
                """)
        print("             </form>")
        print("             </article>")
        print("         </section>")
    elif login == "kugel":
        print("         <section>")
        print("             <article>")
        print("             <h1>Ergebnisse eintragen - Kugelstoßen</h1>".translate(HTML))
        print("             <p>Wählen Sie Klasse und Geschlecht aus!</p>".translate(HTML))
        print("             <form action='http://sportfestserver/cgi-bin/eintragen.py' method='post'>")
        print("             <input type='hidden' name = 'login' value = {} >".format(login))
        print("             <input type='hidden' name = 'password' value = {} >".format(password))
        print("             <input type='hidden' name = 'sportart' value = 'Kugel' >")
        print("""           <p>
                                        <label for='klasse'>Klasse: </label>
                                        <select name='klasse'> 
                                            <option>Klassen</option>""")
        for dsatz in cursor:
            if int(dsatz["stufe"]) >= 8:
                print("                     <option>", dsatz['klasse'], "</option>")
        print("""				</select>
                                    </p>
                                    <p>
                                        <label for='ju'>Jungen: </label>
                                        <input type='radio' id='ju' name='geschlecht' value='M' checked>  
                                        <label for='mae'>M&auml;dchen: </label>
                                        <input type='radio' id='mae' name='geschlecht' value='W'>  
                                    </p>
                                    <p>
                                        <button>absenden</button>
                                    </p>
                """)
        print("             </form>")
        print("             </article>")
        print("         </section>")
else:
    print(LOGINFEHLER)


print(FOOTER)