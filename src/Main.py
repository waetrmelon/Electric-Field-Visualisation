import pygame 
import random
import math

screen = pygame.display.set_mode((1280+200, 720)) 
pygame.display.set_caption('Electric Field Visualisation') 
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 15)
negative_charge = pygame.image.load("assets\\negative_charge.png")
negative_charge = pygame.transform.scale(negative_charge, (35,35))

PERMITIVITY = 8.85 * math.pow(10,-12)


class Vector():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.magnitude = 0
        self.angle = 0
        self.colour = [255,255,255]
        self.vector_arrow = pygame.image.load("assets\\arrow.png")
        self.vector_arrow = pygame.transform.scale(self.vector_arrow, (20,20))
    def Render(self, screen):
        self.CalculateMagnitude(Charges, screen)
        pygame.draw.circle(screen, (self.colour[0],self.colour[1],self.colour[2]), (self.x, self.y), 5)
    def CalculateMagnitude(self, Charges, screen):
        Distance = math.sqrt((self.x-Charges[0].x)**2 + (self.y-Charges[0].y)**2)
        if Distance == 0: Distance = 1
        Force = (Charges[0].charge)/((4*math.pi*PERMITIVITY)*math.pow(Distance,2))
        Scale = float(str(Force)[:4])
        self.colour[0] = 0
        self.magnitude = Force
        text_surface = font.render('{}'.format(str(Force)[:4]+"^"+str(Force)[-2:]), False, (255, 255, 255))
        screen.blit(text_surface, (self.x,self.y-20))
        text_surface = font.render('{}'.format(str(Distance)[:4]), False, (255, 255, 255))
        screen.blit(text_surface, (self.x,self.y-5))

class Charge():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.charge = 1.602* math.pow(10,-19)
    def Render(self, screen):
        self.x = pygame.mouse.get_pos()[0]+15
        self.y = pygame.mouse.get_pos()[1]+15
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 15)

Objects = []
Charges = []

NUM_ROW = 20
NUM_COLUMN = 10
for x in range(1,NUM_ROW):
    for y in range(1,NUM_COLUMN):
        Objects.append(Vector((1280/NUM_ROW) * x, (720/NUM_COLUMN) * y))

Charges.append(Charge(100,100))

running = True
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:   running = False

    screen.fill((0,0,0)) 

    
    for Object in Objects: Object.Render(screen)
    for CurrentCharge in Charges: CurrentCharge.Render(screen)

    pygame.display.update()