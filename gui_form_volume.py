import pygame
from pygame.locals import *

from background import Background
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_widget import Widget


class FormVolumen(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.volumeMenos = Widget(master_form=self, x=0, y=0, w=250, h=40, color_background=C_BLACK, color_border=None, image_background=r'D:\programacion cursos\UTN\python UTN\python utn ejercicios\11 pygame\my_pygame_2\CLASE_23_inicio_juego\images\volume\mas.png', text="Volumen", font="Helvetica", font_size=20, font_color=C_WHITE)


        self.lista_widget = [self.volumeMenos]




            





    def on_click_boton_cambiar_nivel(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

        # control de audio
        # low volume
        if keys[pygame.K_7] and pygame.mixer.music.get_volume() > 0.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume - 0.01)
            # screen.blit( self.volumeMenos , (850, 25))

        if keys[pygame.K_9] and pygame.mixer.music.get_volume() < 1.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume - 0.01)
            # screen.blit( self.volumeMenos , (850, 25))

    def draw(self):
        super().draw()

        for aux_widget in self.lista_widget:
            aux_widget.draw()
