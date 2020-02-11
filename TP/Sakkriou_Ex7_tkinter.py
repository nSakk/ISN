from tkinter import *

maFenetre = Tk()

x = 0
y = 0
l = 0
c = 0


# Fonctions
def grilleCreation():
    grille.delete("all")
    for loop in range(5, 305, 20):
        grille.create_line([(loop, 5), (loop, 305)])

    for loop in range(5, 305, 20):
        grille.create_line([(5, loop), (305, loop)])

    grille.create_line([(5, 5), (5, 305)])
    grille.create_line([(305, 5), (305, 305)])
    grille.create_line([(5, 5), (305, 5)])
    grille.create_line([(5, 305), (305, 305)])


def coordonnes(event):
    global x, y
    x = event.x
    y = event.y
    result_labelx.config(text=f"abscisse : {x}")
    result_labely.config(text=f"ordonnée : {y}")
    ligne = int(y / 20) + 1
    column = int(x / 20) + 1
    result_colonne.config(text=f"colonne : {column}")
    result_ligne.config(text=f"ligne : {ligne}")

    grilleCreation()
    grille.create_line([(x - 5, y), (x + 5, y)])
    grille.create_line([(x, y - 5), (x, y + 5)])


# Création des widgets
result_labelx = Label(maFenetre, text=f"abscisse : {x}")
result_labely = Label(maFenetre, text=f"ordonnée : {x}")
result_ligne = Label(maFenetre, text=f"ligne : {l}")
result_colonne = Label(maFenetre, text=f"colonne : {c}")
boutonGrid = Button(maFenetre, text="Tracer la grille", command=grilleCreation)

grille = Canvas(maFenetre, width=310, height=310)

# Affichage des widgets
boutonGrid.grid(row=0, column=1)
result_labelx.grid(row=1, column=1)
result_labely.grid(row=2, column=1)
result_ligne.grid(row=3, column=1)
result_colonne.grid(row=4, column=1)
grille.grid(row=0, column=0, rowspan=5)

# Boucle principale
maFenetre.bind("<Button 1>", coordonnes)
maFenetre.mainloop()