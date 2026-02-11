import pygame
class InputHandler:
    def __init__(self, player=None, game=None):
        self.player = player
        self.game = game

    def handle_input(self, events: list[pygame.event.Event]) -> dict:
        result = {}  # словник з діями, які потрібно обробити в Game
        
        for event in events:
            if event.type == pygame.QUIT:
                result['quit'] = True
                return result  # можна одразу вийти
            
        keys = pygame.key.get_pressed()
        
        if self.player is not None:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move_left()

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move_right()

        return result