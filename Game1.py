import pygame, sys

#General Setup
pygame.init()
clock= pygame.time.Clock()

#Setting up the main window
screen_width=950
screen_height=650
screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First Game')
bg_color= pygame.Color('lightgrey')
light_grey= (200, 90, 90)

background= pygame.image.load("Bkgrnd_game1.jpg")

#Position
x_position = screen_width/3.5 -30
y_position = screen_height/1.5 -45

#Player
player= pygame.Rect(x_position, y_position, 10, 100)

#Game variables

jumping= False
y_gravity= 1
jump_height= 20
y_velocity= jump_height


moving_right= False
x_position = screen_width/3.5 -30

moving_left= False
y_position = screen_height/1.5 -45

#The Game
while True:
	 for event in pygame.event.get():
	 	if event.type == pygame.QUIT:
	 		pygame.quit()
	 		sys.exit()
	 #Visuals
	 screen.blit(background, (0, 0))
	 pygame.draw.rect(screen, light_grey, player)
	 
	 #Game logic
	 keys_pressed= pygame.key.get_pressed()
	 
	 #Player_animation
	 if keys_pressed[pygame.K_RIGHT]:
	 	moving_right == True

	 if keys_pressed[pygame.K_LEFT]:
	 	moving_left ==True

	 #RIGHT
	 if moving_right:
	 	x_position+=10

	 #LEFT
	 if moving_left:
	 	player.x_position -= 20

	 #JUMP
	 if keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_UP]:
	 	jumping= True

	 if jumping:
	 	y_position-= y_velocity
	 	y_velocity-= y_gravity
	 	if y_velocity <- jump_height:
	 		jumping= False
	 		y_velocity= jump_height
	 	player= pygame.Rect(x_position, y_position, 10, 100)
	 #DOWN



	 #Updating the window
	 pygame.display.update()
	 clock.tick(60)