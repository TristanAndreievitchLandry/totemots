import copy
import random
import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

lcd_columns = 16
lcd_rows = 2

i2c = busio.I2C(board.SCL, board.SDA)

lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()

def a():
    lcd.message = "On m\'appelle\nbouleau"
    time.sleep(2)
    lcd.clear()
    lcd.message ="a cause de\nl\'ecorce"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de mon coeur"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je raconte au\nvent"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les racines\nde la vie."
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je couvre de\nplumes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la memoire\ndes ancetres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je dechire tes\nmots de glaise"
    time.sleep(2)
    lcd.clear()
    lcd.message = "quand tu\nchantes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "mon pays"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Tu ne dis\npas que je"
    time.sleep(2)
    lcd.clear()
    lcd.message = "chassais la"
    time.sleep(2)
    lcd.clear()
    lcd.message = "quand tu\nparles de la"
    time.sleep(2)
    lcd.clear()
    lcd.message = "quand tu\nparles de la"
    time.sleep(2)
    lcd.clear()
    lcd.message = "route de\nl\'Inde"
    time.sleep(2)
    lcd.clear()
    lcd.message = "J\'ai la seve de\nl\'arbre comme"
    time.sleep(2)
    lcd.clear()
    lcd.message = "une liqueur\nd\'histoire"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Jean Sioui"
    time.sleep(5)
    lcd.clear()

def c():
    lcd.message = "Espoir que tu\nnous sois feroce"
    time.sleep(2)
    lcd.clear()
    lcd.message ="histoire je te\ndedie"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la derniere de\nmes chansons"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la terre est\nsoeur"
    time.sleep(2)
    lcd.clear()
    lcd.message ="avec la mer" 
    time.sleep(2)
    lcd.clear()
    lcd.message = "je suis l\'epouse\nadultere"
    time.sleep(2)
    lcd.clear()
    lcd.message = "du\nfleuve"
    time.sleep(2)
    lcd.clear()
    lcd.message = "j\'ai quitte\nloin mon pays"
    time.sleep(2)
    lcd.clear()
    lcd.message = "ou mes pieds\nse baignent" 
    time.sleep(2)
    lcd.clear()
    lcd.message = "du repos des\nancetres"
    time.sleep(2)
    lcd.clear() 
    lcd.message = "de l\'ecume qui\nme sert de savon"
    time.sleep(2)
    lcd.clear()
    lcd.message ="sans javel"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Natasha Kanape\nFontaine"
    time.sleep(5)
    lcd.clear()

def d():
    lcd.message = "Et si\nje saccageais"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les portes des\nplans nord"
    time.sleep(2)
    lcd.clear()
    lcd.message = "faisais dechoir\nles ruines"
    time.sleep(2)
    lcd.clear()
    lcd.message = "degrafais\nla terre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "des ancetres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "il n\'y aurait\nplus de pays"
    time.sleep(2)
    lcd.clear()
    lcd.message = "il y aurait moi\net ma mere"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et ma soeur\net mon frere"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et mon pere\net les autres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et les autres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Natasha Kanape\nFontaine"
    time.sleep(5)
    lcd.clear()

def e():
    lcd.message = "Je presenterai\nun feu immense"
    time.sleep(2)
    lcd.clear()
    lcd.message = "je brulerai\nles ecoles"
    time.sleep(2)
    lcd.clear()
    lcd.message = "residences"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les papiers lois"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Et d\'un seul\ncoup de vent"
    time.sleep(2)
    lcd.clear()
    lcd.message = "chasserai\nd\'une main"
    time.sleep(2)
    lcd.clear()
    lcd.message = "tous\nles pipelines"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les caribous\nviendront"
    time.sleep(2)
    lcd.clear()
    lcd.message = "courir\navec les bisons"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les chevaux\nles cerfs"
    time.sleep(2)
    lcd.clear()
    lcd.message = "il y aura\nun grand" 
    time.sleep(2)
    lcd.clear()
    lcd.message = "fremissement"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Les caribous\nles visons"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les chevaux"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les cerfs\nviendront"
    time.sleep(2)
    lcd.clear()
    lcd.message = "noyer\nles oleoducs"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Nous brulerons"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les ecoles"
    time.sleep(2)
    lcd.clear()
    lcd.message = "residences"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les papiers lois"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Nous incarnerons\nun feu immense."
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Natasha Kanape\nFontaine"
    time.sleep(5)
    lcd.clear()

