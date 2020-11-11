from configparser import SafeConfigParser
import pygame
pygame.init()

class Screen:
    def __init__(self):
        parser = SafeConfigParser()
        parser.read('game.ini')

        self.game_size = [int(parser.get('GENERAL', 'game_size_w')), int(parser.get('GENERAL', 'game_size_h'))]
        self.screen = pygame.display.set_mode(self.game_size)
        self.background_color = (230, 230, 230)
    


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                    #player1.shoot()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass
            #player1.turn(-1)
        if keys[pygame.K_RIGHT]:
            pass
            #player1.turn(1)
        if keys[pygame.K_UP]:
            pass
            #player1.drive()
    

    def render(self, game):
        self.screen.fill(self.background_color)
        game.draw_player(game.player1, self.screen)
        game.draw_player(game.player2, self.screen)
        pygame.display.flip()
