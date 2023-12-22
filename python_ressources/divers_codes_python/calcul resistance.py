#codin:utf-8

class Application:
    def __init__(self):
        """Constructeur de la fen�tre principale"""
        self.root =Tk()
        self.root.title('Code des couleurs')
        self.dessineResistance()
        Label(self.root,
              text ="Entrez la valeur de la r�sistance, en ohms :").grid(row =2)
        Button(self.root, text ='Montrer',
               command =self.changeCouleurs).grid(row =3, sticky = W) 
        Button(self.root, text ='Quitter',
               command =self.root.quit).grid(row =3, sticky = E)
        self.entree = Entry(self.root, width =14)
        self.entree.grid(row =3)
        # Code des couleurs pour les valeurs de z�ro � neuf :
        self.cc = ['black','brown','red','orange','yellow',
                   'green','blue','purple','grey','white']
        self.root.mainloop()
        
    def dessineResistance(self):
        """Canevas avec un mod�le de r�sistance � trois lignes color�es"""
        self.can = Canvas(self.root, width=250, height =100, bg ='ivory')
        self.can.grid(row =1, pady =5, padx =5)
        self.can.create_line(10, 50, 240, 50, width =5)         # fils
        self.can.create_rectangle(65, 30, 185, 70, fill ='light grey', width =2)
        # Dessin des trois lignes color�es (noires au d�part) :
        self.ligne =[]              # on m�morisera les trois lignes dans 1 liste  
        for x in range(85,150,24):
            self.ligne.append(self.can.create_rectangle(x,30,x+12,70,
                                                        fill='black',width=0))

    def changeCouleurs(self):
        """Affichage des couleurs correspondant � la valeur entr�e"""
        self.v1ch = self.entree.get()       # la m�thode get() renvoie une cha�ne
        try:
            v = float(self.v1ch)            # conversion en valeur num�rique
        except:            
            err =1                          # erreur : entr�e non num�rique
        else:
            err =0
        if err ==1 or v < 10 or v > 1e11 :
            self.signaleErreur()            # entr�e incorrecte ou hors limites
        else:
            li =[0]*3                       # liste des 3 codes � afficher
            logv = int(log10(v))            # partie enti�re du logarithme 
            ordgr = 10**logv                # ordre de grandeur
            # extraction du premier chiffre significatif :
            li[0] = int(v/ordgr)            # partie enti�re
            decim = v/ordgr - li[0]         # partie d�cimale
            # extraction du second chiffre significatif :
            li[1] = int(decim*10 +.5)           # +.5 pour arrondir correctement
            # nombre de z�ros � accoler aux 2 chiffres significatifs :
            li[2] = logv -1                                 
            # Coloration des 3 lignes :
            for n in range(3):
                self.can.itemconfigure(self.ligne[n], fill =self.cc[li[n]])
            
    def signaleErreur(self):
 # colorer le fond du champ
        self.entree.configure(bg ='red')
        self.root.after(1000, self.videEntree)
        # apr�s 1 seconde, effacer
    def videEntree(self):
 # r�tablir le fond blanc
        self.entree.configure(bg ='white')
        self.entree.delete(0, len(self.v1ch))
# r�tablir le fond blanc
# Programme principal :        
from Tkinter import *
 # logarithmes en base 10
from math import log10
 # instanciation de l'objet application
f = Application()