def f():
    lcd.message = "Qui parsemait"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les champs\ndes cieux?"
    time.sleep(2)
    lcd.clear()
    lcd.message = "un immuable\nespoir"
    time.sleep(2)
    lcd.clear()
    lcd.message = "s\'ebranle"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les bitumes et\nles pieds cornus"
    time.sleep(2)
    lcd.clear()
    lcd.message = "J\'ai une terre\na mourir"
    time.sleep(2)
    lcd.clear()
    lcd.message = "avec les\nprairies"
    time.sleep(2)
    lcd.clear()
    lcd.message = "magnetiques"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les hauts bles\ncarabines"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les eaux blondes\ntoxiques"
    time.sleep(2)
    lcd.clear()
    lcd.message = "ou mes jupes\nse suspendent"
    time.sleep(2)
    lcd.clear()
    lcd.message = "ou mes crinieres\ns'eprennent"
    time.sleep(2)
    lcd.clear()
    lcd.message = "ou ma colere\nse pend."
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Natasha Kanape\nFontaine"
    time.sleep(5)
    lcd.clear()

def g():
    lcd.message = "La culture\nconsole"
    time.sleep(2)
    lcd.clear()
    lcd.message = "l\'ecchymose\ndu fleuve"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Le mazout boit\nl\'eau"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Montreal\ndistinguait"
    time.sleep(2)
    lcd.clear()
    lcd.message = "le chant"
    time.sleep(2)
    lcd.clear()
    lcd.message = "des outardes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "oseront-elles\nrevenir?"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Natasha Kanape\nFontaine"
    time.sleep(5)
    lcd.clear()

def h():
    lcd.message = "J\'ai pleure,\npleure la deesse"
    time.sleep(2)
    lcd.clear()
    lcd.message = "ils construisent\npartout"
    time.sleep(2)
    lcd.clear()
    lcd.message = "des pipelines"
    time.sleep(2)
    lcd.clear()
    lcd.message ="ils oublient"
    time.sleep(2)
    lcd.clear()
    lcd.message = "on s'appellera\nbois de petrole"
    time.sleep(2)
    lcd.clear()
    lcd.message = "vagin javel"
    time.sleep(2)
    lcd.clear()
    lcd.message ="tu veux mon\npipeline"
    time.sleep(2)
    lcd.clear()
    lcd.message = "dans ta bouche?"
    time.sleep(2)
    lcd.clear()
    lcd.message = "diraient\nles autres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Si ce n\'est\npas moi"
    time.sleep(2)
    lcd.clear()
    lcd.message = "oui j\'irai\nmanger Enbridge"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et tous\nles autres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "sales carboneux"
    time.sleep(2)
    lcd.clear()
    lcd.message = "parce que\nj'ai famine"
    time.sleep(2)
    lcd.clear()
    lcd.message = "parce que j'ai\nfamine de vivre."
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Natasha Kanape\nFontaine"
    time.sleep(5)
    lcd.clear()

def i():
    lcd.message = "Ma foret pleure\ntoute seule"
    time.sleep(2)
    lcd.clear()
    lcd.message = "en silence"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et les rivieres\net les lacs"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et les etres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et les esprits."
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Natasha Kanape\nFontaine"
    time.sleep(5)
    lcd.clear()

