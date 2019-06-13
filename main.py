import random
from tkinter import *
from tkinter.filedialog import *
import pygame
from PIL import Image, ImageTk
from pygame import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pos = 0
        self.musics = []
        pygame.mixer.init()
        self.img = ImageTk.PhotoImage(Image.open("background.jpg"))
        self.labelbg = Label(window, image=self.img)
        self.labelbg.pack(side="bottom", fill="both", expand="yes")

        p_original = PhotoImage(file="playbutton.png")
        p_small = p_original.subsample(10, 10)
        self.playButton = Button(self.labelbg, command=self.play, image=p_small).grid(column=2, row=0)

        s_original = PhotoImage(file="stop.png")
        sSmall = s_original.subsample(10, 10)
        self.stopBtn = Button(self.labelbg, command=self.stop, image=sSmall).grid(column=1, row=0)

        pa_original = PhotoImage(file="pause.png")
        pa_small = pa_original.subsample(10, 10)
        self.pauseBtn = Button(self.labelbg, command=self.pause, image=pa_small).grid(column=3, row=0)

        vu_original = PhotoImage(file="volumeup.png")
        vu_small = vu_original.subsample(10, 10)
        self.volumedownBtn = Button(self.labelbg, command=self.volumeUp, image=vu_small).grid(
            column=4, row=1)
        vd_original = PhotoImage(file="volumedown.png")
        vd_small = vd_original.subsample(10, 10)
        self.volumeupBtn = Button(self.labelbg, command=self.volumeDown, image=vd_small).grid(column=0,
                                                                                                              row=1)
        n_Original = PhotoImage(file="nextsong.png")
        n_small = n_Original.subsample(5, 5)
        self.nextSong = Button(self.labelbg, command=self.nextSong, image=n_small).grid(column=4, row=0)

        pr_original = PhotoImage(file="presong.png")
        pr_small = pr_original.subsample(10, 10)
        self.preSong = Button(self.labelbg, command=self.preSong, image=pr_small).grid(column=0, row=0)

        m_original = PhotoImage(file="mixbutton.png")
        m_small = m_original.subsample(10, 10)
        self.mix = Button(self.labelbg, command=self.mix, image=m_small).grid(column=1, row=1)

        re_original = PhotoImage(file="rewin.png")
        re_small = re_original.subsample(10, 10)
        self.rewind = Button(self.labelbg, command=self.rewind, image=re_small).grid(column=2, row=1)

        f_original = PhotoImage(file="forward button.png")
        f_small = f_original.subsample(5, 5)
        self.forward = Button(self.labelbg, command=self.forward, image=f_small).grid(column=3, row=1)

        pl_original = PhotoImage(file="playlist.png")
        pl_small = pl_original.subsample(10, 10)
        self.playlistopen = Button(self.labelbg, command=self.add_Playlist, image=pl_small).grid(
            column=0, row=2)
        self.v = StringVar()
        self.nowLbl = Label(self.labelbg, textvariable=self.v, relief=RAISED)

        self.pauseLbl = Label(self.labelbg, textvariable=self.v, relief=RAISED)

        window.mainloop()

    def play(self):
        pygame.mixer.music.load(self.musics[self.pos])
        pygame.mixer.music.play()
        self.NowPlaying()

    def add_Playlist(self):
        directory = askopenfilenames()
        print(directory)
        for song in directory:
            self.musics.append(song)

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()
        self.v.set("Paused ...")
        self.pauseLbl.place(x=0,y=180)

    def volumeDown(self):
        volume = pygame.mixer.music.get_volume()

        if volume > 0.1:
            volume -= 0.1
        else:
            volume = 0
        pygame.mixer.music.set_volume(volume)

    def volumeUp(self):
        volume = pygame.mixer.music.get_volume()

        if volume < 0.9:
            volume += 0.1
        else:
            volume = 1.0
        pygame.mixer.music.set_volume(volume)

    def nextSong(self):
        if self.pos < len(self.musics) - 1:
            self.pos += 1
        else:
            self.pos = 0
        pygame.mixer.music.load(self.musics[self.pos])
        pygame.mixer.music.play()
        self.NowPlaying()

    def preSong(self):
        if self.pos > 0:
            self.pos -= 1
        else:
            self.pos = len(self.musics) - 1
        pygame.mixer.music.load(self.musics[self.pos])
        pygame.mixer.music.play()
        self.NowPlaying()

    def mix(self):
        random.shuffle(self.musics)

        pygame.mixer.music.load(self.musics[self.pos])
        pygame.mixer.music.play()
        self.NowPlaying()


    def rewind(self):
        pygame.mixer.music.rewind()


    def forward(self):
        a = pygame.mixer_music.get_pos()
        time = a // 1000
        if time > 0:
            time += 10
            print(time)
        pygame.mixer.music.set_pos(time)

    def NowPlaying(self):
        songName = str(self.musics[self.pos]).split('/')

        self.v.set("Now Playing : " + songName[-1])
        self.nowLbl.place(x=80,y=130)




window = Tk()
window.geometry("300x300")
window.title("MP3 PLAYER")
window.configure(background="grey")
app = App(window)
