import pygame

pygame.init()

screen = pygame.display.set_mode((1000,618))

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

running = True

while running:
	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				print("up clicked")
			if event.key == pygame.K_DOWN:
				print("down clicked")
			if event.key == pygame.K_w:
				print("w clicked")
			if event.key == pygame.K_s:
				print("s clicked")

	pygame.draw.circle(screen, WHITE, (500,309),12)


	pygame.display.flip()

pygame.quit
