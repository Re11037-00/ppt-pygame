import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

estado = 'menu'
personagem = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    elif event.type == pygame.KEYDOWN:  

        if event.key == pygame.K_ESCAPE:
            running = False  #jogo fechará se apertar esc

        elif estado == 'menu' and event.key == pygame.K_RETURN:
            estado = 'selecao_personagem' #jogo abrirá menu de seleção se apertar enter
        

        if estado == 'menu':
            screen.fill((255, 255, 255))
    

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
