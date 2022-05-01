from pip import main
import pygame
import pygame_gui
from pygame_gui import elements
from GUI_contact import contact_page
from csv_handler import *
from back_end import *

pygame.init()
pygame.display.set_caption('All in One messaging tool')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#1B2836'))

#theme.json for the theme
manager = pygame_gui.UIManager((800, 600), 'theme.json')


#Rect((left, top), (width, height)) -> Rect
send_button = elements.UIButton(relative_rect=pygame.Rect((500, 200), (100, 50)),
                                            text='SEND',
                                            manager=manager,)

add_button = elements.UIButton(relative_rect=pygame.Rect((500, 280), (150, 50)),
                                            text='ADD CONTACT',
                                            manager=manager)

text_input = elements.UITextEntryLine(relative_rect=pygame.Rect(100, 200,375,50),
                                        manager=manager)

message = elements.UILabel(relative_rect=pygame.Rect(5,150,375,50),
                            text="sending message...",
                            manager=manager,
                            object_id='@message_label',
                            visible=0)

error_message = elements.UILabel(relative_rect=pygame.Rect(5,150,375,50),
                            text="error",
                            manager=manager,
                            object_id='@error_message_label',
                            visible=0)
contacts = import_contacts_names()
user_dropdown_menu = elements.UIDropDownMenu(relative_rect=pygame.Rect(100, 260, 200, 50),
                                            starting_option="send to...",
                                            manager=manager,
                                            options_list=contacts)

error_discord_message = elements.UILabel(relative_rect=pygame.Rect(100,340,375,50),
                            text="fail! did not send message to user's discord",
                            manager=manager,
                            object_id='@error_message_label',
                            visible=0)

success_discord_message = elements.UILabel(relative_rect=pygame.Rect(100,340,375,50),
                            text="successfully sent message to user's discord",
                            manager=manager,
                            object_id='@message_label',
                            visible=0)

error_email_message = elements.UILabel(relative_rect=pygame.Rect(100,370,375,50),
                            text="fail! did not send message to user's email",
                            manager=manager,
                            object_id='@error_message_label',
                            visible=0)

success_email_message = elements.UILabel(relative_rect=pygame.Rect(100,370,375,50),
                            text="successfully sent message to user's email",
                            manager=manager,
                            object_id='@message_label',
                            visible=0)

def main_page():
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        time_delta = clock.tick(60)/1000.0
        manager.set_text_input_hovered(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == add_button:
                    contact_page()
                    contacts = import_contacts_names()
                    user_dropdown_menu.update_options_list(contacts)
                    

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == user_dropdown_menu:
                    user_dropdown_menu.disable()
                    selected = user_dropdown_menu.selected_option
                    add_button.disable()
                    print(selected)
                    send_button.enable()
            
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED or event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == text_input or event.ui_element == send_button:
                    if text_input.get_text()!= "" and user_dropdown_menu.selected_option != "send to...":
                        print(user_dropdown_menu.selected_option)
                        print(text_input.get_text())
                        reciever = user_dropdown_menu.selected_option
                        input_message = text_input.get_text()
                        text_input.set_text("")
                        #disable buttons while sinding
                        text_input.disable()
                        send_button.disable()
                        
                        
                        contact_details = import_contact_detals(reciever)
                        sending_to_discord = send_to_discord(contact_details["dicord_username"],msg=input_message)
                        if sending_to_discord:
                            success_discord_message.visible = 1
                        else:
                            error_discord_message.visible = 1

                        print(contact_details["dicord_username"])
                        sending_to_email = send_email(msg=input_message, reciever=contact_details["email_address"])
                        
                        if sending_to_email:
                            success_email_message.visible = 1
                        else:
                            error_email_message.visible = 1


                            
                        #enable buttons after sending
                        add_button.enable()
                        user_dropdown_menu.enable()
                        text_input.enable()

                    elif text_input.get_text()!= "" and user_dropdown_menu.selected_option == "send to...":
                        error_message.set_text("error: contact not selected")
                        error_message.visible = 1
                        error_message.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)

                    else:
                        error_message.set_text("error: message cannot be empty")
                        error_message.visible = 1
                        error_message.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)
            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()

if __name__ == '__main__':
    main_page()
