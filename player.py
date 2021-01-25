import pygame #used to create video games
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #it permits selecting dir
import os #it permits to interact with the operating system

music_player = tkr.Tk()
music_player.title("Cho's first python project")
music_player.geometry("200x400")

directory = askdirectory()
os.chdir(directory) #it permits to change the current dir
song_list = os.listdir() #it returns the list of files song

play_list = tkr.Listbox(music_player, font="Moon 9 bold", bg="wheat", fg="brown", selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width=5, height=1, font="Moon 12 bold", text="PLAY", command=play, bg="tan", fg="white")
Button2 = tkr.Button(music_player, width=5, height=1, font="Moon 12 bold", text="STOP", command=stop, bg="brown", fg="white")
Button3 = tkr.Button(music_player, width=5, height=1, font="Moon 12 bold", text="PAUSE", command=pause, bg="peru", fg="white")
Button4 = tkr.Button(music_player, width=5, height=1, font="Moon 12 bold", text="CONTINUE", command=unpause, bg="coral", fg="brown")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Moon 9 bold", bg="green", fg="lime", textvariable=var)

play_list.pack(fill="both", expand="yes")
song_title.pack()
Button1.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button2.pack(fill="x")
music_player.mainloop()
