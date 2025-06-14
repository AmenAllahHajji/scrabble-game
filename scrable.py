import tkinter as tk
from tkinter import messagebox
from random import randint
from spellchecker import SpellChecker
import unicodedata

class ScrabbleGame:
    def __init__(self,root):
        self.root=root
        self.root.title("Scrable")
        self.root.geometry("800x600")
        self.root.configure(bg="#C8E6D9")
        titre=tk.Label(self.root,text="Bienvenue au jeu Scrabble",font=("Helvetica", 22, "bold"),bg="#f5f5f5", fg="#333")
        titre.pack(pady=10)
        cadre = tk.Frame(self.root)
        cadre.pack(expand=True)
        self.liste=[]
        for i in range(7):
            bouton=tk.Button(cadre,text="",font=("Arial", 24), width=5, height=2,command=lambda i=i: self.ajouter(i))
            bouton.grid(row=0,column=i)
            self.liste.append(bouton)
        self.scores_lettres={
            'A':1,'E':1,'I':1,'L':1,'N':1,'O':1,'R':1,'S':1,'T':1,'U':1,
            'D':2,'G':2,
            'B':3,'C':3,'M':3,'P':3,
            'F':4,'H':4,'V':4,'W':4,'Y':4,
            'K':5,
            'J':8,'X':8,
            'Q':10,'Z':10
         }
        self.spell = SpellChecker(language='fr')
        self.s=""
        self.selectionnes=[]
        self.mots_possibles = [mot.upper() for mot in self.spell.word_frequency.words() if len(mot)== 7]
        self.time_left =60
        self.timer_on = True      
        self.mot=tk.Label(self.root,text="",font=("arial",24),bg="#f0f0f0",width=35, height=2,anchor="center")
        self.mot.pack(pady=(0, 50))
        self.mot.configure(bg="#ffffff", fg="#222", relief="sunken", bd=2)
        self.bouton_valider = tk.Button(self.root, text="Valider", font=("Arial", 12),bg="#ADD8E6",command=self.valider)
        self.bouton_valider.pack(pady=10)
        self.bouton_valider.configure(bg="#4caf50", fg="white", relief="raised", bd=3)
        self.bouton_nouvelle_main = tk.Button(self.root, text="Rejouer", font=("Arial", 12),bg="#ADD8E6",command=self.initialiser)
        self.bouton_nouvelle_main.pack(pady=10)
        self.bouton_nouvelle_main.configure(bg="#2196f3", fg="white", relief="raised", bd=3)
        self.bouton_retirer=tk.Button(self.root,text="Effacer Dernière Lettre",font=("Arial", 12), bg="#FFB6C1", command=self.supprimer_dernier)
        self.bouton_retirer.pack(pady=10)
        self.timer= tk.Label(self.root, text="Temps restant : 60", font=("Arial", 16), bg="#C8E6D9")
        self.timer.pack()
        self.initialiser()
    def ajouter(self,i):
        self.s+=self.liste[i]["text"]
        self.mot.config(text=self.s)
        self.liste[i].config(bg="#4CAF50", state="disabled")
        self.selectionnes.append(i)
    def verouiller_boutons(self):
        for btn in self.liste:
            btn.config(state="disabled")
        self.bouton_valider.config(state="disabled")
        self.bouton_retirer.config(state="disabled")
    def activer_boutons(self):
        for btn in self.liste:
            btn.config(state="normal")
        self.bouton_valider.config(state="normal")
        self.bouton_retirer.config(state="normal")
    def initialiser(self):
        self.selectionnes = []
        self.s = ""
        self.time_left =60
        self.timer_on = True
        lettres=list(self.mots_possibles[randint(0,len(self.mots_possibles)-1)])
        ch=[]
        print(lettres)
        for i in range(7):
            ch.append(lettres.pop(randint(0, len(lettres) - 1))) 
        for i in range(7):
            self.liste[i].config(text=ch[i],bg="white")
        self.mot.config(text="")
        self.activer_boutons()
        self.timer.config(text="Temps restant : 60")
        self.countdown()
    def countdown(self):
        if self.timer_on and self.time_left>0:
            self.time_left -= 1
            self.timer.config(text="Temps restant :  "+str(self.time_left))
            self.root.after(1000, self.countdown)
        elif self.time_left == 0:
               self.timer_on = False
               messagebox.showinfo("Temps écoulé", "Le temps est écoulé, partie terminée.")
               self.verouiller_boutons()
    def valider(self):
        mot_genere=self.s.lower()
        if mot_genere== "":
            messagebox.showinfo("Erreur", "Veuillez construire un mot.")
        elif mot_genere in self.spell:
            messagebox.showinfo("Fin du jeu","Vous avez gagné!!")
            self.calculer_score()
            self.timer_on = False
            self.verouiller_boutons()
            
        else:
            messagebox.showinfo("Fin du jeu","Vous avez perdu!!")
            self.verouiller_boutons()
    def supprimer_dernier(self):
        if len(self.s) > 0:
            self.s = self.s[:-1]
            self.mot.config(text=self.s)
            indice=self.selectionnes.pop()
            self.liste[indice].config(bg="white",state="normal")
    def calculer_score(self):
        bonus=0
        ch=self.enlever_accents(self.s)
        for lettre in ch:
            bonus+=self.scores_lettres[lettre]
        messagebox.showinfo("Bonus","vous avez gagné"+str(bonus)+" points !!!")
    def enlever_accents(self, s):
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )
            
    
    
    
    
            
root=tk.Tk()
game = ScrabbleGame(root)
root.mainloop()
        
        
