import math

class Schueler:
    __schnr = None
    __nname = None
    __vname = None
    __klasse = None
    __stufe = None
    __geschlecht = None
    __lauf = None
    __notelauf = None
    __punktelauf = None
    __sprung1 = None
    __sprung2 = None
    __sprung3 = None
    __bestsprung = None
    __notesprung = None
    __punktesprung = None
    __wurfstoss1 = None
    __wurfstoss2 = None
    __wurfstoss3 = None
    __bestwurfstoss = None
    __notewurfstoss = None
    __punktewurfstoss = None
    __punktemehrkampf = None
    __bemerkung = None

    def setSchnr(self, schnr):
        self.__schnr = schnr

    def getSchnr(self):
        return self.__schnr
        
    def setNname(self, nname):
        self.__nname = nname

    def getNname(self):
        return self.__nname

    def setVname(self, vname):
        self.__vname = vname

    def getVname(self):
        return self.__vname

    def setKlasse(self, klasse):
        self.__klasse = klasse

    def getKlasse(self):
        return self.__klasse

    def setStufe(self, stufe):
        self.__stufe = stufe

    def getStufe(self):
        return self.__stufe

    def setGeschlecht(self, geschlecht):
        if geschlecht in ["männlich", "weiblich"]:
            self.__geschlecht = geschlecht

    def getGeschlecht(self):
        return self.__geschlecht

    def setLauf(self, lauf):
        self.__lauf = lauf

    def getLauf(self):
        return self.__lauf

    def setPunktelauf(self):
        if self.__lauf is not None:
            if self.__stufe in [5, 6]:
                if self.__geschlecht == "weiblich":
                    self.__punktelauf = int(((50 / (self.__lauf + 0.24)) - 3.648) / 0.0066)
                elif self.__geschlecht == "männlich":
                    self.__punktelauf = int(((50/(self.__lauf+0.24))-3.79)/0.0069)
            elif self.__stufe in [7, 8]:
                if self.__geschlecht == "weiblich":
                    self.__punktelauf = int(((75/(self.__lauf+0.24))-3.998)/0.0066)
                elif self.__geschlecht == "männlich":
                    self.__punktelauf = int(((75/(self.__lauf+0.24))-4.1)/0.00664)
            elif self.__stufe in [9, 10]:
                if self.__geschlecht == "weiblich":
                    self.__punktelauf = int(((100/(self.__lauf+0.24))-4.0062)/0.00656)
                elif self.__geschlecht == "männlich":
                    self.__punktelauf = int(((100/(self.__lauf+0.24))-4.341)/0.00676)

    def getPunktelauf(self):
        return self.__punktelauf


    def setNotelauf(self):
        if self.__lauf is not None:
            if self.__stufe == 5:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__lauf <= 8.1:
                        self.__notelauf = 1
                    elif 8.1 < self.__lauf <= 8.7:
                        self.__notelauf = 2
                    elif 8.7 < self.__lauf <= 9.3:
                        self.__notelauf = 3
                    elif 9.3 < self.__lauf <= 9.8:
                        self.__notelauf = 4
                    elif 9.8 < self.__lauf <= 10.6:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__lauf <= 8.3:
                        self.__notelauf = 1
                    elif 8.3 < self.__lauf <= 9.0:
                        self.__notelauf = 2
                    elif 9.0 < self.__lauf <= 9.5:
                        self.__notelauf = 3
                    elif 9.5 < self.__lauf <= 9.9:
                        self.__notelauf = 4
                    elif 9.9 < self.__lauf <= 10.7:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
            elif self.__stufe == 6:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__lauf <= 7.7:
                        self.__notelauf = 1
                    elif 7.7 < self.__lauf <= 8.4:
                        self.__notelauf = 2
                    elif 8.4 < self.__lauf <= 9.1:
                        self.__notelauf = 3
                    elif 9.1 < self.__lauf <= 9.7:
                        self.__notelauf = 4
                    elif 9.7 < self.__lauf <= 10.5:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__lauf <= 8.2:
                        self.__notelauf = 1
                    elif 8.2 < self.__lauf <= 8.7:
                        self.__notelauf = 2
                    elif 8.7 < self.__lauf <= 9.3:
                        self.__notelauf = 3
                    elif 9.3 < self.__lauf <= 9.8:
                        self.__notelauf = 4
                    elif 9.8 < self.__lauf <= 10.4:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
            elif self.__stufe == 7:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__lauf <= 10.8:
                        self.__notelauf = 1
                    elif 10.8 < self.__lauf <= 11.8:
                        self.__notelauf = 2
                    elif 11.8 < self.__lauf <= 12.9:
                        self.__notelauf = 3
                    elif 12.9 < self.__lauf <= 13.5:
                        self.__notelauf = 4
                    elif 13.5 < self.__lauf <= 14.5:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__lauf <= 11.8:
                        self.__notelauf = 1
                    elif 11.8 < self.__lauf <= 12.8:
                        self.__notelauf = 2
                    elif 12.8 < self.__lauf <= 13.6:
                        self.__notelauf = 3
                    elif 13.6 < self.__lauf <= 14.0:
                        self.__notelauf = 4
                    elif 14.0 < self.__lauf <= 14.8:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
            elif self.__stufe == 8:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__lauf <= 10.6:
                        self.__notelauf = 1
                    elif 10.6 < self.__lauf <= 11.5:
                        self.__notelauf = 2
                    elif 11.5 < self.__lauf <= 12.4:
                        self.__notelauf = 3
                    elif 12.4 < self.__lauf <= 13:
                        self.__notelauf = 4
                    elif 13 < self.__lauf <= 13.8:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__lauf <= 11.7:
                        self.__notelauf = 1
                    elif 11.7 < self.__lauf <= 12.7:
                        self.__notelauf = 2
                    elif 12.7 < self.__lauf <= 13.3:
                        self.__notelauf = 3
                    elif 13.3 < self.__lauf <= 13.8:
                        self.__notelauf = 4
                    elif 13.8 < self.__lauf <= 14.5:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
            elif self.__stufe == 9:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__lauf <= 13.3:
                        self.__notelauf = 1
                    elif 13.3 < self.__lauf <= 14.2:
                        self.__notelauf = 2
                    elif 14.2 < self.__lauf <= 15.3:
                        self.__notelauf = 3
                    elif 15.3 < self.__lauf <= 16.4:
                        self.__notelauf = 4
                    elif 16.4 < self.__lauf <= 17.9:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__lauf <= 15.0:
                        self.__notelauf = 1
                    elif 15.0 < self.__lauf <= 16.1:
                        self.__notelauf = 2
                    elif 16.1 < self.__lauf <= 17.2:
                        self.__notelauf = 3
                    elif 17.2 < self.__lauf <= 18.3:
                        self.__notelauf = 4
                    elif 18.3 < self.__lauf <= 19.7:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
            elif self.__stufe == 10:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__lauf <= 13.0:
                        self.__notelauf = 1
                    elif 13.0 < self.__lauf <= 13.6:
                        self.__notelauf = 2
                    elif 13.6 < self.__lauf <= 14.5:
                        self.__notelauf = 3
                    elif 14.5 < self.__lauf <= 15.6:
                        self.__notelauf = 4
                    elif 15.6 < self.__lauf <= 16.9:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__lauf <= 14.9:
                        self.__notelauf = 1
                    elif 14.9 < self.__lauf <= 16.0:
                        self.__notelauf = 2
                    elif 16.0 < self.__lauf <= 17.0:
                        self.__notelauf = 3
                    elif 17.0 < self.__lauf <= 18.1:
                        self.__notelauf = 4
                    elif 18.1 < self.__lauf <= 19.4:
                        self.__notelauf = 5
                    else:
                        self.__notelauf = 6

    def getNotelauf(self):
        return self.__notelauf

    def setSprung(self, sprung1, sprung2, sprung3):
        self.__sprung1 = sprung1
        self.__sprung2 = sprung2
        self.__sprung3 = sprung3

    def getSprung(self):
        return [self.__sprung1, self.__sprung2, self.__sprung3]

    def setBestsprung(self):
        spr = []
        for wert in self.getSprung():
            if wert is not None:
                spr.append(wert)
        if len(spr) != 0:
            self.__bestsprung = max(spr)

    def getBestsprung(self):
        return self.__bestsprung

    def setPunktesprung(self):
        if self.__bestsprung is not None:
            if self.__geschlecht == "männlich":
                self.__punktesprung = int((math.sqrt(self.__bestsprung)-1.15028)/0.00219)
            elif self.__geschlecht == "weiblich":
                self.__punktesprung = int((math.sqrt(self.__bestsprung)-1.0935)/0.00208)

    def getPunktesprung(self):
        return self.__punktesprung

    def setNotesprung(self):
        if self.__bestsprung is not None:
            if self.__stufe == 5:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestsprung >= 3.7:
                        self.__notesprung = 1
                    elif 3.7 > self.__bestsprung >= 3.26:
                        self.__notesprung = 2
                    elif 3.26 > self.__bestsprung >= 2.90:
                        self.__notesprung = 3
                    elif 2.90 > self.__bestsprung >= 2.67:
                        self.__notesprung = 4
                    elif 2.67 > self.__bestsprung >= 2.25:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestsprung >= 3.38:
                        self.__notesprung = 1
                    elif 3.38 > self.__bestsprung >= 2.90:
                        self.__notesprung = 2
                    elif 2.90 > self.__bestsprung >= 2.63:
                        self.__notesprung = 3
                    elif 2.63 > self.__bestsprung >= 2.40:
                        self.__notesprung = 4
                    elif 2.40 > self.__bestsprung >= 2.10:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
            elif self.__stufe == 6:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestsprung >= 3.74:
                        self.__notesprung = 1
                    elif 3.74 > self.__bestsprung >= 3.37:
                        self.__notesprung = 2
                    elif 3.37 > self.__bestsprung >= 3.00:
                        self.__notesprung = 3
                    elif 3.00 > self.__bestsprung >= 2.75:
                        self.__notesprung = 4
                    elif 2.75 > self.__bestsprung >= 2.35:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
                elif self.__geschlecht == "weiblich": # erledigt
                    if self.__bestsprung >= 3.49:
                        self.__notesprung = 1
                    elif 3.49 > self.__bestsprung >= 3.10:
                        self.__notesprung = 2
                    elif 3.10 > self.__bestsprung >= 2.75:
                        self.__notesprung = 3
                    elif 2.75 > self.__bestsprung >= 2.58:
                        self.__notesprung = 4
                    elif 2.58 > self.__bestsprung >= 2.21:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
            elif self.__stufe == 7:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestsprung >= 3.98:
                        self.__notesprung = 1
                    elif 3.98 > self.__bestsprung >= 3.51:
                        self.__notesprung = 2
                    elif 3.51 > self.__bestsprung >= 3.15:
                        self.__notesprung = 3
                    elif 3.15 > self.__bestsprung >= 2.85:
                        self.__notesprung = 4
                    elif 2.85 > self.__bestsprung >= 2.51:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestsprung >= 3.70:
                        self.__notesprung = 1
                    elif 3.70 > self.__bestsprung >= 3.35:
                        self.__notesprung = 2
                    elif 3.35 > self.__bestsprung >= 3.05:
                        self.__notesprung = 3
                    elif 3.05 > self.__bestsprung >= 2.72:
                        self.__notesprung = 4
                    elif 2.72 > self.__bestsprung >= 2.32:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
            elif self.__stufe == 8:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestsprung >= 4.37:
                        self.__notesprung = 1
                    elif 4.37 > self.__bestsprung >= 3.80:
                        self.__notesprung = 2
                    elif 3.80 > self.__bestsprung >= 3.32:
                        self.__notesprung = 3
                    elif 3.32 > self.__bestsprung >= 3.04:
                        self.__notesprung = 4
                    elif 3.04 > self.__bestsprung >= 2.70:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
                elif self.__geschlecht == "weiblich":
                    if self.__bestsprung >= 3.73:
                        self.__notesprung = 1
                    elif 3.73 > self.__bestsprung >= 3.42:
                        self.__notesprung = 2
                    elif 3.42 > self.__bestsprung >= 3.10:
                        self.__notesprung = 3
                    elif 3.10 > self.__bestsprung >= 2.75:
                        self.__notesprung = 4
                    elif 2.75 > self.__bestsprung >= 2.37:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
            elif self.__stufe == 9:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestsprung >= 4.80:
                        self.__notesprung = 1
                    elif 4.80 > self.__bestsprung >= 4.08:
                        self.__notesprung = 2
                    elif 4.08 > self.__bestsprung >= 3.55:
                        self.__notesprung = 3
                    elif 3.55 > self.__bestsprung >= 3.32:
                        self.__notesprung = 4
                    elif 3.32 > self.__bestsprung >= 2.91:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestsprung >= 3.75:
                        self.__notesprung = 1
                    elif 3.75 > self.__bestsprung >= 3.52:
                        self.__notesprung = 2
                    elif 3.52 > self.__bestsprung >= 3.12:
                        self.__notesprung = 3
                    elif 3.12 > self.__bestsprung >= 2.84:
                        self.__notesprung = 4
                    elif 2.84 > self.__bestsprung >= 2.40:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
            elif self.__stufe == 10:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestsprung >= 5.02:
                        self.__notesprung = 1
                    elif 5.02 > self.__bestsprung >= 4.48:
                        self.__notesprung = 2
                    elif 4.48 > self.__bestsprung >= 3.73:
                        self.__notesprung = 3
                    elif 3.73 > self.__bestsprung >= 3.53:
                        self.__notesprung = 4
                    elif 3.53 > self.__bestsprung >= 3.10:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestsprung >= 3.92:
                        self.__notesprung = 1
                    elif 3.92 > self.__bestsprung >= 3.60:
                        self.__notesprung = 2
                    elif 3.60 > self.__bestsprung >= 3.15:
                        self.__notesprung = 3
                    elif 3.15 > self.__bestsprung >= 2.86:
                        self.__notesprung = 4
                    elif 2.86 > self.__bestsprung >= 2.49:
                        self.__notesprung = 5
                    else:
                        self.__notesprung = 6

    def getNotesprung(self):
        return self.__notesprung

    def setWurfstoss(self, wurfstoss1, wurfstoss2, wurfstoss3):
        self.__wurfstoss1 = wurfstoss1
        self.__wurfstoss2 = wurfstoss2
        self.__wurfstoss3 = wurfstoss3

    def getWurfstoss(self):
        return [self.__wurfstoss1, self.__wurfstoss2, self.__wurfstoss3]


    def setBestwurfstoss(self):
        wst = []
        for wert in self.getWurfstoss():
            if wert is not None:
                wst.append(wert)
        if len(wst) != 0:
            self.__bestwurfstoss = max(wst)

    def getBestwurfstoss(self):
        return self.__bestwurfstoss

    def setPunktewurfstoss(self):
        if self.__bestwurfstoss is not None:
            if self.__stufe in [5, 6, 7]:
                if self.__geschlecht == "männlich":
                    self.__punktewurfstoss = int((math.sqrt(self.__bestwurfstoss) - 1.936)/0.0124)
                elif self.__geschlecht == "weiblich":
                    self.__punktewurfstoss = int((math.sqrt(self.__bestwurfstoss)-1.4149)/0.01039)
            elif self.__stufe in [8, 9, 10]:
                if self.__geschlecht == "männlich":
                    self.__punktewurfstoss = int((math.sqrt(self.__bestwurfstoss) - 1.425) / 0.0037)
                elif self.__geschlecht == "weiblich":
                    self.__punktewurfstoss = int((math.sqrt(self.__bestwurfstoss) - 1.279) / 0.00398)

    def getPunktewurfstoss(self):
        return self.__punktewurfstoss


    def setNotewurfstoss(self):
        if self.__bestwurfstoss is not None:
            if self.__stufe == 5:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestwurfstoss >= 37.0:
                        self.__notewurfstoss = 1
                    elif 37.0 > self.__bestwurfstoss >= 31.0:
                        self.__notewurfstoss = 2
                    elif 31.0 > self.__bestwurfstoss >= 24.5:
                        self.__notewurfstoss = 3
                    elif 24.5 > self.__bestwurfstoss >= 21.5:
                        self.__notewurfstoss = 4
                    elif 21.5 > self.__bestwurfstoss >= 17.0:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestwurfstoss >= 25.0:
                        self.__notewurfstoss = 1
                    elif 25.0 > self.__bestwurfstoss >= 20.5:
                        self.__notewurfstoss = 2
                    elif 20.5 > self.__bestwurfstoss >= 15.5:
                        self.__notewurfstoss = 3
                    elif 15.5 > self.__bestwurfstoss >= 12.5:
                        self.__notewurfstoss = 4
                    elif 12.5 > self.__bestwurfstoss >= 9.5:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
            elif self.__stufe == 6:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestwurfstoss >= 42.0:
                        self.__notewurfstoss = 1
                    elif 42.0 > self.__bestwurfstoss >= 34.5:
                        self.__notewurfstoss = 2
                    elif 34.5 > self.__bestwurfstoss >= 27.0:
                        self.__notewurfstoss = 3
                    elif 27.0 > self.__bestwurfstoss >= 24.0:
                        self.__notewurfstoss = 4
                    elif 24.0 > self.__bestwurfstoss >= 19.0:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestwurfstoss >= 27.5:
                        self.__notewurfstoss = 1
                    elif 27.5 > self.__bestwurfstoss >= 22.5:
                        self.__notewurfstoss = 2
                    elif 22.5 > self.__bestwurfstoss >= 17.5:
                        self.__notewurfstoss = 3
                    elif 17.5 > self.__bestwurfstoss >= 14.5:
                        self.__notewurfstoss = 4
                    elif 14.5 > self.__bestwurfstoss >= 11.0:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
            elif self.__stufe == 7:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestwurfstoss >= 45.0:
                        self.__notewurfstoss = 1
                    elif 45.0 > self.__bestwurfstoss >= 36.0:
                        self.__notewurfstoss = 2
                    elif 36.0 > self.__bestwurfstoss >= 30.5:
                        self.__notewurfstoss = 3
                    elif 30.5 > self.__bestwurfstoss >= 27.0:
                        self.__notewurfstoss = 4
                    elif 27.0 > self.__bestwurfstoss >= 22.5:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestwurfstoss >= 30.0:
                        self.__notewurfstoss = 1
                    elif 30.0 > self.__bestwurfstoss >= 24.0:
                        self.__notewurfstoss = 2
                    elif 24.0 > self.__bestwurfstoss >= 18.0:
                        self.__notewurfstoss = 3
                    elif 18.0 > self.__bestwurfstoss >= 16.5:
                        self.__notewurfstoss = 4
                    elif 16.5 > self.__bestwurfstoss >= 13.0:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
            elif self.__stufe == 8:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestwurfstoss >= 8.6:
                        self.__notewurfstoss = 1
                    elif 8.6 > self.__bestwurfstoss >= 7.6:
                        self.__notewurfstoss = 2
                    elif 7.6 > self.__bestwurfstoss >= 6.5:
                        self.__notewurfstoss = 3
                    elif 6.5 > self.__bestwurfstoss >= 5.7:
                        self.__notewurfstoss = 4
                    elif 5.7 > self.__bestwurfstoss >= 4.8:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestwurfstoss >= 7.3:
                        self.__notewurfstoss = 1
                    elif 7.3 > self.__bestwurfstoss >= 6.4:
                        self.__notewurfstoss = 2
                    elif 6.4 > self.__bestwurfstoss >= 5.6:
                        self.__notewurfstoss = 3
                    elif 5.6 > self.__bestwurfstoss >= 5.0:
                        self.__notewurfstoss = 4
                    elif 5.0 > self.__bestwurfstoss >= 4.3:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
            elif self.__stufe == 9:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestwurfstoss >= 9.3:
                        self.__notewurfstoss = 1
                    elif 9.3 > self.__bestwurfstoss >= 8.5:
                        self.__notewurfstoss = 2
                    elif 8.5 > self.__bestwurfstoss >= 7.7:
                        self.__notewurfstoss = 3
                    elif 7.7 > self.__bestwurfstoss >= 7.0:
                        self.__notewurfstoss = 4
                    elif 7.0 > self.__bestwurfstoss >= 5.8:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestwurfstoss >= 7.5:
                        self.__notewurfstoss = 1
                    elif 7.5 > self.__bestwurfstoss >= 6.6:
                        self.__notewurfstoss = 2
                    elif 6.6 > self.__bestwurfstoss >= 5.8:
                        self.__notewurfstoss = 3
                    elif 5.8 > self.__bestwurfstoss >= 5.3:
                        self.__notewurfstoss = 4
                    elif 5.3 > self.__bestwurfstoss >= 4.8:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
            elif self.__stufe == 10:
                if self.__geschlecht == "männlich": #erledigt
                    if self.__bestwurfstoss >= 9.9:
                        self.__notewurfstoss = 1
                    elif 9.9 > self.__bestwurfstoss >= 9.0:
                        self.__notewurfstoss = 2
                    elif 9.0 > self.__bestwurfstoss >= 8.1:
                        self.__notewurfstoss = 3
                    elif 8.1 > self.__bestwurfstoss >= 7.6:
                        self.__notewurfstoss = 4
                    elif 7.6 > self.__bestwurfstoss >= 6.8:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6
                elif self.__geschlecht == "weiblich": #erledigt
                    if self.__bestwurfstoss >= 7.6:
                        self.__notewurfstoss = 1
                    elif 7.6 > self.__bestwurfstoss >= 6.7:
                        self.__notewurfstoss = 2
                    elif 6.7 > self.__bestwurfstoss >= 6.0:
                        self.__notewurfstoss = 3
                    elif 6.0 > self.__bestwurfstoss >= 5.6:
                        self.__notewurfstoss = 4
                    elif 5.6 > self.__bestwurfstoss >= 5.0:
                        self.__notewurfstoss = 5
                    else:
                        self.__notewurfstoss = 6

    def getNotewurfstoss(self):
        return self.__notewurfstoss

    def setPunktemehrkampf(self):
        p = []
        if self.__punktelauf is not None:
            p.append(self.__punktelauf)
        if self.__punktesprung is not None:
            p.append(self.__punktesprung)
        if self.__punktewurfstoss is not None:
            p.append(self.__punktewurfstoss)
        if len(p) > 0:
            self.__punktemehrkampf = sum(p)

    def getPunktemehrkampf(self):
        return self.__punktemehrkampf

    def setAll(self):
        self.setPunktelauf()
        self.setNotelauf()
        self.setBestsprung()
        self.setPunktesprung()
        self.setNotesprung()
        self.setBestwurfstoss()
        self.setPunktewurfstoss()
        self.setNotewurfstoss()
        self.setPunktemehrkampf()

    def __init__(self, schnr, nname, vname, klasse, stufe, geschlecht):
        self.setSchnr(schnr)
        self.setNname(nname)
        self.setVname(vname)
        self.setKlasse(klasse)
        self.setStufe(stufe)
        self.setGeschlecht(geschlecht)

if __name__ == '__main__':
    schueler = Schueler(1,"Mustermann","Willi", "a", 10, "weiblich")
    print(schueler.getSchnr(), schueler.getNname(), schueler.getVname(),
          schueler.getKlasse(), schueler.getStufe(), schueler.getGeschlecht())
    schueler.setLauf(14.4)
    schueler.setSprung(4.34, None, None)
    schueler.setWurfstoss(8.07, None, None)
    schueler.setAll()
    print("Lauf - Zeit:",schueler.getLauf(), "Punkte:", schueler.getPunktelauf(), "Note:", schueler.getNotelauf())
    print("Sprung: - Weite:",schueler.getBestsprung(), "Punkte:", schueler.getPunktesprung(), "Note:", schueler.getNotesprung())
    print("Wurfstoss: - Weite:",schueler.getBestwurfstoss(), "Punkte:", schueler.getPunktewurfstoss(), "Note:", schueler.getNotewurfstoss())
    print("Mehrkampf:",schueler.getPunktemehrkampf())
