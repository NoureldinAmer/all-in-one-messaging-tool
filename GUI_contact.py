from unicodedata import name
import pygame
import pygame_gui
from pygame_gui import elements
import time

def contact_page():
    #method will return a 2d array of users
    users = []
    user = {}
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
    
    add_another_user_button = elements.UIButton(relative_rect=pygame.Rect((190, 20), (200, 50)),
                                                text='add another user',
                                                manager=manager)

    save_button = elements.UIButton(relative_rect=pygame.Rect((100, 20), (70, 50)),
                                                text='save',
                                                manager=manager)

    accounts = ["discord", "gmail"]
    account_type_dropDownMenu = elements.UIDropDownMenu(options_list=accounts,
                                                        starting_option="choose account type",
                                                        relative_rect=pygame.Rect(90,200,225,30),
                                                        manager=manager,
                                                        visible=1)
    #account_type_dropDownMenu is enabled once name is entered successfully
    account_type_dropDownMenu.disable()
    
    instruct_message = elements.UILabel(relative_rect=pygame.Rect(45,240,175,50),
                            manager=manager,
                            text="",
                            object_id='@message_label',
                            visible=0)

    error_message =  elements.UILabel(relative_rect=pygame.Rect(510,300,250,50),
                            manager=manager,
                            text="username cannot be empty",
                            object_id='@error_message_label',
                            visible=0)   
    
    success_message = elements.UILabel(relative_rect=pygame.Rect(480,300,250,50),
                            manager=manager,
                            text="success",
                            object_id='@message_label',
                            visible=0) 

    add_another_account_message = elements.UILabel(relative_rect=pygame.Rect(45,261,200,50),
                            manager=manager,
                            text="click add to add another account",
                            object_id='@message_label',
                            visible=0)

    input = elements.UITextEntryLine(relative_rect=pygame.Rect(45,300,375, 50),
                                    manager=manager,
                                    visible=0)

    add_button = elements.UIButton(pygame.Rect(415,300, 70, 50),
                                    text='ADD',
                                    visible=0,
                                    manager=manager)
    
    name_input = elements.UITextEntryLine(relative_rect=pygame.Rect(45,120,375, 50),
                                    manager=manager,
                                    visible=1)
    
    name_instruct_message = elements.UILabel(relative_rect=pygame.Rect(45,75,275,50),
                            manager=manager,
                            text="enter the name of your contact",
                            object_id='@message_label',
                            visible=1)

    name_add_button = elements.UIButton(pygame.Rect(415,120, 70, 50),
                                    text='ADD',
                                    visible=1,
                                    manager=manager)

    name_error_message =  elements.UILabel(relative_rect=pygame.Rect(510,120,250,50),
                            manager=manager,
                            text="username cannot be empty",
                            object_id='@error_message_label',
                            visible=0) 

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
                    return users
                
                if event.ui_element == add_another_user_button:
                    users.append(user)
                    user.clear()
                    account_type_dropDownMenu.disable()
                    name_input.set_text("")
                    input.visible = 0
                    instruct_message.visible = 0
                    add_button.visible = 0

                if event.ui_element == add_another_user_button:
                    users.append(user)
                    user.clear()

            if event.type == pygame_gui.UI_BUTTON_ON_HOVERED and event.ui_element == add_button:
                add_another_account_message.visible = 1
                add_another_account_message.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)

            #condition for if the user clicks the 'add' button to add a contact name 
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == name_add_button:
                if name_input.get_text() != "":
                    print(name_input.get_text())
                    print("success")
                    user.update({'name':name_input.get_text()})
                    account_type_dropDownMenu.enable()
                else:
                        print("error")
                        name_error_message.visible = 1
                        name_error_message.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)


            i = 0
            #condition for if the user clicks the 'add' button for the user name 
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == add_button:
                if input.get_text() != "":
                    print(input.get_text())
                    account_type_dropDownMenu.enable()
                    success_message.visible = 1
                    add_button.visible = 1
                    success_message.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)
                    #list storing all user details
                    user.update({f'account{i}':account_type_dropDownMenu.selected_option})
                    user.update({'username{i}':input.get_text()})
                    i+=1
                    #users.append(user)
                    print(user)
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