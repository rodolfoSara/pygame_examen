import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_C import FormMenuC
from gui_form_menu_niveles import FormMenuNiveles
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l3 import FormGameLevel3

from gui_form_volume import FormVolumen

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(255,255,0),color_border=(255,0,255),active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=600,y=200,w=300,h=400,color_background=None,color_border=None,active=False)
form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

form_menu_niveles = FormMenuNiveles(name="form_menu_niveles",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

form_game_L3 = FormGameLevel3(name="a",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

#form_volumen = FormVolumen(name="form_volumen",master_surface = screen,x=600,y=400,w=250,h=250,color_background=(0,255,255),color_border=(255,0,255),active=False)

# musica
pygame.mixer.music.load("sound/track 2.ogg")
# -1 play in loop always
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


while True:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    if(aux_form_active != None):
        aux_form_active.update(lista_eventos,keys,delta_ms)
        aux_form_active.draw()



    pygame.display.flip()




    


  