def j():
    lcd.message = "Missinaku\nm\'abreuve"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Papakassiku\ncourt avec moi"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Le lichen\nme nourrit"
    time.sleep(2)
    lcd.clear()
    lcd.message = "La mousse soigne\nmes larmes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def k():
    lcd.message = "Les genoux\nabimes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "J\'arrive a toi"
    time.sleep(2)
    lcd.clear()
    lcd.message = "La solitude ne\nm\'effraie pas"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Mes perches\nsont la"
    time.sleep(2)
    lcd.clear()
    lcd.message = "a m\'attendre\nsur ton lichen"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def l():
    lcd.message = "Nous partageons\nUn the"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Dans la Toundra\nUn reconfort"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Face a l\'infini"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def m():
    lcd.message = "Une tendresse"
    time.sleep(2)
    lcd.clear()
    lcd.message = " pour\nun pas de danse"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Une salle\nde bal"
    time.sleep(2)
    lcd.clear()
    lcd.message = "tapissee\nde lichens"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Et de\nconstellations"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Dessine\nmon infini"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def n():
    lcd.message = "Toundra"
    time.sleep(2)
    lcd.clear()
    lcd.message = " Tu as vu naitre\nma famille"
    time.sleep(2)
    lcd.clear()
    lcd.message = "J\'ecoute\nton coeur"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Le tambour\nrythme ma vie"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def o():
    lcd.message = "Septembre,"
    time.sleep(2)
    lcd.clear()
    lcd.message = " je pars\navec mes parents"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Sur\nle territoire"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je suis\nle saumon"
    time.sleep(2)
    lcd.clear()
    lcd.message = "qui remonte\nles chutes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Et fraie\nles eaux"
    time.sleep(2)
    lcd.clear()
    lcd.message = "pour\nla pondaison"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def p():
    lcd.message = "Je levite"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Mes pas se\nlaissent porter"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Sur le lichen\nqui nourrit"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Papakassiku"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Les fleurs\nse transforment"
    time.sleep(2)
    lcd.clear()
    lcd.message = "en de petites\nbaies"
    time.sleep(2)
    lcd.clear()
    lcd.message = "aux couleurs\nrouges, jaunes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def q():
    lcd.message = "Je ne suis pas"
    time.sleep(2)
    lcd.clear()
    lcd.message = "l\'errante\nde la ville"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je suis\nla nomade"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de la Toundra"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def r():
    lcd.message = "L\'odeur du the"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de la Toundra\nm\'enivre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Il me tend une\ntasse d\'ecorce"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Mon etre\nse rechauffe"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Toundra,\ntu me gates"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def s():
    lcd.message = "Tout est calme\ndans la Toundra"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Le silence est\nvrai"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Les bulldozers"
    time.sleep(2)
    lcd.clear()
    lcd.message = "ne crachent plus\nleur fiel"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je suis seule\navec ma priere"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def t():
    lcd.message = "Aujourd\'hui\nle printemps"
    time.sleep(2)
    lcd.clear()
    lcd.message = "s\'est mele\na l\'hiver"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Tout fond"
    time.sleep(2)
    lcd.clear()
    lcd.message = "L\'hiver\nn\'a pas dit"
    time.sleep(2)
    lcd.clear()
    lcd.message = "son dernier mot"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def u():
    lcd.message = "Les aurores\nboreales"
    time.sleep(2)
    lcd.clear()
    lcd.message = "dansent\nles gestes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de la terre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "C\'est la nuit\ndes cicatrices"
    time.sleep(2)
    lcd.clear()
    lcd.message = "qui pardonnent"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def v():
    lcd.message = "Ma terre est\nbafouee"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Par un serpent\nvenimeux"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Ou coule\nmon histoire"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def w():
    lcd.message = "Tu parles\nd\'etoiles"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je te parle\nde rivieres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Tu parles\nd\'astres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je te parle\nde lacs"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Tu parles\nde l\'infini"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je te parle\nde la toundra"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Tu parles\nd\'anges"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je te parle"
    time.sleep(2)
    lcd.clear()
    lcd.message = "d\'aurores\nboreales"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Tu parles\ndes cieux"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Je te parle\nde la terre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def x():
    lcd.message = "Dans le cercle\ncrepitent"
    time.sleep(2)
    lcd.clear()
    lcd.message ="les braises\nde l\'offrande"
    time.sleep(2)
    lcd.clear()
    lcd.message = "quelques\nfeuilles"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de tabac\naffranchies"
    time.sleep(2)
    lcd.clear()
    lcd.message = "d\'une main\nde pierre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Louis-Karl\nPicard-Sioui"
    time.sleep(5)
    lcd.clear()

