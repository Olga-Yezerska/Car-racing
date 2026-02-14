import pygame
class InputHandler:
    """
    Клас для обробки введень користувача
    """
    def init(self, player=None, game=None):
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
        result = {}
        
        for event in events:
            if event.type == pygame.QUIT:
                result["quit"] = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    result["select_1"] = True
                if event.key == pygame.K_2:
                    result["select_2"] = True
                if event.key == pygame.K_ESCAPE:
                    result["escape"] = True
                if event.key == pygame.K_RIGHT:
                    result["right"] = True
                if event.key == pygame.K_LEFT:
                    result["left"] = True
                if event.key == pygame.K_UP:
                    result["up"] = True
                if event.key == pygame.K_DOWN:
                    result["down"] = True
                if event.key == pygame.K_m:
                    result["music"] = True
                if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    result["pause_toggle"] = True

        keys = pygame.key.get_pressed()
        if self.player:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.player.move_left()

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.player.move_right()
        return result