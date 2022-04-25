from unicodedata import name
import pygame
import pygame_gui
from pygame_gui import elements
import time

def contact_page():
    pygame.init()
    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#1B2836'))

    #theme.json for the theme
    manager = pygame_gui.UIManager((800, 600), 'theme.json')
    
    #Rect((left, top), (width, height)) -> Rect
    back_button = elements.UIButton(relative_rect=pygame.Rect((20, 20), (70, 50)),
                                                text='back',
                                                manager=manager)
    
    accounts = ["discord", "gmail"]
    account_type_dropDownMenu = elements.UIDropDownMenu(options_list=accounts,
                                                        starting_option="choose account type",
                                                        relative_rect=pygame.Rect(90,100,225,30),
                                                        manager=manager)
    
    instruct_message = elements.UILabel(relative_rect=pygame.Rect(45,140,175,50),
                            manager=manager,
                            text="",
                            object_id='@message_label',
                            visible=0)

    error_message =  elements.UILabel(relative_rect=pygame.Rect(510,200,250,50),
                            manager=manager,
                            text="username cannot be empty",
                            object_id='@error_message_label',
                            visible=0)   
    
    success_message = elements.UILabel(relative_rect=pygame.Rect(480,200,250,50),
                            manager=manager,
                            text="success",
                            object_id='@message_label',
                            visible=0) 

    add_another_account_message = elements.UILabel(relative_rect=pygame.Rect(480,250,250,50),
                            manager=manager,
                            text="click add to add another account",
                            object_id='@message_label',
                            visible=0)

    input = elements.UITextEntryLine(relative_rect=pygame.Rect(45,200,375, 50),
                                    manager=manager,
                                    visible=0)

    add_button = elements.UIButton(pygame.Rect(415,200, 70, 50),
                                    text='ADD',
                                    visible=0,
                                    manager=manager)
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        time_delta = clock.tick(60)/1000.0
        manager.set_text_input_hovered(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quitting')
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    print("pressed back")
                    is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == add_button:
                if input.get_text() != "":
                    print(input.get_text())
                    account_type_dropDownMenu.enable()
                    success_message.visible = 1
                    add_button.visible = 1
                    success_message.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)
                    add_another_account_message.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)
                    print("success")
                    input.set_text("")
                    
                
                else:
                    print("error")
                    error_message.visible = 1
                    error_message.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)
            
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == account_type_dropDownMenu:
                    selected = account_type_dropDownMenu.selected_option
                    print(selected)
                    account_type_dropDownMenu.disable()
                    instruct_message.set_text(f"enter {selected} username")
                    instruct_message.visible = 1
                    input.visible = 1
                    add_button.visible = 1
                

            
            
            manager.process_events(event)

        

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()

if __name__ == '__main__':
    contact_page()