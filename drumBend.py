# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:55:52 2019

@author: Owner
"""

import pygame, sys
from tkinter import *
from tkinter import ttk

class DrumBend(Frame) :
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.inisialisasiBunyiDrum()
        parent.geometry('680x300')
        self.buatText()
        self.crashSatu()
        self.crashDua()
        self.buatHat()
        self.kickSatu()
        self.kickDua()
        self.rideSatu()
        self.rideDua()
        self.buatSnare()
        self.tomSatu()
        self.tomDua()
        self.tomTiga()
        self.tomEmpat()
        self.hatKick()
    def inisialisasiBunyiDrum(self):
        self.crash1 = 'crash1.wav'
        self.crash2 = 'crash2.wav'
        self.hat = 'hat.wav'
        self.kick1 = 'kick1.wav'
        self.kick2 = 'kick2.wav'
        self.ride1 = 'ride1.wav'
        self.ride2 = 'ride2.wav'
        self.snare = 'snare.wav'
        self.tom1 = 'tom1.wav'
        self.tom2 = 'tom2.wav'
        self.tom3 = 'tom3.wav'
        self.tom4 = 'tom4.wav'
        self.hat_kick = 'hat_kick.wav'
    def drumSatu(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.crash1)
        pygame.mixer.music.play()
    def drumDua(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.crash2)
        pygame.mixer.music.play()
    def drumTiga(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.hat)
        pygame.mixer.music.play()
    def drumEmpat(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.kick1)
        pygame.mixer.music.play()
    def drumLima(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.kick2)
        pygame.mixer.music.play()
    def drumEnam(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.ride1)
        pygame.mixer.music.play()
    def drumTujuh(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.ride2)
        pygame.mixer.music.play()
    def drumDelapan(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.snare)
        pygame.mixer.music.play()
    def drumSembilan(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.tom1)
        pygame.mixer.music.play()
    def drumSepuluh(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.tom2)
        pygame.mixer.music.play()
    def drumSebelas(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.tom3)
        pygame.mixer.music.play()
    def drumDuabelas(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.tom4)
        pygame.mixer.music.play()
    def drumTigabelas(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.hat_kick)
        pygame.mixer.music.play()
    def buatText(self):
        Label(text="Drum Bend", fg="dodgerblue", bg="white").pack(fill=X)
    def crashSatu(self):
        Button(text="Tekan Q = Crash 1", command=self.drumSatu).pack(fill=X)
    def crashDua(self):
        Button(text="Tekan W = Crash 2", command=self.drumDua).pack(fill=X)
    def buatHat(self):
        Button(text="Tekan E = Hat", command=self.drumTiga).pack(fill=X)
    def kickSatu(self):
        Button(text="Tekan R = Kick 1", command=self.drumEmpat).pack(fill=X)
    def kickDua(self):
        Button(text="Tekan T = Kick 2", command=self.drumLima).pack(fill=X)
    def rideSatu(self):
        Button(text="Tekan Y = Ride 1", command=self.drumEnam).pack(fill=X)
    def rideDua(self):
        Button(text="Tekan U = Ride 2", command=self.drumTujuh).pack(fill=X)
    def buatSnare(self):
        Button(text="Tekan I = Snare", command=self.drumDelapan).pack(fill=X)
    def tomSatu(self):
        Button(text="Tekan O = Tom 1", command=self.drumSembilan).pack(fill=X)
    def tomDua(self):
        Button(text="Tekan P = Tom 2", command=self.drumSepuluh).pack(fill=X)
    def tomTiga(self):
        Button(text="Tekan A = Tom 3", command=self.drumSebelas).pack(fill=X)
    def tomEmpat(self):
        Button(text="Tekan S = Tom 4", command=self.drumDuabelas).pack(fill=X)
    def hatKick(self):
        Button(text="Tekan D = Hat_Kick", command=self.drumDuabelas).pack(fill=X)
    def stopMusik(self):
        pygame.mixer.music.stop()
        
def main():
    root = Tk()
    bend=DrumBend(root)
    def key(event):
        if event.keysym=="q" :
            bend.drumSatu()
        if event.char=="w" :
            bend.drumDua()
        if event.char=="e" :
            bend.drumTiga()
        if event.char=="q" :
            bend.drumEmpat()
        if event.char=="r" :
            bend.drumLima()
        if event.char=="t" :
            bend.drumEnam()
        if event.char=="y" :
            bend.drumTujuh()
        if event.char=="u" :
            bend.drumDelapan()
        if event.char=="i" :
            bend.drumSembilan()
        if event.char=="i" :
            bend.drumSepuluh()
        if event.char=="o" :
            bend.drumSebelas()
        if event.char=="p" :
            bend.drumSembilan()
        if event.char=="a" :
            bend.drumDuabelas()
        if event.char=="d" :
            bend.drumTigabelas()
        if event.char=="s":
            bend.stopMusik()
    root.bind("<Key>", key)
    root.mainloop()
    pygame.quit()
    
if __name__ == '__main__' :
    main()     