import pygame
import tkinter as tk
from tkinter import *
import os
import platform
if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

root = tk.Tk()
# creates embed frame for pygame window
embed = tk.Frame(root, width=80, height=80)
embed.grid(columnspan=(600), rowspan=500)  # Adds grid
embed.pack(side=LEFT)  # packs window to the left
buttonwin = tk.Frame(root, width=5, height=5)
buttonwin.pack(padx=12, pady=12)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
screen = pygame.display.set_mode((800, 800))
screen.fill(pygame.Color(255, 255, 255))
pygame.display.init()
pygame.display.update()


def draw():
    pygame.draw.circle(screen, (0, 0, 0), (250, 250), 125)
    pygame.display.update()
    button1 = Button(buttonwin, text='Draw',  command=draw)
    button1.pack(side=LEFT)
    root.update()


draw()

while True:
    pygame.display.update()
    root.update()


