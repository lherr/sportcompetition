HTML = {ord("ä"): "&auml;", ord("ö"): "&ouml;",
        ord("ü"): "&uuml;", ord("Ä"): "&Auml;",
        ord("Ö"): "&Ouml;", ord("Ü"): "&Uuml;",
        ord("ß"): "&szlig;", ord("è"): "&egrave;",
        ord("é"): "&eacute;", ord("à"): "&agrave;",
        ord("á"): "&aacute;", ord("ò"): "&ograve;",
        ord("ó"): "&oacute;", ord("ù"): "&ugrave;",
        ord("ú"): "&uacute;"}

LATEX = {ord("ä"): "\\\"a", ord("ö"): "\\\"o",
        ord("ü"): "\\\"u", ord("Ä"): "\\\"A",
        ord("Ö"): "\\\"O", ord("Ü"): "\\\"U",
        ord("ß"): "\\ss{}", ord("è"): "\\`{e}",
        ord("é"): "\\\'{e}", ord("à"): "\\`{a}",
        ord("á"): "\\\'{a}", ord("ò"): "\\`{o}",
        ord("ó"): "\\\'{o}", ord("ù"): "\\`{u}",
        ord("ú"): "\\\'{u}"}


USERS ={"admin":"25deb7c1a54ef06fa43a7920d1072376", "sportlehrer":"25deb7c1a54ef06fa43a7920d1072376",
        "sprint": "25deb7c1a54ef06fa43a7920d1072376", "sprung": "25deb7c1a54ef06fa43a7920d1072376",
        "kugel": "25deb7c1a54ef06fa43a7920d1072376", "wurf": "25deb7c1a54ef06fa43a7920d1072376"}

HEADER = """Content-type:text/html; char-set=utf8

<!DOCTYPE html>
<html>
    <head>
		<meta http-equiv="Content-Type" content="charset=utf-8" />
		<title>Sportfest</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximal-scale=1">
		<link href="http://sportfestserver/sportfest.css" rel="stylesheet" type="text/css">
	</head>
	<body>
		<div id="wrapper">
		<header><h1>Auswertungsprogramm Sportfest</h1></header>
		"""

NAV1 ="""
        <nav>
                <ul>
                        <li><a href='#'>&Uuml;bersicht</a></li>
                </ul>
        </nav>
"""

FOOTER ="""	
		<footer><p>&copy; Lutz Herrmann - 2018 bis 2019</p></footer>
		</div>
	</body>
</html>"""

LOGINFEHLER="""
        <section>
             <article>
                 <h1>Falsche Logindaten!</h1>
                 <p><a href='http://localhost'>Zur&uuml;ck</a></p>
             </article>
         </section>"""

LATEXHEADER="""\\documentclass[10pt,a4paper]{scrartcl}
\\usepackage[utf8]{inputenc}
\\usepackage[german]{babel}
\\usepackage[T1]{fontenc}
\\usepackage{yfonts}
\\usepackage{amsmath}
\\usepackage{amsfonts}
\\usepackage{amssymb}
\\usepackage{graphicx}
\\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}
\\usepackage{palatino}
\\pagestyle{empty}

\\begin{document}
\\begin{center}
"""

LATEXFOOTER="""\\end{center}
\\end{document}
"""

URKUNDENHEADER="""\\documentclass[10pt,a4paper]{scrartcl}
\\usepackage[utf8]{inputenc}
\\usepackage[german]{babel}
\\usepackage[T1]{fontenc}
\\usepackage{yfonts}
\\usepackage{amsmath}
\\usepackage{amsfonts}
\\usepackage{amssymb}
\\usepackage{graphicx}
\\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}
\\usepackage{palatino}
\\pagestyle{empty}

\\begin{document}
"""

URKUNDE1="""\\begin{center}

{\Large Georgius-Agricola-Gymnasium Glauchau}

\\vspace*{0,5cm}

\\includegraphics[scale=0.25]{schullogo}

\\vspace*{0,5cm}

{\\fontfamily{pzc}
\\fontseries{b}
\\fontsize{80}{100}
\\selectfont
Urkunde}

\\vspace*{2cm}

\\begin{minipage}{4cm}
\\includegraphics[scale=0.3]{sportbild}
\\end{minipage}
\\begin{minipage}{12cm}
\\begin{center}
"""

URKUNDE2="""\\end{center}

\\end{minipage}




\\end{center}

\\vspace*{2cm}"""

URKUNDE3="""

\\begin{flushright}
{\\large $\\overline{\\text{Wettkampfleiter}}$}
\\end{flushright}

"""