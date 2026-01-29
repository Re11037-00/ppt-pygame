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

        elif estado == 'selecao_personagem':
            if event.key == pygame.K_LEFT:
                personagem = 0 #personagem da esquerda
            elif event.key == pygame.K_RIGHT:
                personagem = 1 #personagem da direita

            elif estado == 'selecao_personagem' and event.key == pygame.K_RETURN:
                estado = 'jogo'  #inicia o jogo

        if estado == 'menu':
            screen.fill((255, 255, 255))
        
        #Teste da funcionalidade do menu de seleção de personagem
        elif estado == 'selecao_personagem':
            if personagem == 0:
                screen.fill((0, 0, 255)) #azul para representar personagem esquerdo
            elif personagem == 1:
                screen.fill((255, 0, 0)) #vermelho para representar personagem direito
        elif estado == 'jogo':
            screen.fill((0, 255, 0)) #tela fica verde após selecionar um dos personagens
            


  pygame.display.flip()
  clock.tick(60)

pygame.quit()