def y():
    lcd.message = "Cette histoire\nexpire"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les distances"
    time.sleep(2)
    lcd.clear()
    lcd.message = "retire"
    time.sleep(2)
    lcd.clear()
    lcd.message ="ses branches et\nses racines"
    time.sleep(2)
    lcd.clear()
    lcd.message = "l\'une apres\nl\'autre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "d\'hier\na peut-etre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Louis-Karl\nPicard-Sioui"
    time.sleep(5)
    lcd.clear()

def z():
    lcd.message = "Deux ames\nentremelees"
    time.sleep(2)
    lcd.clear()
    lcd.message ="s\'embrassant"
    time.sleep(2)
    lcd.clear()
    lcd.message ="pres d\'un feu de \nbroussaille"
    time.sleep(2)
    lcd.clear()
    lcd.message = "deux ames gisant\npres d\'une terre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "a pourfendre\ncomme le ciel"
    time.sleep(2)
    lcd.clear()
    lcd.message = "ameutant son\ncoeur de ciel"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et le lac\nseul temoin"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Louis-Karl\nPicard-Sioui"
    time.sleep(5)
    lcd.clear()

def aa():
    lcd.message = "Le vent et\nla mer"
    time.sleep(2)
    lcd.clear()
    lcd.message ="la route et\nla riviere"
    time.sleep(2)
    lcd.clear()
    lcd.message = "comblent tes\nambitions"
    time.sleep(2)
    lcd.clear()
    lcd.message = "sous le soleil\ncouchant"
    time.sleep(2)
    lcd.clear()
    lcd.message = "crepite un\ntresor nouveau"
    time.sleep(2)
    lcd.clear()
    lcd.message = "a cueillir\na palir"
    time.sleep(2)
    lcd.clear()
    lcd.message = "ces racines m\'ancrent\na cette terre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "mon souffle\nnourrit"
    time.sleep(2)
    lcd.clear()
    lcd.message = "l\'automne\nen feuilles"
    time.sleep(2)
    lcd.clear()
    lcd.message = "c\'est toi\ndiaphane"
    time.sleep(2)
    lcd.clear()
    lcd.message = "qui peint\nl\'horizon"
    time.sleep(2)
    lcd.clear()
    lcd.message = "c\'est toi\nla-bas"
    time.sleep(2)
    lcd.clear()
    lcd.message = "tu y es\ndeja"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Louis-Karl\nPicard-Sioui"
    time.sleep(5)
    lcd.clear()

def bb():
    lcd.message = "L\'amour c\'est"
    time.sleep(2)
    lcd.clear()
    lcd.message ="une foret\nvierge"
    time.sleep(2)
    lcd.clear()
    lcd.message = "pis..."
    time.sleep(2)
    lcd.clear()
    lcd.message = "une coupe\na blanc"
    time.sleep(2)
    lcd.clear()
    lcd.message = "dans la meme\nphrase."
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(5)
    lcd.clear()

def cc():
    lcd.message = "T\'es la talle\nd\'epinettes"
    time.sleep(2)
    lcd.clear()
    lcd.message ="noires qui brule\nmon coeur"
    time.sleep(2)
    lcd.clear()
    lcd.message = "full de super"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(5)
    lcd.clear()

def dd():
    lcd.message = "Les erablieres\ndans les coulees"
    time.sleep(2)
    lcd.clear()
    lcd.message ="l\'ombre des\ncrans"
    time.sleep(2)
    lcd.clear()
    lcd.message ="sur les\nmontagnes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(5)
    lcd.clear()

