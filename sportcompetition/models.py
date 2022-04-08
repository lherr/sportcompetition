from django.db import models
import math

# Create your models here.

class Schueler(models.Model):
    schnr = models.IntegerField(primary_key=True)
    nname = models.CharField(max_length=200)
    vname = models.CharField(max_length=200)
    klasse = models.CharField(max_length=20)
    stufe = models.IntegerField()
    geschlecht = models.CharField(max_length=20)
    lauf = models.FloatField(blank=True, null=True)
    notelauf = models.IntegerField(blank=True, null=True)
    punktelauf = models.IntegerField(blank=True, null=True)
    sprung1 = models.FloatField(blank=True, null=True)
    sprung2 = models.FloatField(blank=True, null=True)
    sprung3 = models.FloatField(blank=True, null=True)
    bestsprung = models.FloatField(blank=True, null=True)
    notesprung = models.IntegerField(blank=True, null=True)
    punktesprung = models.IntegerField(blank=True, null=True)
    wurfstoss1 = models.FloatField(blank=True, null=True)
    wurfstoss2 = models.FloatField(blank=True, null=True)
    wurfstoss3 = models.FloatField(blank=True, null=True)
    bestwurfstoss = models.FloatField(blank=True, null=True)
    notewurfstoss = models.IntegerField(blank=True, null=True)
    punktewurfstoss = models.IntegerField(blank=True, null=True)
    punktemehrkampf = models.IntegerField(blank=True, null=True)
    bemerkung = models.TextField(blank=True, null=True)

    def setSchnr(self, schnr):
        self.schnr = schnr
        self.save()

    def getSchnr(self):
        return self.schnr
        
    def setNname(self, nname):
        self.nname = nname
        self.save()

    def getNname(self):
        return self.nname

    def setVname(self, vname):
        self.vname = vname
        self.save()

    def getVname(self):
        return self.vname

    def setKlasse(self, klasse):
        self.klasse = klasse
        self.save()

    def getKlasse(self):
        return self.klasse

    def setStufe(self, stufe):
        self.stufe = stufe
        self.save()

    def getStufe(self):
        return self.stufe

    def setGeschlecht(self, geschlecht):
        if geschlecht in ["männlich", "weiblich"]:
            self.geschlecht = geschlecht
        self.save()

    def getGeschlecht(self):
        return self.geschlecht

    def setLauf(self, lauf):
        self.lauf = lauf
        self.save()

    def getLauf(self):
        return self.lauf

    def setPunktelauf(self):
        if self.lauf is not None:
            if self.stufe in [5, 6]:
                if self.geschlecht == "weiblich":
                    self.punktelauf = int(((50 / (self.lauf + 0.24)) - 3.648) / 0.0066)
                elif self.geschlecht == "männlich":
                    self.punktelauf = int(((50/(self.lauf+0.24))-3.79)/0.0069)
            elif self.stufe in [7, 8]:
                if self.geschlecht == "weiblich":
                    self.punktelauf = int(((75/(self.lauf+0.24))-3.998)/0.0066)
                elif self.geschlecht == "männlich":
                    self.punktelauf = int(((75/(self.lauf+0.24))-4.1)/0.00664)
            elif self.stufe in [9, 10]:
                if self.geschlecht == "weiblich":
                    self.punktelauf = int(((100/(self.lauf+0.24))-4.0062)/0.00656)
                elif self.geschlecht == "männlich":
                    self.punktelauf = int(((100/(self.lauf+0.24))-4.341)/0.00676)
        self.save()

    def getPunktelauf(self):
        return self.punktelauf


    def setNotelauf(self):
        if self.lauf is not None:
            if self.stufe == 5:
                if self.geschlecht == "männlich": #erledigt
                    if self.lauf <= 8.1:
                        self.notelauf = 1
                    elif 8.1 < self.lauf <= 8.7:
                        self.notelauf = 2
                    elif 8.7 < self.lauf <= 9.3:
                        self.notelauf = 3
                    elif 9.3 < self.lauf <= 9.8:
                        self.notelauf = 4
                    elif 9.8 < self.lauf <= 10.6:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.lauf <= 8.3:
                        self.notelauf = 1
                    elif 8.3 < self.lauf <= 9.0:
                        self.notelauf = 2
                    elif 9.0 < self.lauf <= 9.5:
                        self.notelauf = 3
                    elif 9.5 < self.lauf <= 9.9:
                        self.notelauf = 4
                    elif 9.9 < self.lauf <= 10.7:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
            elif self.stufe == 6:
                if self.geschlecht == "männlich": #erledigt
                    if self.lauf <= 7.7:
                        self.notelauf = 1
                    elif 7.7 < self.lauf <= 8.4:
                        self.notelauf = 2
                    elif 8.4 < self.lauf <= 9.1:
                        self.notelauf = 3
                    elif 9.1 < self.lauf <= 9.7:
                        self.notelauf = 4
                    elif 9.7 < self.lauf <= 10.5:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.lauf <= 8.2:
                        self.notelauf = 1
                    elif 8.2 < self.lauf <= 8.7:
                        self.notelauf = 2
                    elif 8.7 < self.lauf <= 9.3:
                        self.notelauf = 3
                    elif 9.3 < self.lauf <= 9.8:
                        self.notelauf = 4
                    elif 9.8 < self.lauf <= 10.4:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
            elif self.stufe == 7:
                if self.geschlecht == "männlich": #erledigt
                    if self.lauf <= 10.8:
                        self.notelauf = 1
                    elif 10.8 < self.lauf <= 11.8:
                        self.notelauf = 2
                    elif 11.8 < self.lauf <= 12.9:
                        self.notelauf = 3
                    elif 12.9 < self.lauf <= 13.5:
                        self.notelauf = 4
                    elif 13.5 < self.lauf <= 14.5:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.lauf <= 11.8:
                        self.notelauf = 1
                    elif 11.8 < self.lauf <= 12.8:
                        self.notelauf = 2
                    elif 12.8 < self.lauf <= 13.6:
                        self.notelauf = 3
                    elif 13.6 < self.lauf <= 14.0:
                        self.notelauf = 4
                    elif 14.0 < self.lauf <= 14.8:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
            elif self.stufe == 8:
                if self.geschlecht == "männlich": #erledigt
                    if self.lauf <= 10.6:
                        self.notelauf = 1
                    elif 10.6 < self.lauf <= 11.5:
                        self.notelauf = 2
                    elif 11.5 < self.lauf <= 12.4:
                        self.notelauf = 3
                    elif 12.4 < self.lauf <= 13:
                        self.notelauf = 4
                    elif 13 < self.lauf <= 13.8:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.lauf <= 11.7:
                        self.notelauf = 1
                    elif 11.7 < self.lauf <= 12.7:
                        self.notelauf = 2
                    elif 12.7 < self.lauf <= 13.3:
                        self.notelauf = 3
                    elif 13.3 < self.lauf <= 13.8:
                        self.notelauf = 4
                    elif 13.8 < self.lauf <= 14.5:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
            elif self.stufe == 9:
                if self.geschlecht == "männlich": #erledigt
                    if self.lauf <= 13.3:
                        self.notelauf = 1
                    elif 13.3 < self.lauf <= 14.2:
                        self.notelauf = 2
                    elif 14.2 < self.lauf <= 15.3:
                        self.notelauf = 3
                    elif 15.3 < self.lauf <= 16.4:
                        self.notelauf = 4
                    elif 16.4 < self.lauf <= 17.9:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.lauf <= 15.0:
                        self.notelauf = 1
                    elif 15.0 < self.lauf <= 16.1:
                        self.notelauf = 2
                    elif 16.1 < self.lauf <= 17.2:
                        self.notelauf = 3
                    elif 17.2 < self.lauf <= 18.3:
                        self.notelauf = 4
                    elif 18.3 < self.lauf <= 19.7:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
            elif self.stufe == 10:
                if self.geschlecht == "männlich": #erledigt
                    if self.lauf <= 13.0:
                        self.notelauf = 1
                    elif 13.0 < self.lauf <= 13.6:
                        self.notelauf = 2
                    elif 13.6 < self.lauf <= 14.5:
                        self.notelauf = 3
                    elif 14.5 < self.lauf <= 15.6:
                        self.notelauf = 4
                    elif 15.6 < self.lauf <= 16.9:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.lauf <= 14.9:
                        self.notelauf = 1
                    elif 14.9 < self.lauf <= 16.0:
                        self.notelauf = 2
                    elif 16.0 < self.lauf <= 17.0:
                        self.notelauf = 3
                    elif 17.0 < self.lauf <= 18.1:
                        self.notelauf = 4
                    elif 18.1 < self.lauf <= 19.4:
                        self.notelauf = 5
                    else:
                        self.notelauf = 6
        self.save()

    def getNotelauf(self):
        return self.notelauf

    def setSprung(self, sprung1, sprung2, sprung3):
        self.sprung1 = sprung1
        self.sprung2 = sprung2
        self.sprung3 = sprung3
        self.save()

    def getSprung(self):
        return [self.sprung1, self.sprung2, self.sprung3]

    def setBestsprung(self):
        spr = []
        for wert in self.getSprung():
            if wert is not None:
                spr.append(wert)
        if len(spr) != 0:
            self.bestsprung = max(spr)
        self.save()

    def getBestsprung(self):
        return self.bestsprung

    def setPunktesprung(self):
        if self.bestsprung is not None:
            if self.geschlecht == "männlich":
                self.punktesprung = int((math.sqrt(self.bestsprung)-1.15028)/0.00219)
            elif self.geschlecht == "weiblich":
                self.punktesprung = int((math.sqrt(self.bestsprung)-1.0935)/0.00208)
        self.save()

    def getPunktesprung(self):
        return self.punktesprung

    def setNotesprung(self):
        if self.bestsprung is not None:
            if self.stufe == 5:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestsprung >= 3.7:
                        self.notesprung = 1
                    elif 3.7 > self.bestsprung >= 3.26:
                        self.notesprung = 2
                    elif 3.26 > self.bestsprung >= 2.90:
                        self.notesprung = 3
                    elif 2.90 > self.bestsprung >= 2.67:
                        self.notesprung = 4
                    elif 2.67 > self.bestsprung >= 2.25:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestsprung >= 3.38:
                        self.notesprung = 1
                    elif 3.38 > self.bestsprung >= 2.90:
                        self.notesprung = 2
                    elif 2.90 > self.bestsprung >= 2.63:
                        self.notesprung = 3
                    elif 2.63 > self.bestsprung >= 2.40:
                        self.notesprung = 4
                    elif 2.40 > self.bestsprung >= 2.10:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
            elif self.stufe == 6:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestsprung >= 3.74:
                        self.notesprung = 1
                    elif 3.74 > self.bestsprung >= 3.37:
                        self.notesprung = 2
                    elif 3.37 > self.bestsprung >= 3.00:
                        self.notesprung = 3
                    elif 3.00 > self.bestsprung >= 2.75:
                        self.notesprung = 4
                    elif 2.75 > self.bestsprung >= 2.35:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
                elif self.geschlecht == "weiblich": # erledigt
                    if self.bestsprung >= 3.49:
                        self.notesprung = 1
                    elif 3.49 > self.bestsprung >= 3.10:
                        self.notesprung = 2
                    elif 3.10 > self.bestsprung >= 2.75:
                        self.notesprung = 3
                    elif 2.75 > self.bestsprung >= 2.58:
                        self.notesprung = 4
                    elif 2.58 > self.bestsprung >= 2.21:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
            elif self.stufe == 7:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestsprung >= 3.98:
                        self.notesprung = 1
                    elif 3.98 > self.bestsprung >= 3.51:
                        self.notesprung = 2
                    elif 3.51 > self.bestsprung >= 3.15:
                        self.notesprung = 3
                    elif 3.15 > self.bestsprung >= 2.85:
                        self.notesprung = 4
                    elif 2.85 > self.bestsprung >= 2.51:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestsprung >= 3.70:
                        self.notesprung = 1
                    elif 3.70 > self.bestsprung >= 3.35:
                        self.notesprung = 2
                    elif 3.35 > self.bestsprung >= 3.05:
                        self.notesprung = 3
                    elif 3.05 > self.bestsprung >= 2.72:
                        self.notesprung = 4
                    elif 2.72 > self.bestsprung >= 2.32:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
            elif self.stufe == 8:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestsprung >= 4.37:
                        self.notesprung = 1
                    elif 4.37 > self.bestsprung >= 3.80:
                        self.notesprung = 2
                    elif 3.80 > self.bestsprung >= 3.32:
                        self.notesprung = 3
                    elif 3.32 > self.bestsprung >= 3.04:
                        self.notesprung = 4
                    elif 3.04 > self.bestsprung >= 2.70:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
                elif self.geschlecht == "weiblich":
                    if self.bestsprung >= 3.73:
                        self.notesprung = 1
                    elif 3.73 > self.bestsprung >= 3.42:
                        self.notesprung = 2
                    elif 3.42 > self.bestsprung >= 3.10:
                        self.notesprung = 3
                    elif 3.10 > self.bestsprung >= 2.75:
                        self.notesprung = 4
                    elif 2.75 > self.bestsprung >= 2.37:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
            elif self.stufe == 9:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestsprung >= 4.80:
                        self.notesprung = 1
                    elif 4.80 > self.bestsprung >= 4.08:
                        self.notesprung = 2
                    elif 4.08 > self.bestsprung >= 3.55:
                        self.notesprung = 3
                    elif 3.55 > self.bestsprung >= 3.32:
                        self.notesprung = 4
                    elif 3.32 > self.bestsprung >= 2.91:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestsprung >= 3.75:
                        self.notesprung = 1
                    elif 3.75 > self.bestsprung >= 3.52:
                        self.notesprung = 2
                    elif 3.52 > self.bestsprung >= 3.12:
                        self.notesprung = 3
                    elif 3.12 > self.bestsprung >= 2.84:
                        self.notesprung = 4
                    elif 2.84 > self.bestsprung >= 2.40:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
            elif self.stufe == 10:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestsprung >= 5.02:
                        self.notesprung = 1
                    elif 5.02 > self.bestsprung >= 4.48:
                        self.notesprung = 2
                    elif 4.48 > self.bestsprung >= 3.73:
                        self.notesprung = 3
                    elif 3.73 > self.bestsprung >= 3.53:
                        self.notesprung = 4
                    elif 3.53 > self.bestsprung >= 3.10:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestsprung >= 3.92:
                        self.notesprung = 1
                    elif 3.92 > self.bestsprung >= 3.60:
                        self.notesprung = 2
                    elif 3.60 > self.bestsprung >= 3.15:
                        self.notesprung = 3
                    elif 3.15 > self.bestsprung >= 2.86:
                        self.notesprung = 4
                    elif 2.86 > self.bestsprung >= 2.49:
                        self.notesprung = 5
                    else:
                        self.notesprung = 6
        self.save()

    def getNotesprung(self):
        return self.notesprung

    def setWurfstoss(self, wurfstoss1, wurfstoss2, wurfstoss3):
        self.wurfstoss1 = wurfstoss1
        self.wurfstoss2 = wurfstoss2
        self.wurfstoss3 = wurfstoss3
        self.save()

    def getWurfstoss(self):
        return [self.wurfstoss1, self.wurfstoss2, self.wurfstoss3]


    def setBestwurfstoss(self):
        wst = []
        for wert in self.getWurfstoss():
            if wert is not None:
                wst.append(wert)
        if len(wst) != 0:
            self.bestwurfstoss = max(wst)
        self.save()

    def getBestwurfstoss(self):
        return self.bestwurfstoss

    def setPunktewurfstoss(self):
        if self.bestwurfstoss is not None:
            if self.stufe in [5, 6, 7]:
                if self.geschlecht == "männlich":
                    self.punktewurfstoss = int((math.sqrt(self.bestwurfstoss) - 1.936)/0.0124)
                elif self.geschlecht == "weiblich":
                    self.punktewurfstoss = int((math.sqrt(self.bestwurfstoss)-1.4149)/0.01039)
            elif self.stufe in [8, 9, 10]:
                if self.geschlecht == "männlich":
                    self.punktewurfstoss = int((math.sqrt(self.bestwurfstoss) - 1.425) / 0.0037)
                elif self.geschlecht == "weiblich":
                    self.punktewurfstoss = int((math.sqrt(self.bestwurfstoss) - 1.279) / 0.00398)
        self.save()

    def getPunktewurfstoss(self):
        return self.punktewurfstoss


    def setNotewurfstoss(self):
        if self.bestwurfstoss is not None:
            if self.stufe == 5:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestwurfstoss >= 37.0:
                        self.notewurfstoss = 1
                    elif 37.0 > self.bestwurfstoss >= 31.0:
                        self.notewurfstoss = 2
                    elif 31.0 > self.bestwurfstoss >= 24.5:
                        self.notewurfstoss = 3
                    elif 24.5 > self.bestwurfstoss >= 21.5:
                        self.notewurfstoss = 4
                    elif 21.5 > self.bestwurfstoss >= 17.0:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestwurfstoss >= 25.0:
                        self.notewurfstoss = 1
                    elif 25.0 > self.bestwurfstoss >= 20.5:
                        self.notewurfstoss = 2
                    elif 20.5 > self.bestwurfstoss >= 15.5:
                        self.notewurfstoss = 3
                    elif 15.5 > self.bestwurfstoss >= 12.5:
                        self.notewurfstoss = 4
                    elif 12.5 > self.bestwurfstoss >= 9.5:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
            elif self.stufe == 6:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestwurfstoss >= 42.0:
                        self.notewurfstoss = 1
                    elif 42.0 > self.bestwurfstoss >= 34.5:
                        self.notewurfstoss = 2
                    elif 34.5 > self.bestwurfstoss >= 27.0:
                        self.notewurfstoss = 3
                    elif 27.0 > self.bestwurfstoss >= 24.0:
                        self.notewurfstoss = 4
                    elif 24.0 > self.bestwurfstoss >= 19.0:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestwurfstoss >= 27.5:
                        self.notewurfstoss = 1
                    elif 27.5 > self.bestwurfstoss >= 22.5:
                        self.notewurfstoss = 2
                    elif 22.5 > self.bestwurfstoss >= 17.5:
                        self.notewurfstoss = 3
                    elif 17.5 > self.bestwurfstoss >= 14.5:
                        self.notewurfstoss = 4
                    elif 14.5 > self.bestwurfstoss >= 11.0:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
            elif self.stufe == 7:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestwurfstoss >= 45.0:
                        self.notewurfstoss = 1
                    elif 45.0 > self.bestwurfstoss >= 36.0:
                        self.notewurfstoss = 2
                    elif 36.0 > self.bestwurfstoss >= 30.5:
                        self.notewurfstoss = 3
                    elif 30.5 > self.bestwurfstoss >= 27.0:
                        self.notewurfstoss = 4
                    elif 27.0 > self.bestwurfstoss >= 22.5:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestwurfstoss >= 30.0:
                        self.notewurfstoss = 1
                    elif 30.0 > self.bestwurfstoss >= 24.0:
                        self.notewurfstoss = 2
                    elif 24.0 > self.bestwurfstoss >= 18.0:
                        self.notewurfstoss = 3
                    elif 18.0 > self.bestwurfstoss >= 16.5:
                        self.notewurfstoss = 4
                    elif 16.5 > self.bestwurfstoss >= 13.0:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
            elif self.stufe == 8:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestwurfstoss >= 8.6:
                        self.notewurfstoss = 1
                    elif 8.6 > self.bestwurfstoss >= 7.6:
                        self.notewurfstoss = 2
                    elif 7.6 > self.bestwurfstoss >= 6.5:
                        self.notewurfstoss = 3
                    elif 6.5 > self.bestwurfstoss >= 5.7:
                        self.notewurfstoss = 4
                    elif 5.7 > self.bestwurfstoss >= 4.8:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestwurfstoss >= 7.3:
                        self.notewurfstoss = 1
                    elif 7.3 > self.bestwurfstoss >= 6.4:
                        self.notewurfstoss = 2
                    elif 6.4 > self.bestwurfstoss >= 5.6:
                        self.notewurfstoss = 3
                    elif 5.6 > self.bestwurfstoss >= 5.0:
                        self.notewurfstoss = 4
                    elif 5.0 > self.bestwurfstoss >= 4.3:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
            elif self.stufe == 9:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestwurfstoss >= 9.3:
                        self.notewurfstoss = 1
                    elif 9.3 > self.bestwurfstoss >= 8.5:
                        self.notewurfstoss = 2
                    elif 8.5 > self.bestwurfstoss >= 7.7:
                        self.notewurfstoss = 3
                    elif 7.7 > self.bestwurfstoss >= 7.0:
                        self.notewurfstoss = 4
                    elif 7.0 > self.bestwurfstoss >= 5.8:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestwurfstoss >= 7.5:
                        self.notewurfstoss = 1
                    elif 7.5 > self.bestwurfstoss >= 6.6:
                        self.notewurfstoss = 2
                    elif 6.6 > self.bestwurfstoss >= 5.8:
                        self.notewurfstoss = 3
                    elif 5.8 > self.bestwurfstoss >= 5.3:
                        self.notewurfstoss = 4
                    elif 5.3 > self.bestwurfstoss >= 4.8:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
            elif self.stufe == 10:
                if self.geschlecht == "männlich": #erledigt
                    if self.bestwurfstoss >= 9.9:
                        self.notewurfstoss = 1
                    elif 9.9 > self.bestwurfstoss >= 9.0:
                        self.notewurfstoss = 2
                    elif 9.0 > self.bestwurfstoss >= 8.1:
                        self.notewurfstoss = 3
                    elif 8.1 > self.bestwurfstoss >= 7.6:
                        self.notewurfstoss = 4
                    elif 7.6 > self.bestwurfstoss >= 6.8:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
                elif self.geschlecht == "weiblich": #erledigt
                    if self.bestwurfstoss >= 7.6:
                        self.notewurfstoss = 1
                    elif 7.6 > self.bestwurfstoss >= 6.7:
                        self.notewurfstoss = 2
                    elif 6.7 > self.bestwurfstoss >= 6.0:
                        self.notewurfstoss = 3
                    elif 6.0 > self.bestwurfstoss >= 5.6:
                        self.notewurfstoss = 4
                    elif 5.6 > self.bestwurfstoss >= 5.0:
                        self.notewurfstoss = 5
                    else:
                        self.notewurfstoss = 6
        self.save()

    def getNotewurfstoss(self):
        return self.notewurfstoss

    def setPunktemehrkampf(self):
        p = []
        if self.punktelauf is not None:
            p.append(self.punktelauf)
        if self.punktesprung is not None:
            p.append(self.punktesprung)
        if self.punktewurfstoss is not None:
            p.append(self.punktewurfstoss)
        if len(p) > 0:
            self.punktemehrkampf = sum(p)
        self.save()

    def getPunktemehrkampf(self):
        return self.punktemehrkampf

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
        self.save()

    def __init__(self, schnr, nname, vname, klasse, stufe, geschlecht):
        self.setSchnr(schnr)
        self.setNname(nname)
        self.setVname(vname)
        self.setKlasse(klasse)
        self.setStufe(stufe)
        self.setGeschlecht(geschlecht)
        self.save()

