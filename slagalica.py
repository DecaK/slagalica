import eel
import random

igraci = {
    "xawfloawfwafaw": "Marko",
    "awfpogkawgawga": "Sava"
}

igraci = {}
slova = 'abcčdefghijklmnoprsštuvzž'
slovaZaIgru = ''.join(random.choice(slova) for i in range(12))
with open('words', encoding='utf8') as f:
    availableWords = f.readlines()

eel.init("web")

@eel.expose
def ubaci_igraca(ime):
    global igraci
    random_auth = random.randint(1, 500000)
    if random_auth not in igraci:
        igraci[random_auth] = Igrac(ime, 0, '', '', False)
    else:
        igraci[random_auth] = 'kurac'
    print(random_auth)
    return random_auth

@eel.expose
def get_slova():
    print(slovaZaIgru)
    return slovaZaIgru

@eel.expose
def submit_word(auth, word):
    print(len(word))
    if auth not in igraci:
        return False
    igrac = igraci[auth]
    if validate_word(word, slova):
        igrac.set_rec(word)
        return True
    print('{} je submit rec "{}"'.format(igrac, word))
    return False

@eel.expose
def dodeli_poene_rec(igrac1, igrac2):
    igraci[igrac1].set_points(len(igraci[igrac1].get_rec()))
    igraci[igrac2].set_points(len(igraci[igrac2].get_rec()))

@eel.expose
def get_poeni(auth):
    return igraci[auth].get_points()

def validate_word(word, slova):
    supposed_len = len(slova) - len(word)
    for i in word:
        slova = slova.replace(i, '', 1)
    return len(slova) == supposed_len and word+'\n' in availableWords

igrac1_poeni = 0
igrac2_poeni = 0
igrac1_rec = ''
igrac2_rec = ''
igrac1_brojresenje = ''
igrac2_brojresenje = ''

class Igrac(object):
    def __init__(self, ime, points, rec, broj, ready):
        self.ime = ime
        self.points = points
        self.rec = rec
        self.broj = broj
        self.ready = ready
    def get_points(self):
        return self.points
    def get_ime(self):
        return self.ime
    def get_broj(self):
        return self.broj
    def get_ready(self):
        return self.ready
    def get_rec(self):
        return self.rec
    def set_ready(self, ready):
        self.ready = ready
    def set_points(self, points):
        self.points = points
    def set_rec(self, rec):
        self.rec = rec
    def set_broj(self, broj):
        self.broj = broj

#@eel.expose
#def posalji_rec(igrac, rec):

#@eel.expose
#def check_for_update():

eel.start('index.html', port=8444)
