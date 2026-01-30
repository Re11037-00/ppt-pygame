import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

estado = 'menu'
personagem = 0

# fundos 
tela_inicial = pygame.image.load('assets/tela_inicial.jpeg').convert()  # Imagem de tela inicial
tela_inicial = pygame.transform.scale(tela_inicial, (640, 480))
tela_selecao_p1 = pygame.image.load('assets/p1_selecionado.jpeg').convert()  # Seleção P1
tela_selecao_p1 = pygame.transform.scale(tela_selecao_p1, (640, 480))
tela_selecao_p2 = pygame.image.load('assets/p2_selecionado.jpeg').convert()  # Seleção P2
tela_selecao_p2 = pygame.transform.scale(tela_selecao_p2, (640, 480))
bg_jogo_p1 = pygame.image.load('assets/p2_oponente.jpeg').convert()  # P2 como oponente
bg_jogo_p1 = pygame.transform.scale(bg_jogo_p1, (640, 480))
bg_jogo_p2 = pygame.image.load('assets/p1_oponente.jpeg').convert()  # P1 como oponente
bg_jogo_p2 = pygame.transform.scale(bg_jogo_p2, (640, 480))


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
        
        # Definir fundo
    if estado == 'menu':
        screen.blit(tela_inicial, (0, 0))
    elif estado == 'selecao_personagem':
        if personagem == 0:
            screen.blit(tela_selecao_p1, (0, 0))
        elif personagem == 1:
            screen.blit(tela_selecao_p2, (0, 0))
    elif estado == 'jogo':
        if personagem == 0:
            screen.blit(bg_jogo_p1, (0, 0))
        else:
            screen.blit(bg_jogo_p2, (0, 0))


  pygame.display.flip()
  clock.tick(60)

pygame.quit()
