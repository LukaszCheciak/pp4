import queue

def Oblicz_podatek(brutto,podatek):
    if type(brutto) is float and type(podatek) is float:
        netto = 0
        netto = brutto - ((podatek*brutto)/100)
        return netto
    else:
        return "Dane zostały wprowadzone nieprawidłowo"
        
#------------------------------------------------------------------------------------#

queue =  queue.Queue()

for i in range(10):
    queue.put(i)
while not queue.empty():
    print(queue.get())


#-----------------------------------------------------------------------------------#

with open('tekst.txt', 'w') as f:
    f.write("tekst tekst tekst\n")

#--------------------------------------------------------------------------------------#

class Zajecia:
    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def zapiszStudenta(imie,nazwisko):
        lista = []
        if len(lista) >=10:
            return "Za duzo osob"
        else:
            p = Zajecia(imie,nazwisko)
            lista.append(p)
            print(lista)
