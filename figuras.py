import pygame
from random import randint

class CFigura:
    x = 0
    y = 0
    col = (0,0,0)
    nF = 0
    forma = []
    
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.nF = n
        self.ActuForma()
    
    def ActuForma(self):
        if self.nF ==1:
            self.forma = [(self.x,self.y), (self.x+100,self.y), (self.x+100, self.y+50), (self.x, self.y +50)]
            self.col =(2, 189, 198)
        elif self.nF == 2:
            self.forma = [(self.x,self.y), (self.x+100, self.y), (self.x+100, self.y+50), (self.x+50,self.y+50), (self.x+50, self.y+100), (self.x,self.y+100)]
            self.col = (7, 244, 255)
        elif self.nF == 3:
            self.forma = [(self.x,self.y), (self.x+50,self.y), (self.x+50, self.y+50), (self.x+200, self.y+50), (self.x+200,self.y+100), (self.x,self.y+100)]
            self.col = (142, 68, 173)
        elif self.nF == 4:
            self.forma = [(self.x+50,self.y),(self.x+150,self.y), (self.x+150,self.y+50), (self.x+100,self.y+50), (self.x+100, self.y+150), (self.x,self.y+150), (self.x, self.y+100), (self.x+50, self.y+100)]
            self.col = (225, 179, 6)
        elif self.nF == 5:
            self.forma = [(self.x,self.y), (self.x+150,self.y), (self.x+150,self.y+50), (self.x+100,self.y+50), (self.x+100,self.y+100), (self.x+50, self.y+100), (self.x+50, self.y+50), (self.x, self.y+50)]
            self.col = (255, 255, 29)
        elif self.nF == 6:
            self.forma = [(self.x+50, self.y), (self.x+100, self.y), (self.x+100, self.y+150), (self.x, self.y+150), (self.x, self.y+50), (self.x+50, self.y+50)]
            self.col = (120, 255, 8)
    
    def draw(self, screen):
        self.ActuForma()
        pygame.draw.polygon(screen, self.col, self.forma, 0)  
    
    def getForm(self):
        return self.forma

    def getCol(self):
        return self.col
    
    def setPos(self, x,y):
        self.x = x
        self.y = y
    

def main():

    # Booleano que controla el while principal
    running = True
    
    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    pygame.display.set_caption('Ubongo!!!')

    # establece el tamaño de la ventana
    
    screen = pygame.display
    
    #Tamaño de la pantalla
    xs = 800
    ys = 600
    
    #Superfice que te toma
    surface = screen.set_mode([xs,ys])

    pygame.display.flip()

    #Reloj
    reloj = pygame.time.Clock()
    
    #Se crea la lista con todas las figuras
    Figuras = []
    for i in range(1,6):
        Figuras.append(CFigura(randint(0,500),randint(0,400),i))

    #Variables controladoras
    #X y Y sirven para obtener la posicion del raton
    x = 0
    y = 0
    #Bool que activa o desactiva el movimiento
    activate = False
    
    #aux -> Tomará los valores de la Figura seleccionada
    aux = 0 
    
    # bucle infinito 
    while running:
        reloj.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Booleanos que cambian su estado dependiendo si los botones
        #del mouse son apretados
        #Boton1 -> Click Izquierdo
        #Boton3 -> Click Derecho 
        boton1, boton2,boton3 = pygame.mouse.get_pressed()
        #Funcion que obtiene la posicion actual del puntero
        x,y = pygame.mouse.get_pos()
        #Funcion que obtiene el color en la posicion x,y (en este caso la pos del puntero)
        pixel = list(surface.get_at((x, y)))
        pixel.pop()
        
        #Si se apreta el boton1
        if boton1:
            for i in range(len(Figuras)):
                #Se compara el color de las figuras con la del pixel en la pos del mouse
                if pixel == list(Figuras[i].col):
                    activate = True
                    #aux se referencia a la figura[i]
                    aux = Figuras[i]
                    
        #Se apreta para dejar de mover la figura
        if boton3:
            activate = False
        
        #Si activate es True, la figura cambia de posición
        if activate:
            aux.setPos(x,y)
        
        surface.fill((237, 187, 153))
        #Se pintan todas las figuras
        for i in range(len(Figuras)):
            Figuras[i].draw(surface)
    
        screen.update()
        
    
main()