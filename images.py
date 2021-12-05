from sense_hat import SenseHat
from camera import*
from tkinter import*

def Visionneur():
    fen = Tk()
    can = Canvas(fen,bg='dark grey',height=200,width=200)
    photo = PhotoImage(file ='image.png')
    item = can.create_image(80, 80, image =photo)
    bou1 =  Button(fen, text='Quitter', command = fen.destroy)
    bou5 =  Button(fen, text='Appareil', command = Appareil)
    can.pack()
    bou1.pack(side=BOTTOM)
    bou5.pack(side=BOTTOM)
    fen.mainloop()

def Appareil():
    fen1 = Tk()
    bou2 =  Button(fen1, text= "Photo", command = photo)
    bou3 =  Button(fen1, text='Filmer', command = film)
    bou4 =  Button(fen1, text='Voir les photos', command = Visionneur)
    bou =  Button(fen1, text='Quitter', command = fen1.destroy)
    bou2.pack()
    bou3.pack()
    bou4.pack()
    bou.pack()
    fen1.mainloop()

Appareil()
