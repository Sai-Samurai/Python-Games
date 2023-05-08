import pygame 
import math

pygame.init()

larg = 720
long = 720
num1 = ((long - 50)//22)
num2 = (larg//20)
PI = math.pi
PacposX = 20
PacposY = 345
screen = pygame.display.set_mode([larg, long])

# 0 = noir, 1 = trait H, 2 = trait V, 3 = petit point, 4 = gros point blanc
# 5 = coin (type en haut à gauche), 6 = coin (type en haut à droite)
# 7 = coin (type en bas à gauche), 8 = coin (type en bas à droite)
# 9 = trait H blanc 

case = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6], 
[2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2], 
[2, 4, 5, 1, 1, 6, 3, 5, 6, 3, 2, 3, 5, 6, 3, 5, 1, 6, 4, 2], 
[2, 3, 2, 0, 0, 2, 3, 2, 2, 0, 2, 3, 2, 2, 3, 2, 0, 2, 3, 2], 
[2, 3, 2, 0, 0, 2, 3, 2, 2, 3, 2, 3, 2, 2, 3, 2, 0, 2, 3, 2], 
[2, 3, 7, 1, 1, 8, 3, 7, 8, 3, 2, 3, 7, 8, 3, 7, 1, 8, 3, 2], 
[2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2], 
[2, 3, 5, 1, 1, 1, 1, 1, 6, 3, 5, 1, 1, 1, 1, 1, 1, 6, 3, 2], 
[2, 3, 2, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 2, 3, 2], 
[8, 3, 7, 1, 1, 1, 1, 1, 8, 3, 7, 1, 1, 1, 1, 1, 1, 8, 3, 7], 
[0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0], 
[6, 3, 1, 1, 1, 6, 3, 5, 1, 9, 9, 9, 1, 6, 3, 5, 1, 1, 1, 5], 
[2, 3, 3, 3, 3, 2, 3, 2, 0, 0, 0, 0, 0, 2, 3, 2, 3, 3, 3, 2], 
[2, 3, 5, 6, 3, 2, 3, 2, 0, 0, 0, 0, 0, 2, 3, 2, 3, 3, 3, 2], 
[2, 3, 2, 2, 3, 2, 3, 7, 1, 1, 1, 1, 1, 8, 3, 2, 3, 2, 3, 2], 
[2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2], 
[2, 4, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 4, 2], 
[2, 3, 7, 8, 3, 7, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 8, 3, 2], 
[2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],
[7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def afficher_case (case): 
    #num1 = ((long - 50)//22)
    #num2 = (larg//20)
    nbelem = 20 
    for a in range (len(case)): 
        for b in range (0, nbelem): 
            if case [a][b] == 3: 
                pygame.draw.circle (screen, (255,255,255), (b * num2 + (0.5 * num2), a * num1 + (0.5 * num1)), 3)
                pygame.display.flip()
            elif case [a][b] == 4:
                pygame.draw.circle (screen, (255,255,255), (b * num2 + (0.5 * num2), a * num1 + (0.5 * num1)), 7)
            elif case [a][b] == 2: 
                pygame.draw.line(screen, (0, 0, 255), (b * num2 + (0.5 * num2), a * num1), (b * num2 + (0.5 * num2), a * num1 + num1), 3)
            elif case [a][b] == 1: 
                pygame.draw.line(screen, (0, 0, 255), (b * num2, a * num1 + (0.5 * num1)), (b * num2 + num2, a * num1 + (0.5 * num1)), 3)
            elif case [a][b] == 9: 
                pygame.draw.line(screen, (255, 255, 255), (b * num2, a * num1 + (0.5 * num1)), (b * num2 + num2, a * num1 + (0.5 * num1)), 3)
            elif case [a][b] == 6: 
                pygame.draw.arc(screen, (0,0,255), [b * num2 - (num2 * 0.5), a * num1 + (0.5 * num1), num2, num1], 0, PI/2, 3)
            elif case [a][b] == 5: 
                pygame.draw.arc(screen, (0,0,255), [b * num2 + (num2 * 0.5), a * num1 + (0.5 * num1), num2, num1], PI/2, PI, 3)
            elif case [a][b] == 7: 
                pygame.draw.arc(screen, (0,0,255), [b * num2 + (num2 * 0.5), a * num1 - (0.5 * num1), num2, num1], PI, 3*PI/2, 3)
            elif case [a][b] == 8: 
                pygame.draw.arc(screen, (0,0,255), [b * num2 - (num2 * 0.5), a * num1 - (0.5 * num1), num2, num1], 3*PI/2, 2*PI, 3)   
              
                
class Perso (): # yellow ball 
    def __init__(self, x, y, taille):
        self.x = x 
        self.y = y 
        self.taille = taille
        
        
    """   
    def set_x (self, p): 
        self.x = p
        
    def get_x (self): 
        print(self.x)
        return self.x
     """
     
    def afficher (self, screen):
        pygame.draw.circle(screen, (255,255,0), (self.x, self.y), self.taille)

class Fant (Perso): #4 other balls 
    def __init__ (self, x, y, taille, couleur): 
        Perso.__init__(self, x, y, taille)
        self.couleur = couleur
        
    def affi (self, screen): 
        pygame.draw.circle (screen, self.couleur, (self.x,self.y), self.taille)
        
        
running = True 
while running: 
    afficher_case (case) # background 
    #pygame.display.flip() 
    Pac = Perso(20, 345, 20) #creating pacman
    fanr = Fant (295, 420, 20, (255,0,255))
    fanb = Fant (350, 420, 20, (0,0,255))
    fano = Fant (400, 420, 20, (255,100,10))
    fanro = Fant (450, 420, 20, (255,0,0))
    Pac.afficher(screen)
    fanr.affi(screen)
    fano.affi(screen)
    fanro.affi(screen)
    fanb.affi(screen)
    pygame.display.flip()
    
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
            
        if event.type == pygame.KEYDOWN: 
            print("key pressed")
            if event.key == pygame.K_RIGHT:
                """
                x = Pac.get_x()
                Pac.set_x (x + 40)
                x = Pac.get_x()
                Pac.afficher(screen)
                """
                PacposX = PacposX + 20
                print(PacposX)
                Pac = Perso (PacposX, PacposY, 20)
                Pac.afficher (screen)
                print("right key")
                pygame.display.flip()
                
            if event.key == pygame.K_LEFT: 
                PacposX = PacposX - 20
                Pac = Perso (PacposX, PacposY, 20)
                Pac.afficher(screen)
                pygame.display.flip()
                print("left key ")
                
            if event.key == pygame.K_DOWN: 
                PacposY = PacposY + 20
                Pac = Perso (PacposX, PacposY, 20)
                Pac.afficher(screen)
                pygame.display.flip()
                print("down key ")
            
            if event.key == pygame.K_UP: 
                PacposY = PacposY - 20
                Pac = Perso(PacposX, PacposY, 20)
                Pac.afficher(screen)
                pygame.display.flip()
                print("up key ")
                
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    pygame.display.flip()
pygame.quit()