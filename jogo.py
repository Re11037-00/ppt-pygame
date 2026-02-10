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
escolha_computador = None

pontos_jogador = 5
pontos_computador = 5

rodada_ativa = False

#balão de fala
linha1 = '' #pontuação
linha2 = '' #jogador
linha3 = '' #computador
linha4 = '' #resultado

# fundos 

# Imagem de tela inicial
tela_inicial = pygame.image.load('assets/tela_inicial.jpeg').convert()  
tela_inicial = pygame.transform.scale(tela_inicial, (640, 480))

# Seleção P1
tela_selecao_p1 = pygame.image.load('assets/p1_selecionado.jpeg').convert()  
tela_selecao_p1 = pygame.transform.scale(tela_selecao_p1, (640, 480))

 # Seleção P2
tela_selecao_p2 = pygame.image.load('assets/p2_selecionado.jpeg').convert() 
tela_selecao_p2 = pygame.transform.scale(tela_selecao_p2, (640, 480))

# P2 como oponente
bg_jogo_p1 = pygame.image.load('assets/p2_oponente.jpeg').convert()  
bg_jogo_p1 = pygame.transform.scale(bg_jogo_p1, (640, 480))

# P1 como oponente
bg_jogo_p2 = pygame.image.load('assets/p1_oponente.jpeg').convert()  
bg_jogo_p2 = pygame.transform.scale(bg_jogo_p2, (640, 480))

#vitoria
vitoria = pygame.image.load('assets/vitoria.png').convert()
vitoria = pygame.transform.scale(vitoria, (640, 480))

#derrota
derrota = pygame.image.load('assets/derrota.png').convert()
derrota = pygame.transform.scale(derrota, (640, 480))

#loop do jogo
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    elif event.type == pygame.KEYDOWN:  

    #jogo fechará se apertar esc
        if event.key == pygame.K_ESCAPE:
            running = False  

    #jogo abrirá menu de seleção se apertar enter
        elif estado == 'menu' and event.key == pygame.K_RETURN:
            estado = 'selecao_personagem' 

    #seleção de personagem
        elif estado == 'selecao_personagem':
            if event.key == pygame.K_LEFT:
                personagem = 0 #personagem da esquerda
            elif event.key == pygame.K_RIGHT:
                personagem = 1 #personagem da direita

    #inicia o jogo
        elif estado == 'selecao_personagem' and event.key == pygame.K_RETURN:
                estado = 'jogo'  
        
    #controles + lógica do jogo
        elif estado == 'jogo': 


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
    
    #definir tela
    if estado == 'menu':
        screen.blit(tela_inicial, (0, 0))

    elif estado == 'selecao_personagem':
        if personagem == 0:
            screen.blit(tela_selecao_p1, (0, 0))
        elif personagem == 1:
            screen.blit(tela_selecao_p2, (0, 0))

    elif estado == 'jogo':
        screen.blit(bg_jogo_p1 if personagem == 0 else bg_jogo_p2, (0, 0))

        #balão de fala + texto
        pygame.draw.rect(screen, (0, 0, 0), (20, 330, 600, 130)) #balão de fala
        y = 340
        for linha in [linha1, linha2, linha3, linha4]: #texto do balão de fala
            texto = font.render(linha, True, (255, 255, 255))
            screen.blit(texto, (30, y))
            y += 30
        if pontos_computador == 0:
            estado = 'vitoria'
        elif pontos_jogador == 0:
            estado = 'derrota'
            
    elif estado == 'vitoria':
        screen.blit(vitoria, (0, 0))    
    elif estado == 'derrota':
        screen.blit(derrota, (0, 0))


    


  pygame.display.flip()
  clock.tick(60)

pygame.quit()
