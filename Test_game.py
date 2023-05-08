import pygame, sys

def player_animation_x():
	if player.left <= 0:
		player.left = 0
	if player.right >= 950:
		player.right = 950
def player_animation_y():
	if player.top <= 0:
		player.top=0
	if player.bottom >=y:
		player.bottom =y

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

y= 535
player= pygame.Rect( 241, y, 10, 80)


jumping= False
y_gravity= 1
jump_height= 20
y_velocity= jump_height

move_right= False
move_left= False
move_up= False


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				move_right = True
			if event.key == pygame.K_LEFT:
				move_left = True
			if event.key == pygame.K_SPACE:
				jumping = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				move_right = False
			if event.key == pygame.K_LEFT:
				move_left = False
			if event.key == pygame.K_SPACE:
				jumping = True
	if move_right:
		player.x += 7.5
	if move_left:
		player.x -= 7.5
	
	if jumping:
		player.y -= y_velocity
		y_velocity -= y_gravity		
		if y_velocity <- jump_height:
	 		jumping= False
	 		y_velocity= jump_height
	 		#player=pygame.Rect(241, player.y, 10, 100)


	player_animation_x()
	player_animation_y()

	#Visuals
	#screen.fill(bg_color)
	screen.blit(background, (0, 50))
	pygame.draw.rect(screen, light_grey, player)

	#Updating the window
	pygame.display.flip()
	clock.tick(60)