import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 36)

#variaveis
estado = 'menu'
personagem = 0
opcoes = ['pedra', 'papel', 'tesoura']
escolha_jogador = None
escolha_computador = random.choice(opcoes)
pontos_jogador = 5
pontos_computador = 5
resultado = 0

#balão de fala
mensagem = ""
texto = font.render(mensagem, True, (255, 255, 255))

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
        
            if estado == 'jogo': #controles do jogo
                if event.key == pygame.K_LEFT:
                    escolha_jogador = 'pedra'
                elif event.key == pygame.K_UP:
                    escolha_jogador = 'papel'
                elif event.key == pygame.K_RIGHT:
                    escolha_jogador = 'tesoura' 


        if escolha_jogador == escolha_computador: #lógica do jogo
            resultado = 'empate'
        elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or (escolha_jogador == 'papel' and escolha_computador == 'pedra') or (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
            resultado = 'vitoria'
            pontos_jogador += 1
            pontos_computador -= 1
        else:
            resultado = 'derrota'
            pontos_jogador -= 1
            pontos_computador += 1


        # if estado == 'jogo': #'texto no balão de fala'
        #     mensagem = f'você escolheu {escolha_jogador} computador escolheu {escolha_computador}. Resultado: {resultado}! Pontos - Você: {pontos_jogador}, Computador: {pontos_computador}'

        if estado == 'jogo' and (pontos_jogador == 0 or pontos_computador == 0):
            estado = 'menu'  #volta para o menu se algum jogador chegar a 0 pontos
            pontos_jogador = 5
            pontos_computador = 5
            mensagem = ""

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

    #criar balão
    if estado == 'jogo':
        # texto = font.render(mensagem, True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (20, 350, 600, 100))
        screen.blit(texto, (30, 360))


  pygame.display.flip()
  clock.tick(60)

pygame.quit()
