import pygame
import csv
from PIL import Image
pygame.init()

def iconChange(img,Width,Height):
    im = Image.open("icon/original/" + img)

    # image size
    size = (int(Width), int(Height))
    out = im.resize(size)
    out.save("icon/resized/" + img)

with open("settings.csv") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        if line[0] == "resolution":
            res = (int(line[1]),int(line[2]))

win = pygame.display.set_mode(res)

x = res[0] * 0.01
y = res[1] * 0.01

h = y * 10
w = h

screen = 1
pygame.display.set_caption('calendar')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (x,y) and pygame.mouse.get_pos() <= (x + w, y + h):
                screen = 2

    iconChange("settings.png", w, h)
    iconChange("arrow.png", w, h)
    win.fill((255,255,255))
    if screen == 1:
        Img = pygame.image.load("icon/resized/settings.png")
        win.blit(Img, (x, y))
    if screen == 2:
        Img = pygame.image.load("icon/resized/arrow.png")
        win.blit(Img, (x, y))


    pygame.display.update()

pygame.quit()