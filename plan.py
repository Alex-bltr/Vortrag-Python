import random #libraries 
import time
#also wir fangen mit etwas kleinem an undzwar mit dem print befehl
print("was auch immmer ihr da rein schreiben wollt")
#ziemlich einfcah wie ihr seht ist das ausgeben von infos etc ziemlich 
#wir hatten ja in nsnap gelernt was sind funktionen und methoden 
class test:
    def __init__(self):
        pass
    def Hallo(): #----------------methode------------------------
        print("hallo")

def Tschüss():
    print("Tschüss") #------------------------funktion-----------------
'''aber das ist auch das nächste kurze thema undzwar funktionen weil eigentlich wie ihr seht ist jede methode 
immer eine funktion einer klasse'''
def Tschüs_name(name):#param 
    print(f"Tschüss{name}")
# hier sieht man dann auch einen f sting... erklär einfach was das ist und wozu 
#lösche alles und mache das bubblesort alg
def bubblesort(Liste):
    print(f"unsorrtierte Liste: {Liste}")
    t1 = time.perf_counter()
    n = len(Liste)
    for i in range(n-1):
        for j in range(n-1-i):
            swapped = False
            if Liste[j] > Liste[j+1]:
                Liste[j],Liste[j+1] = Liste[j+1], Liste[j]
                swapped = True
        if swapped == False:
            t2 = time.perf_counter()
            print(f"sorrtierte Liste: {Listemitzahlen} benötigte Zeit: {t2-t1:.6}s")
            break


if __name__ == "__main__":
    Listemitzahlen = [random.randint(1,10) for i in range(1000)]
    bubblesort(Listemitzahlen)
