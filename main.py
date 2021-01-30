import sys
import pygame
pygame.init()

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size, pygame.SCALED | pygame.FULLSCREEN)

planets = ['images/one.png', 'images/two.png', 'images/three.png']

background = pygame.image.load('images/background.png')
p_index = 0
planet = pygame.image.load(planets[p_index])
spaceship = pygame.image.load('images/spaceship.png')
bullet = pygame.image.load('images/bullet.png')

bullet_sound = pygame.mixer.Sound('sounds/bullet.wav')
collision_sound = pygame.mixer.Sound('sounds/collision.wav')
lost_sound = pygame.mixer.Sound('sounds/lost.ogg')

surfrect = screen.get_rect()
rect = pygame.Rect((165, 500), (40, 70))

win_text = pygame.font.SysFont('Consolas', 40).render('YOU WON!', True, pygame.color.Color('Green'))
lost_text = pygame.font.SysFont('Consolas', 40).render('YOU LOST!', True, pygame.color.Color('Red'))	
continue_text = pygame.font.SysFont('Consolas', 40).render('Click to Play Again', True, pygame.color.Color('White'))

bullets_left = 7
bullets_text = pygame.font.SysFont('Cursive', 25).render(f"Bullets: {bullets_left}", True, pygame.color.Color('Yellow'))

planets_left = 3
planets_text = pygame.font.SysFont('Cursive', 25).render(f"Planets: {planets_left}", True, pygame.color.Color('white'))

planet_x = 140
move_direction = 'right'
fired = False
bullet_y = 500

clock = pygame.time.Clock()

win = False
lost = False
keep_alive = True
while keep_alive:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif ev.type == pygame.MOUSEBUTTONDOWN:
			if rect.collidepoint(ev.pos):
				fired = True
				bullet_sound.play()
		if ev.type == pygame.MOUSEBUTTONDOWN and (win == True or lost == True):
				p_index = 0
				planet = pygame.image.load(planets[p_index])
				move_direction = 'right'
				bullets_left = 7
				bullets_text = pygame.font.SysFont('Cursive', 25).render(f"Bullets: {bullets_left}", True, pygame.color.Color('Yellow'))
				planets_left = 3
				planets_text = pygame.font.SysFont('Cursive', 25).render(f"Planets: {planets_left}", True, pygame.color.Color('White'))
				win = False
				lost = False
	if fired == True:
		bullet_y = bullet_y - 5
		if bullet_y == 50:
			fired = False
			bullet_y = 500
			bullets_left -= 1
			if bullets_left == 0 and win != True:
				lost = True
				lost_sound.play()
			if bullets_left >= 0:
				bullets_text = pygame.font.SysFont('Cursive', 25).render(f"Bullets: {bullets_left}", True, pygame.color.Color('Yellow'))
			
	screen.blit(background, [0,0])
	screen.blit(planet, [planet_x,50])
	screen.blit(bullet, [180,bullet_y])
	screen.blit(spaceship, [160,500])
	screen.blit(bullets_text, [10, 500])
	screen.blit(planets_text, [10, 520])
			
	if move_direction == 'right':
		planet_x = planet_x + 5
		if planet_x == 300:
			move_direction = 'left'
	elif move_direction == 'left':
		planet_x = planet_x - 5
		if planet_x == 0:
			move_direction = 'right'
	else:
		planet_x = 140
		screen.blit(win_text, [115, 250])
		screen.blit(continue_text, [60, 280])
		win = True
	
	if lost == True:
		planet_x = 140
		screen.blit(lost_text, [115, 250])
		screen.blit(continue_text, [60, 280])
	
	if bullet_y < 80 and planet_x > 120 and planet_x < 180:
		p_index = p_index + 1
		collision_sound.play()
		planets_left -= 1
		if planets_left >= 0:
			planets_text = pygame.font.SysFont('Cursive', 25).render(f"Planets: {planets_left}", True, pygame.color.Color('White'))
		if p_index < len(planets):
			planet = pygame.image.load(planets[p_index])
			planet_x = 10
		else:
			move_direction = "none"
	pygame.display.update()
	clock.tick(60)
	

		