import pygame


class InputHandler:
    """
    Клас для обробки введень користувача
    """
    def __init__(self, player=None, game=None):
        """
        Конструктор класу
        """
        self.player = player
        self.game = game

    def handle_input(self, events: list[pygame.event.Event]) -> dict:
        """
        Метод обробки отриманих даних
        
        :param self: об'єкт керування
        :param events: список оброблюваних подій
        :type events: list[pygame.event.Event]
        :return: словник з діями на виконання
        :rtype: dict
        """
        result = {
            "quit": False,
            "enter": False,
            "escape": False,
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "pause_toggle": False
        }

        # Обробка подій KEYDOWN та QUIT
        for event in events:
            if event.type == pygame.QUIT:
                result["quit"] = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    result["enter"] = True
                elif event.key == pygame.K_ESCAPE:
                    result["escape"] = True
                elif event.key == pygame.K_UP:
                    result["up"] = True
                elif event.key == pygame.K_DOWN:
                    result["down"] = True
                elif event.key == pygame.K_LEFT:
                    result["left"] = True
                elif event.key == pygame.K_RIGHT:
                    result["right"] = True
                elif event.key == pygame.K_p:
                    result["pause_toggle"] = True

        if self.player:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.player.move_left()
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.player.move_right()

        return result