def ee():
    lcd.message = "J\'ai voulu\napprendre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "a lire\nta riviere"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(5)
    lcd.clear()

def ff():
    lcd.message = "C\'est dans\nun lit"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de sapinage\nqu\'on a touche"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la beaute\nsourde-muette"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de l\'ephemere" 
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(5)
    lcd.clear()

def gg():
    lcd.message = "Que tu puisses\nvoir"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les fleurs\nsauvages"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de mon coeur cru,\nla medecine"
    time.sleep(2)
    lcd.clear()
    lcd.message = "millenaire qui\nnous enveloppe"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(5)
    lcd.clear()

def hh():
    lcd.message = "Le dehors est\nla seule reponse"
    time.sleep(2)
    lcd.clear()
    lcd.message = "que j\'ai trouve\nau dedans"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(5)
    lcd.clear()

def ii():
    lcd.message = "Je peux aussi\ncourir apres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les orignaux"
    time.sleep(2)
    lcd.clear()
    lcd.message ="et ecouter"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la poesie\npas compliquee"
    time.sleep(2)
    lcd.clear()
    lcd.message = "des faux-trembles"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(5)
    lcd.clear()

def jj():
    lcd.message = "C\'est dans\nle sacre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "d\'un lever\nde soleil"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la musique de \nnos\nanimaux"
    time.sleep(2)
    lcd.clear()
    lcd.message ="rescapes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Marie-Andree\nGill"
    time.sleep(2)
    lcd.clear()
    time.sleep(5)
    lcd.clear()

def kk(): 
    lcd.message = "Je depose\ndu tabac"
    time.sleep(2)
    lcd.clear()
    lcd.message = "en offrande\nsur une pierre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def ll():
    lcd.message = "Un air\nme rappelle"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la verte\nToundra"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def mm():
    lcd.message = "Le lichen\nme nourrit"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la mousse soigne\nmes larmes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def nn():
    lcd.message = "Tu retournes\nsur une terre"
    time.sleep(2)
    lcd.clear()
    lcd.message = "qui te respecte"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def oo():
    lcd.message = "J\'arrive enfin"
    time.sleep(2)
    lcd.clear()
    lcd.message = "a la terre\nqui espere" 
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def pp():
    lcd.message = "Cueillir le\nchampignon"
    time.sleep(2)
    lcd.clear()
    lcd.message = "qui preserve\nle feu"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def qq():
    lcd.message = "L\'echo fredonne\nune incantation"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Papakassik\nl\'entend"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def rr():
    lcd.message = "Je suis libre\ndans les eaux"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de Missinak"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def ss():
    lcd.message = "Sur le lichen\nqui nourrit"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Papakassik"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Les fleurs se\ntransforment"
    time.sleep(2)
    lcd.clear()
    lcd.message = "en de petites\nbaies"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def tt():
    lcd.message = "Je suis\nle saumon"
    time.sleep(2)
    lcd.clear()
    lcd.message = "qui remonte\nles chutes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et fraie\nles eaux"
    time.sleep(2)
    lcd.clear()
    lcd.message = "pour la\npondaison"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def uu():
    lcd.message = "Enfant de\nla Toundra"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Resonne\nmon coeur"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def vv():
    lcd.message = "Lentement"
    time.sleep(2)
    lcd.clear()
    lcd.message = "je fais le tour\ndu lac"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Une truite grise\nme devisage"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def ww():
    lcd.message = "J\'ai pagaye pour\nte rencontrer"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def xx():
    lcd.message = "Grand-pere ours"
    time.sleep(2)
    lcd.clear()
    lcd.message = "s\'en est alle\ndormir"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Le rouge de ses\nairelles"
    time.sleep(2)
    lcd.clear()
    lcd.message = "accompagne\nsa retraite"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Josephine\nBacon"
    time.sleep(5)
    lcd.clear()

