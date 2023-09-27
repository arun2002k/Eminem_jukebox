import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os


player = tkinter.Tk()
player.title("M&M Player")
player.geometry("310x325")

var = tkinter.StringVar()
var.set("Select the song to play")

os.chdir(askdirectory())
songlist = os.listdir()

playing = tkinter.Listbox(player, font = "Orbitron 10 bold",width=25, bg="black",fg="white",selectmode=tkinter.SINGLE)

for item in songlist:
    playing.insert(0,item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tkinter.ACTIVE))
    name = playing.get(tkinter.ACTIVE)
    var.set(f"{name[:16]}..." if len(name)>18 else name)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

text = tkinter.Label(player,font= "Orbitron",textvariable= var).grid(row=0,columnspan=3)
playing.grid(columnspan=3)

playB = tkinter.Button(player, width = 6, height = 1,font ="Orbitron",text="Play",command=play,bg="lightgreen").grid(row=2,column=0)
pauseB = tkinter.Button(player, width = 6, height = 1,font ="Orbitron",text="Pause",command=pause,bg="lightblue",fg="black").grid(row=2,column=1)
resumeB = tkinter.Button(player, width = 7, height = 1,font ="Orbitron",text="Resume",command=resume,bg="lightpink",fg="black").grid(row=2,column=2)

player.mainloop()