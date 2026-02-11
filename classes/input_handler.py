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
        Args: 
           events: події, що надходять
        """
        result = {} #список результатів

        for event in events:
            if event.type == pygame.QUIT:
                result['quit'] = True
                return result  
            
        keys = pygame.key.get_pressed()
        
        if self.player is not None:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move_left()

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move_right()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    if self.game is not None:
                        self.game.is_paused = not self.game.is_paused
                    result['pause_toggle'] = True

        return result