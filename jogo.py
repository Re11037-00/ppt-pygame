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

        elif estado == 'vitoria' and event.key == pygame.K_RETURN or estado == 'derrota' and event.key == pygame.K_RETURN:
            estado = 'menu'

    #seleção de personagem
        elif estado == 'selecao_personagem':
            if event.key == pygame.K_LEFT:
                personagem = 0 #personagem da esquerda
            elif event.key == pygame.K_RIGHT:
                personagem = 1 #personagem da direita
            elif estado == 'selecao_personagem' and event.key == pygame.K_RETURN:
                estado = 'jogo'  #inicia o jogo
        
    #lógica do jogo
        elif estado == 'jogo': 
            if rodada_ativa:
                escolha_jogador = None
                escolha_computador = None
                rodada_ativa = False
                linha1 = ''
                linha2 = ''
                linha3 = ''
                linha4 = ''
            else:
                #controles
                if event.key == pygame.K_LEFT:
                    escolha_jogador = 'pedra'
                elif event.key == pygame.K_UP:
                    escolha_jogador = 'papel'
                elif event.key == pygame.K_RIGHT:
                    escolha_jogador = 'tesoura'
                
                if escolha_jogador != None:
                    rodada_ativa = True
                    escolha_computador = random.choice(opcoes)  

                    #empate
                    if escolha_jogador == escolha_computador:
                        resultado = 'Empate!'

                    #vitória
                    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or (escolha_jogador == 'papel' and escolha_computador == 'pedra') or (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
                        resultado = 'Vitória!'
                        pontos_jogador = pontos_jogador + 1
                        pontos_computador = pontos_computador - 1

                    #derrota
                    else:
                        resultado = 'Derrota!'
                        pontos_jogador = pontos_jogador - 1
                        pontos_computador = pontos_computador + 1

                    #atualizar balão de fala
                    linha1 = f'Pontos - Jogador: {pontos_jogador} | Computador: {pontos_computador}'
                    linha2 = f'Jogador: {escolha_jogador}'
                    linha3 = f'Computador: {escolha_computador}'
                    linha4 = f'Resultado: {resultado}'
    
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