def yy():
    lcd.message ="Si tu vois"
    time.sleep(2)
    lcd.clear()
    lcd.message = "un champ\nen friche"
    time.sleep(2)
    lcd.clear()
    lcd.message = "herisse de"
    time.sleep(2)
    lcd.clear()
    lcd.message = "vielles\ncultures"
    time.sleep(2)
    lcd.clear()
    lcd.message = "souffle sur\nles aigrettes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de la fleur\nla plus modeste"
    time.sleep(2)
    lcd.clear()
    lcd.message ="regarde le ciel\npasser du noir"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de confettis au\nbleu de l\'Est" 
    time.sleep(2)
    lcd.clear()
    lcd.message = "c\'est alors que\nle champ"
    time.sleep(2)
    lcd.clear()
    lcd.message ="se couvre de\nlumiere fleurie"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Christine Sioui\nWawanoloath"
    time.sleep(5)
    lcd.clear()

def zz():
    lcd.message ="L\'odeur\nde pin d\'ete"
    time.sleep(2)
    lcd.clear()
    lcd.message = "joie\nrepercutee"
    time.sleep(2)
    lcd.clear()
    lcd.message = "la pluie chaude\ntorentielle"
    time.sleep(2)
    lcd.clear()
    lcd.message = "enveloppante\nhilarante"
    time.sleep(2)
    lcd.clear()
    lcd.message = "L\'herbe\nparfumee"
    time.sleep(2)
    lcd.clear()
    lcd.message = "etincelante\nondulante"
    time.sleep(2)
    lcd.clear()
    lcd.message ="L\'ombre d\'une\nfleur"
    time.sleep(2)
    lcd.clear()
    lcd.message = "plus butee que\nl\'authentique" 
    time.sleep(2)
    lcd.clear()
    lcd.message = "Souvenirs"
    time.sleep(2)
    lcd.clear()
    lcd.message = "en tableaux \nliquides"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Christine Sioui\nWawanoloath"
    time.sleep(5)
    lcd.clear()

def aaa():
    lcd.message ="Elle est nee\nil y a"
    time.sleep(2)
    lcd.clear()
    lcd.message = "des milliers\nd\'annees"
    time.sleep(2)
    lcd.clear()
    lcd.message = "d\'une pensee\nmagique"
    time.sleep(2)
    lcd.clear()
    lcd.message = "pour nourrir\nle monde antique"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Elle renait\nencore deesse"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Maize"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Christine Sioui\nWawanoloath"
    time.sleep(5)
    lcd.clear()

def bbb():
    lcd.message ="La nature etait\nla parente"
    time.sleep(2)
    lcd.clear()
    lcd.message = "bien-aimee\nde nos ancetres"
    time.sleep(2)
    lcd.clear()
    lcd.message = "les Wabanakis"
    time.sleep(2)
    lcd.clear()
    lcd.message = "Ils savaient\ncomposer"
    time.sleep(2)
    lcd.clear()
    lcd.message = "de grande\nlegendes"
    time.sleep(2)
    lcd.clear()
    lcd.message = "avec tous les\nelements visibles"
    time.sleep(2)
    lcd.clear()
    lcd.message = "et invisibles\nde l\'univers"
    time.sleep(2)
    lcd.clear()
    lcd.message = "-Christine Sioui\nWawanoloath"
    time.sleep(5)
    lcd.clear()

poemes = [a,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx, yy, zz, aaa, bbb]

poemes2=copy.copy(poemes)

def rouge():
    lcd.color = [100, 0, 0]
def bleu(): 
    lcd.color = [0, 100, 0]
def vert():
    lcd.color = [0, 0, 100]
def pourpre():
    lcd.color = [50, 0, 50]

couleurs = [rouge, bleu, vert, pourpre]

while poemes:
        couleur=random.choice(list(couleurs))
        couleur()
        poeme=random.choice(list(poemes))
        poeme()
        if len(poemes)==1:
            poemes.extend(poemes2)
        else:
            poemes.remove(poeme)
        
