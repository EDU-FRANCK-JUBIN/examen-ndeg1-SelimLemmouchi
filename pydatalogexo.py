from pyDatalog import pyDatalog
from easygui import *

pyDatalog.clear()

pyDatalog.create_terms('plusUrgent, moinsUrgent, physique, electrique, chaleur, asphyxie, saigne, etouffement, malaise, brulure,  X')

plusUrgent(X) <= physique(X)
plusUrgent(X) <= electrique(X)
plusUrgent(X) <= chaleur(X)
plusUrgent(X) <= asphyxie(X)

moinsUrgent(X) <= saigne(X)
moinsUrgent(X) <= etouffement(X)
moinsUrgent(X) <= brulure(X)
moinsUrgent(X) <= malaise(X)

+etouffement('mainALaGorge')


message = "bonjour, raison de l'appel ?"
title = "mon ihm"
msgbox(message, title, "ok !")
print(reponse)
