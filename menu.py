import pygame, sys
import webbrowser
from pygame.locals import *
from single_linked_list import SingleLinkedList
from ComboBox import ComboBox
inst=SingleLinkedList()
class main:
    def __init__(self):
        pygame.init()
        self.window_size=(1280,720)
        self.window= pygame.display.set_mode(self.window_size)
        self.gray_color=(211,211,211)
        self.white_color=(255,255,255)
        self.black_color=(0,0,0)
        self.blue_color=(0,0,255)
        self.font=pygame.font.SysFont('Times New Roman',16)
        self.darius_image = pygame.image.load("Archivos/darius.jpg")
        self.katarina_image = pygame.image.load("Archivos/katarina.jpg")
        self.leeSin_image = pygame.image.load("Archivos/leeSin.jpg")
        self.warwick_image = pygame.image.load("Archivos/warwick.jpg")
        self.uam_image = pygame.image.load("Archivos/UAM.png")
        self.github_image = pygame.image.load("Archivos/github.png")
        self.options_image = pygame.image.load("Archivos/menu.png")
        self.arbol_image = pygame.image.load("Archivos/arbol.png")
        self.nodo_image= pygame.image.load("Archivos/nodo.png")
        self.combo_functions_rect= pygame.Rect(351,185,242,37)
        self.combo= ComboBox(self.window,['Añadir al inicio','Añadir al final','Eliminar al inicio','Eliminar al final','Invertir la lista', 'Eliminar todos los elementos','Eliminar por posicion','Añadir por posicion','Actualizar valor','Unir Duplicados','Eliminar Duplicados'],self.combo_functions_rect,self.white_color,'Times New Roman',16,20,self.black_color,self.black_color,40,' ')
        self.combo_selected= False
        self.combo_pos_rect= pygame.Rect(862,185,50,37)
        self.combo_pos= ComboBox(self.window,['1','2','3','4','5','6'],self.combo_pos_rect,self.white_color,'Times New Roman',16,20,self.black_color,self.black_color,40,' ')
        self.combo_pos_selected= False
        self.initial_window = True
        self.click_button= False
        self.rect_aux= None
        self.node_aux= None
        self.github_rect= pygame.Rect(850,665,38,36)


    def run_app(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                if self.initial_window:
                    self.initial()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_pos= pygame.mouse.get_pos()
                        self.click_on_head()
                else:
                    self.draw_sll_window()
                    self.combo.draw()
                    self.combo_pos.draw()
            pygame.display.flip()    
            
    def rectGroup(self):
        self.darius_rect = pygame.Rect(209,265,150,88)
        self.katarina_rect = pygame.Rect(409,265,150,88)
        self.leeSin_rect = pygame.Rect(609,265,150,88)  
        self.warwick_rect = pygame.Rect(809,265,150,88)
                       
        
    def text(self):
        pygame.display.set_caption('League Of Legends Champs List')
        self.font.set_bold(True)
        sll_text= self.font.render('Single Linked List', True, self.white_color)
        self.font.set_bold(False)
        status_text= self.font.render('Estado de la lista: ', True,self.white_color)
        copyright_text= self.font.render('Desarrollado por : Johan Steven Polo Nieto',True,self.black_color)
        copyright_2_text= self.font.render('TAD I SEM -2023',True,self.white_color)
        sll_option= self.font.render('SLL',True,self.white_color)
        dll_option= self.font.render('DLL',True,self.white_color)
        pyc_option= self.font.render('PILAS Y COLAS',True,self.white_color)
        arbol_option= self.font.render('ÁRBOL',True,self.white_color)
        grafo_option= self.font.render('GRAFO',True,self.white_color)
        self.window.blit(sll_option,(89,30))
        self.window.blit(dll_option,(312,30))
        self.window.blit(pyc_option,(540,30))
        self.window.blit(arbol_option,(874,30))
        self.window.blit(grafo_option,(1134,30))
        self.window.blit(sll_text,(154,133))
        self.window.blit(status_text,(154,423))
        self.window.blit(copyright_text,(485,661))
        self.window.blit(copyright_2_text,(569,683))
        self.window.blit(self.options_image,(40,27))
        self.window.blit(self.options_image,(254,27))
        self.window.blit(self.options_image,(485,27))
        self.window.blit(self.arbol_image,(822,27))
        self.window.blit(self.options_image,(1082,27))
        
        
    def draw_init_window(self):
        self.window.fill(self.black_color)
        self.top_rect=pygame.draw.rect(self.window,self.black_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1020,159),0,20)
        self.darius_rect_initial = pygame.Rect(418,271,114,135)
        self.katarina_rect_initial = pygame.Rect(608,271,114,135)
        self.leeSin_rect_initial = pygame.Rect(798,271,114,135)  
        self.text()
        init_text= self.font.render('SELECCIONA LA CABEZA DE LA LISTA',True, self.black_color)
        self.window.blit(init_text,(341,220))
        self.window.blit(self.darius_image, (418,271))
        self.window.blit(self.katarina_image,(608,271))
        self.window.blit(self.leeSin_image,(798,271))
        self.window.blit(self.uam_image,(1188,658))
        self.window.blit(self.github_image,(850,665))       
    
    def draw_sll_window(self):
        self.window.fill(self.black_color)
        self.top_rect=pygame.draw.rect(self.window,self.black_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.black_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.black_color,(154,460,1044,159),0,20)
        self.button_rect= pygame.draw.rect(self.window,self.white_color,(959,185,129,38),0,20)
        self.text()
        agree_text= self.font.render('Aceptar', True,self.black_color)
        methods_text= self.font.render('Seleccione un método: ',True,self.white_color)
        pos_text= self.font.render('Seleccione una posición: ',True,self.white_color)
        pygame.draw.rect(self.window,self.white_color,self.combo_functions_rect,0,20)
        pygame.draw.rect(self.window,self.white_color,self.combo_pos_rect,0,20)
        self.window.blit(methods_text,(154,192))
        self.window.blit(pos_text,(666,192))
        self.window.blit(agree_text,(990,192))
        self.window.blit(self.darius_image, (209,265))
        self.window.blit(self.katarina_image,(409,265))
        self.window.blit(self.leeSin_image,(609,265))
        self.window.blit(self.warwick_image,(809,265))
        self.window.blit(self.uam_image,(818,628))
        self.window.blit(self.github_image,(910,628)) 
        self.rectGroup()
        self.visual_list() 
        self.select_image()
        
        
        
    
    def initial(self):
        self.window.fill(self.white_color)
        self.top_rect=pygame.draw.rect(self.window,self.white_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1020,159),0,20)
        self.darius_rect_initial = pygame.Rect(418,271,114,135)
        self.katarina_rect_initial = pygame.Rect(608,271,114,135)
        self.leeSin_rect_initial = pygame.Rect(798,271,114,135)  
        self.text()
        init_text= self.font.render('SELECCIONA LA CABEZA DE LA LISTA',True, self.black_color)
        self.window.blit(init_text,(341,220))
        self.window.blit(self.darius_image, (418,271))
        self.window.blit(self.katarina_image,(608,271))
        self.window.blit(self.leeSin_image,(798,271))
        self.window.blit(self.uam_image,(1188,658))
        self.window.blit(self.github_image,(850,665))
        self.visual_list() 
        
        
        
    
    def click_on_head(self):
        mouse_pos= pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.darius_rect_initial.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('darius')
                inst.show_list()
                self.initial_window = False
            if self.katarina_rect_initial.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('katarina')
                inst.show_list()
                self.initial_window = False
            if self.leeSin_rect_initial.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('leeSin')
                inst.show_list()
                self.initial_window = False

    def visual_list(self):
        gap=0
        for i in range(1,inst.length+1):
            if inst.get_node_value(i) == 'darius':
                self.window.blit(self.darius_image, (164+gap,472))
            if inst.get_node_value(i) == 'katarina':
                self.window.blit(self.katarina_image,(164+gap,472))
            if inst.get_node_value(i) == 'leeSin':
                self.window.blit(self.leeSin_image,(164+gap,472))
            if inst.get_node_value(i) == 'warwick':
                self.window.blit(self.warwick_image,(164+gap,472)) 
            gap+=140
            



    def select_image(self):
        if pygame.mouse.get_pressed()[0]:
            if self.darius_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'darius'
                print('Nodo D seleccionado')
            if self.katarina_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'katarina'
                print('Nodo K seleccionado')
            if self.leeSin_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'leeSin'
                print('Nodo L seleccionado')
            if self.warwick_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'warwick'
                print('Nodo W seleccionado')
            
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                print('click en el boton')
                if self.combo.getIndex()== 1:
                    if self.node_aux is not None:                        
                        inst.create_node_sll_unshift(self.node_aux)
                        self.node_aux=None
                        inst.show_list()
                        
                if self.combo.getIndex()== 2:
                    if self.node_aux is not None:
                        inst.create_node_sll_ends(self.node_aux)
                        self.node_aux=None
                        inst.show_list()
                if self.combo.getIndex()== 3:
                    inst.shift_node_sll()
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()== 4:
                    inst.delete_node_sll_pop()
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()== 5:
                    inst.reverse()
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()==6:
                    inst.remove_node_list()
                    self.node_aux=None
                    inst.show_list()
                    
                if self.combo.getIndex()==7:
                    inst.remove_node_index(self.combo_pos.getIndex())
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()==8:
                    if self.node_aux is not None:
                        inst.insert_on_index(self.combo_pos.getIndex(),self.node_aux)
                        self.node_aux=None
                        inst.show_list()
                        
                if self.combo.getIndex()==9:
                    if self.node_aux is not None:
                        inst.update_node_value(self.combo_pos.getIndex(),self.node_aux)
                        self.node_aux=None
                        inst.show_list()
                if self.combo.getIndex()==10:
                    print("duplicados")
                    self.node_aux=None
                    inst.duplicados()
                    inst.show_list()
                if self.combo.getIndex()==11:
                    if self.node_aux is not None:
                        inst.eliminarDuplicados(self.combo_pos.getIndex(),self.node_aux)
                        self.node_aux=None
                        inst.show_list()
            
            