import pygame
import pygame_gui
from pygame_gui import elements
from GUI_contact import contact_page
import time


pygame.init()
pygame.display.set_caption('Quick Start')
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

message = elements.UILabel(relative_rect=pygame.Rect(100,260,375,50),
                            text="sending message...",
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
                    list_of_users = contact_page()
                    print(list_of_users)
            
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED or event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == text_input or event.ui_element == send_button:
                    print(text_input.get_text())
                    text_input.set_text("")
                    text_input.disable()
                    message.visible = 1
                    message.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()

if __name__ == '__main__':
    main_page()
