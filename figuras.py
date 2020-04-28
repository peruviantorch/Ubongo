import pygame

fig1 = [[1,1,1,1,1,1],
        [1,1,1,1,1,1]]

fig2 = [[1,1,1,1],
        [1,1,1,1],
        [1,1],
        [1,1]]

col = (25, 150, 200)

def main():

    running = True;
    # inicializa Pygame
    pygame.init()

        # establece el título de la ventana
    pygame.display.set_caption('Dibujar polígono')

        # establece el tamaño de la ventana
    screen = pygame.display.set_mode((400, 400))

    rect1 = [(0,0), (100,50)] 
    
    poly1 = [(0,0),(100,0), (100,50), (50,50), (50,100), (0,100)]
    
    #pygame.draw.rect(screen, col, rect1, 0)
    
    pygame.draw.polygon(screen, col, poly1, 0)
    
    pygame.display.flip()

    # bucle infinito

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
main()