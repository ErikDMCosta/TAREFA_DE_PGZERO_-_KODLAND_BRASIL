import pgzrun  # importa Pygame Zero, framework simplificado para jogos em Python
import random   # importa módulo para gerar números aleatórios

WIDTH = 800  # largura da janela do jogo
HEIGHT = 600  # altura da janela do jogo

# Cria ator para o fundo, usando a imagem 'background'
bg = Actor("background")

# Cria ator para a nave do jogador e posiciona no centro inferior
ship = Actor('ship')  # Carrega imagem 'ship'
ship.x = 400  # posição horizontal inicial (metade de WIDTH)
ship.y = 550  # posição vertical inicial (próximo à base)

# Cria ator para o ponto extra que dá pontuação
extrapoint = Actor('extrapoint')  # Carrega imagem 'extrapoint'
extrapoint.x = random.randint(20, 780)  # define x aleatório entre as bordas
extrapoint.y = 0  # inicia no topo da tela

# Cria ator para o inimigo
enemy = Actor('enemy')  # Carrega imagem 'enemy'
enemy.x = random.randint(20, 780)  # posição horizontal aleatória
enemy.y = 0  # inicia no topo

# Cria ator para o asteroide
asteroid = Actor('asteroid')  # Carrega imagem 'asteroid'
asteroid.x = random.randint(20, 780)  # posição horizontal aleatória
asteroid.y = 0  # inicia no topo

# Estado do jogo: pontuação, vidas e flags\score = 0  # pontuação inicial
score = 0  # pontuação marcada durante o jogo
lives = 3  # número de vidas iniciais
game_over = False  # flag para indicar fim de jogo
deathsound = False # controla execução de som de morte

# Imprime pontuação e vidas iniciais no console
print('Recorde: ', score)
print('Vidas: ', lives)

def update():
    global score, lives, game_over, deathsound  # permite alterar variáveis globais

    # Movimento da nave: esquerda/direita sem ultrapassar bordas
    if keyboard.left and ship.x > 30:
        ship.x -= 5  # move para a esquerda
    elif keyboard.right and ship.x < 770:
        ship.x += 5  # move para a direita

    # Atualiza posição do ponto extra: velocidade aumenta com a pontuação
    extrapoint.y += 4 + score / 5  # desce em direção à base
    if extrapoint.y > 600:
        # se sair da tela, reposiciona no topo com x aleatório
        extrapoint.x = random.randint(20,700)
        extrapoint.y = 0

    # Verifica colisão entre nave e ponto extra
    if extrapoint.colliderect(ship):
        sounds.collect.play()  # toca som de coleta
        # reposiciona ponto extra e incrementa pontuação
        extrapoint.x = random.randint(20,700)
        extrapoint.y = 0
        score += 1
        print('Recorde: ', score)  # exibe nova pontuação

    # Atualiza posição do asteroide: velocidade constante
    asteroid.y += 4
    if asteroid.y > 600:
        # reposiciona se sair da tela
        asteroid.x = random.randint(20,700)
        asteroid.y = 0

    # Checa colisão entre nave e asteroide
    if asteroid.colliderect(ship):
        sounds.losing.play()  # toca som de perda
        asteroid.x = random.randint(20,700)
        asteroid.y = 0
        # deduz ponto somente se pontuação > 0
        score -= 1 if score > 0 else 0
        print('Recorde: ', score)  # exibe pontuação atual

    # Atualiza posição do inimigo: velocidade um pouco maior
    enemy.y += 5
    if enemy.y > 600:
        # reposiciona no topo
        enemy.x = random.randint(20,700)
        enemy.y = 0

    # Verifica colisão entre nave e inimigo
    if enemy.colliderect(ship):
        sounds.explosion.play()  # toca som de explosão
        enemy.x = random.randint(20,700)
        enemy.y = 0
        # reduz uma vida se ainda houver vidas
        lives -= 1 if lives > 0 else 0
        print('Vidas: ', lives)  # exibe vidas restantes

    # Se não houver mais vidas, define fim de jogo
    if lives == 0:
        game_over = True  # ativa flag de fim de jogo
        deathsound = True
        # reseta posição vertical dos elementos para parar movimento
        extrapoint.y = 0
        enemy.y = 0
        asteroid.y = 0
        # toca som de morte apenas uma vez
        if deathsound == False:
            sounds.losing.play()
        deathsound = True

def draw():
    # desenha fundo
    bg.draw()

    if game_over:
        # exibe tela de fim de jogo
        screen.draw.text('FIM DE JOGO', (230, 200), color="white", fontname='publicpixel', fontsize=30)
        screen.draw.text('RECORDE FINAL: ' + str(score), (180, 300), color="lightblue", fontname='publicpixel', fontsize=15)
    else:
        # desenha elementos enquanto o jogo não terminou
        ship.draw()         # desenha nave
        extrapoint.draw()   # desenha ponto extra
        enemy.draw()        # desenha inimigo
        asteroid.draw()     # desenha asteroide
        # exibe HUD com pontuação e vidas
        screen.draw.text('Recorde: ' + str(score), (15, 10), color="lightblue", fontname='publicpixel', fontsize=15)
        screen.draw.text('Vidas: ' + str(lives), (665, 10), color="yellow", fontname='publicpixel', fontsize=15)

# inicia o loop principal do jogo
pgzrun.go()
