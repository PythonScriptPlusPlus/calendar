import pygame
import csv
import os
import datetime
import time
from PIL import Image
pygame.init()

""" ТЗ по-backend'у
пофиксить маленькие баги
сделать возможность уведомлять пользователя о событии
"""

""" ТЗ по-frontend'у
нет
"""

def lDay(year, month):
	day = 1
	while 1:
		try:
			datetime.datetime(year,month,day)
			day += 1
		except:
			return day - 1
			break

def getPositions(year, month):
	positions = []
	for j in range(1,7):
		for i in range(0,7):
			if i == 0 and j == 1:
				positions.append((int(h//2), j*(5*y + h + 0.5*h)))

			elif i > 0 and i < 6 and j == 1:
				positions.append((int(h//2)+(a+2*x)*i, j*(5*y + h + 0.5*h)))

			elif i == 6 and j == 1:
				positions.append((res[0]-int(h//2)-a-x, j*(5*y + h + 0.5*h)))

			elif i == 0 and j != 1:
				positions.append((int(h//2), 5*y + (j-1) * (a + 2*x) + (h + 0.5*h)))

			elif i > 0 and i < 6 and j != 1:
				positions.append((int(h//2)+(a+2*x)*i, 5*y + (j-1) * (a + 2*x) + (h + 0.5*h)))

			elif i == 6 and j != 1:
				positions.append((res[0]-int(h//2)-a-x , 5*y + (j-1) * (a + 2*x) + (h + 0.5*h)))

	prevArrowX = positions[2][0]
	prevArrowY = positions[len(positions) - 5][1] + 2*y
	nextArrowX = positions[4][0]
	nextArrowY = positions[len(positions) - 3][1] + 2*y

	firstDay = datetime.datetime(year,month,1).weekday()
	
	for i in range(0,firstDay):
		positions.remove(positions[0])
	for i in range(0,len(positions)-lDay(year, month)):
		positions.remove(positions[len(positions) - 1])

	return positions, prevArrowX, prevArrowY, nextArrowX, nextArrowY

def getDaysOWeek():
	run = True
	i = 0
	a = positions[i][1]
	while run:
		if a == positions[i][1]:
			i += 1
		else:
			a = positions[i][0]
			run = False
	return a

def iconChange(img,Width,Height):
	im = Image.open("icon/original/" + img)

	# image size
	size = (int(Width), int(Height))
	out = im.resize(size)
	out.save("icon/resized/" + img)

def opening(x,y,w,h):
	click = pygame.mouse.get_pos()
	if click[0] >= x and click[0] <= x+w and click[1] >= y and click[1] <= y+h:
		return 1
	else:
		return 0

with open("settings.csv") as csv_file:
	csv_reader = csv.reader(csv_file)

	next(csv_reader)

	for line in csv_reader:
		if line[0] == "resolution":
			res = (int(line[1]),int(line[2]))

now = datetime.datetime.today()
monthHeader = now.month - 1
yearHeader = now.year
print(monthHeader)
onMouse = 1
done = False
colored = []
monthes = ["January","February","March","April","May","June","July","August","September","Octomber","November","December"]
daysOweek = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
win = pygame.display.set_mode(res)
icalendar = pygame.image.load("icon/original/calendar.png")
pygame.display.set_icon(icalendar)

x = int(res[0] * 0.01)
y = int(res[1] * 0.01)

if res[0] > res[1]:
	h = y * 10
	w = h
else:
	h = x * 10
	w = h

a = int((res[0] - h - 12*x) // 7)

fontCounter1 = int(10.5 * h // 14)
fontCounter2 = int(10.5 * h // 2 // 14)
fontCounter3 = int(10.5 * a // 14)

font = pygame.font.Font('InriaSans-Regular.ttf', fontCounter1)
font3 = pygame.font.Font('InriaSans-Regular.ttf', fontCounter2)
font4 = pygame.font.Font('InriaSans-Regular.ttf', fontCounter3)
font1 = pygame.font.Font('InriaSans-Regular.ttf', int(fontCounter1 // 4 * 3))
font2 = pygame.font.Font('InriaSans-Regular.ttf', int(fontCounter1 // 3))


screen = 1
pygame.display.set_caption('calendar')

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN and screen == 1:
			if opening(x,y,w,h):
				os.system('python settings.py')
			try:
				if event.type == pygame.MOUSEBUTTONDOWN and opening(positions[onMouse][0],positions[onMouse][1],a,a):
					with open("date.txt","w") as f:
						f.write(str(yearHeader) + " " + str(monthHeader + 1) + " " + str(onMouse + 1))
					os.system('python adder.py')
			except:
				pass
			if opening(prevArrowX,prevArrowY,w,h):
				if monthHeader == 0:
					yearHeader -= 1
				monthHeader = (monthHeader - 1) % 12
				colored = []
				print(monthHeader)
			if opening(nextArrowX,nextArrowY,w,h):
				if monthHeader == 11:
					yearHeader -=- 1
				monthHeader = (monthHeader + 1) % 12
				colored = []
	notify = "Nothing"
	positions, prevArrowX, prevArrowY, nextArrowX, nextArrowY = getPositions(yearHeader,monthHeader+1)
	iconChange("settings.png", w, h)
	iconChange("home.png", w, h)
	iconChange("arrow_left.png", a, a)
	iconChange("arrow_right.png", a, a)
	win.fill((255,255,255))
	print(yearHeader)
	pygame.draw.line(win,(200,200,200),(int(1.5*x),h+2*y),(res[0]-int(1.5*x),h+2*y), 3)
	if screen == 1:
		Img = pygame.image.load("icon/resized/settings.png")
		arrow_left = pygame.image.load("icon/resized/arrow_left.png")
		arrow_right = pygame.image.load("icon/resized/arrow_right.png")
		header = font.render(str(yearHeader) + " " + monthes[monthHeader], True, (100,100,100)) 
		
		textRect = header.get_rect()
		textRect.center = (res[0] // 2, y + h // 2)

		win.blit(Img, (x, y)) 
		win.blit(header, textRect)

		win.blit(arrow_left,(int(prevArrowX),int(prevArrowY)))
		win.blit(arrow_right,(int(nextArrowX),int(nextArrowY)))

		for i in range(0,7):
			daysOweekLine = getDaysOWeek()

			day = font3.render(daysOweek[i],True, (150,150,150))
			dayRect = day.get_rect()
			dayRect.center = (daysOweekLine + i*(a + 2*x) + int(a//2),int(5*y + h + 0.5*h) - 3*x)

			win.blit(day, dayRect)
		for i in range(0,len(positions)):
			if datetime.datetime.today().day == i+1 and now.month == monthHeader + 1 and now.year == yearHeader:
				pygame.draw.rect(win, (50,200,50),[int(positions[i][0]),int(positions[i][1]), a, a])
			else:
				if i+1 in colored:
					pygame.draw.rect(win, (255,0.5*255,0),[int(positions[i][0]),int(positions[i][1]), a, a])
				else:
					pygame.draw.rect(win, (50,50,50),[int(positions[i][0]),int(positions[i][1]), a, a])
			date = font4.render(str(i+1), True, (250,250,250))

			dateRect = date.get_rect()
			dateRect.center = (int(positions[i][0] + a // 2), int(positions[i][1] + a // 2))

			win.blit(date, dateRect)			
		for i in range(0,len(positions)):
			if opening(positions[i][0],positions[i][1],a,a):
				onMouse = i

				with open("schedule.csv") as csv_file:
					csv_reader = csv.reader(csv_file)

					next(csv_reader)
					for line in csv_reader:
						if line[0] == str(yearHeader) and line[1] == str(monthHeader+1):
							colored.append(int(line[2]))
						if line[0] == str(yearHeader) and line[1] == str(monthHeader+1) and line[2] == str(onMouse+1):
							if notify == "Nothing":
								notify = str(line[3])+":"+str(line[4])+": "+line[5]+"\n"
							else:
								notify += str(line[3])+":"+str(line[4])+": "+line[5]+"\n"
				notify = notify.split("\n")
				notify.sort()
				notify = "\n".join(notify)
				if notify == "Nothing":
					notify = "\n" + notify

				notify = notify.splitlines()

				mouseX = pygame.mouse.get_pos()[0]
				mouseY = pygame.mouse.get_pos()[1]
				if mouseX + h*4 < res[0]:
					pygame.draw.rect(win,(100,100,100),[mouseX,mouseY,h*5,3*h])
					for i, l in enumerate(notify):
						win.blit(font3.render(l, True, (255,255,255)),(int(mouseX),int(mouseY+h/2*(i-1))))		
				else:
					pygame.draw.rect(win,(100,100,100),[mouseX,mouseY,-h*5,3*h])
					for i, l in enumerate(notify):
						win.blit(font3.render(l, True, (255,255,255)),(int(mouseX-h*5),int(mouseY+h/2*(i-1))))



	pygame.display.update()

pygame.quit()
