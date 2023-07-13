import pygame
from pygame.locals import *

from background import Background
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenuNiveles(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=200,y=100,w=300,h=200,color_background=C_BLACK,color_border=None,image_background=None,on_click=self.on_click_boton_cambiar_nivel,on_click_param ="form_game_L1",text="Nivel 1",font="Helvetica",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self, x=200, y=303, w=300, h=200, color_background=C_BLACK, color_border=None,
                             image_background=None, on_click=self.on_click_boton_cambiar_nivel,
                             on_click_param="form_game_L1", text="Nivel 2", font="Helvetica", font_size=30,
                             font_color=C_WHITE)
        self.boton3 = Button(master=self, x=200, y=505, w=300, h=200, color_background=C_BLACK, color_border=None,
                             image_background=None, on_click=self.on_click_boton_cambiar_nivel,
                             on_click_param="form_game_L3", text="Nivel 3", font="Helvetica", font_size=30,
                             font_color=C_WHITE)


        
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

        self.static_background = Background(x=0, y=0, width=w, height=h, path="images/locations/fondo1.png")

    def on_click_boton_cambiar_nivel(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:
            aux_widget.draw()
