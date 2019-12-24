from tkinter import *


main = Tk()
main.configure(width=1200, height=800)
main.resizable(width=False, height=False)

heure = Canvas(main, width=700, height=400, background='white')
actu = Canvas(main, width=250, height=800, background='white')
meteo = Canvas(main, width=150, height=150, background='white')
#------
heure.pack()#CENTRE
actu.pack()#DROITE
meteo.pack()#HAUT GAUCHE
main.mainloop()
