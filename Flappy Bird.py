# Importando e inicializando o PyGame
import random

import pygame

pygame.init()

# Iniciando tela
resolucao = [400, 600]
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Flappy Bird")

# Declaração de texto
fonte = pygame.font.Font("freesansbold.ttf", 32)
texto = fonte.render("0", True, [0, 255, 0])

# Declaração de imagem
fundo = pygame.image.load("./Fundos/Fundo1.png")
fundo = pygame.transform.scale(fundo, (400, 600))

# Criando classe de pássaro
class Passaro:
    x = 170
    y = 250
    largura = 40
    altura = 40

    pulo = 80
    velocidade = 0
    aceleracao = 0.5

    imagem = pygame.image.load("./Jogadores/bird1.png")
    imagem = pygame.transform.scale(imagem, (largura, altura))

    def Atualizar(self, tela):
        self.Desenhar(tela)
        self.Cair()

    def Desenhar(self, tela):
        tela.blit(self.imagem, [self.x, self.y])  # Desenha o pássaro

    def Cair(self):
        self.velocidade += self.aceleracao
        self.y += self.velocidade

    def Voar(self):
        self.y -= self.pulo
        self.velocidade = 0


class Cano:
    largura = 100
    altura = 1550
    velocidade = 4
    baixo_y = 0
    cima_y = 0

    cano_baixo = pygame.image.load("./Objetos/Canos/Cano1/baixo.png")
    cano_baixo = pygame.transform.scale(cano_baixo, (largura, altura))

    cano_cima = pygame.image.load("./Objetos/Canos/Cano1/cima.png")
    cano_cima = pygame.transform.scale(cano_cima, (largura, altura))

    def __init__(self, x):
        self.x = x
        self.Reiniciar()

    def Reiniciar(self):
        y = random.randrange(190, 460)
        self.baixo_y = y
        self.cima_y = self.baixo_y - self.altura - 140

    def Desenhar(self, tela):
        tela.blit(self.cano_baixo, [self.x, self.baixo_y])
        tela.blit(self.cano_cima, [self.x, self.cima_y])

    def Mover(self):
        self.x -= self.velocidade

        if self.x < -self.largura:
            self.x = 450
            self.Reiniciar()

    def Atualizar(self, tela):
        self.Desenhar(tela)
        self.Mover()


class Chao:
    x = 0
    y = 510
    largura = 400
    altura = 90

    imagem = pygame.image.load("./Objetos/Choes/Chao1.png")
    imagem = pygame.transform.scale(imagem, (largura, altura))

    def Atualizar(self, tela):
        self.Desenhar(tela)

    def Desenhar(self, tela):
        tela.blit(self.imagem, [self.x, self.y])  # Desenha o chão


def main():  # Função onde o jogo inteiro irá rodar
    relogio = pygame.time.Clock()
    loop = True

    passaro = Passaro()
    chao = Chao()
    cano_1 = Cano(430)
    cano_2 = Cano(735)

    while loop:  # Criar um loop infinito

        tela.blit(fundo, [0, -85])  # Desenha o fundo
        passaro.Atualizar(tela)
        cano_1.Atualizar(tela)
        cano_2.Atualizar(tela)
        chao.Atualizar(tela)
        tela.blit(texto, [200, 0])  # Desenha o texto
        relogio.tick(30)
        pygame.display.update()  # Atualiza a tela

        for event in pygame.event.get():  # Pega os eventos que ocorrem no jogo
            if event.type == pygame.QUIT:  # Evento para quando o jogador apertar no "X" de nossa tela: sair do jogo
                loop = False

            if event.type == pygame.KEYDOWN:  # Verifica se tecla foi pressionada
                if event.key == pygame.K_UP:  # Verifica se tecla para cima foi pressionada
                    passaro.Voar()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Verifica se mouse foi pressionado
                passaro.Voar()

    pygame.quit()


main()  # Executa o jogo
