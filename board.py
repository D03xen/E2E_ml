import pygame

pygame.init()
window = pygame.display.set_mode((500,500))

light_square = (186,202,68)
dark_square = (118,150,86)
sq_type = True #dark_square is True
sq_values = dark_square
background = pygame.Surface((400,400))

for i in range(0,8):
    for j in range(0,8):
        if sq_type:
            sq_values = dark_square
        else:
            sq_values = light_square
        square = (j*50,i*50,50,50)
        pygame.draw.rect(background,sq_values,square)
        sq_type = not sq_type
    
    sq_type = not sq_type

window.blit(background,(50,50))
pygame.display.flip()

running=True
while running:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            running=False

pygame.quit()