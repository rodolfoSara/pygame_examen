import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from background import Background



class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=735,y=103,w=200,h=100,color_background=C_BLACK,color_border=None,image_background=None, on_click=self.on_click_boton_niveles,on_click_param="",text="Niveles",font="Helvetica",font_size=30,font_color=C_WHITE)
        #self.boton2 = Button(master=self,x=20,y=80,w=140,h=50,color_background=None,color_border=None,image_background=None, on_click=self.on_click_boton2,on_click_param="",text="RESTA -",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=735,y=206,w=200,h=100,color_background=C_BLACK,color_border=None,image_background=None, on_click=self.on_click_boton3,on_click_param="form_game_L1",text="Jugar",font="Helvetica",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self, x=735, y=309, w=200, h=100, color_background=C_BLACK, color_border=None, image_background=None, on_click=self.on_click_boton3, on_click_param="form_game_L1", text="Volume", font="Helvetica", font_size=30, font_color=C_WHITE)
        self.boton4 = Button(master=self, x=735, y=412, w=200, h=100, color_background=C_BLACK, color_border=None, image_background=None, on_click=self.on_click_boton3, on_click_param="form_game_L1", text="Salir", font="Helvetica", font_size=30, font_color=C_WHITE)
        #self.boton4 = Button(master=self,x=20,y=200,w=140,h=50,color_background=None,color_border=None,image_background=None, on_click=self.on_click_boton3,on_click_param="form_menu_B",text="SQL",font="Verdana",font_size=30,font_color=C_WHITE)
        #self.boton5 = Button(master=self,x=20,y=200,w=140,h=50,color_background=C_GREEEN_2,color_border=None,image_background=None, on_click=self.on_click_boton3,on_click_param="form_menu_C",text="Vector",font="Helvetica",font_size=50,font_color=C_WHITE)

        #self.txt1 = TextBox(master=self,x=200,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",text="Text",font="Verdana",font_size=30,font_color=C_BLACK)
        #self.pb1 = ProgressBar(master=self,x=200,y=150,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 3, value_max=8)

        self.lista_widget = [self.boton1,self.boton2, self.boton3,self.boton4]

        self.static_background = Background(x=0, y=0, width=w, height=h, path="images/locations/fondo2.png")

    def on_click_boton_niveles(self, parametro):
        self.set_active("form_menu_niveles")

    """
    def on_click_boton2(self, parametro):
        self.pb1.value -= 1
    """
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:
            aux_widget.draw()