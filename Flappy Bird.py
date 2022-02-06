# Importando e inicializando o PyGame
import pygame

pygame.init()

# Iniciando tela
resolucao = [400, 600]
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Flappy Bird")

#Declaração de texto
fonte = pygame.font.Font("freesansbold.ttf", 32)
texto = fonte.render("Teste", True, [0, 255, 0])

#Declaração de imagem
imagem = pygame.image.load("./Jogadores/bird1.png")
imagem = pygame.transform.scale(imagem, (40, 40))

#Declaração do fundo
fundo1 = pygame.image.load("./Fundos/Fundo1.png")
fundo1 = pygame.transform.scale(fundo1, (400, 600))

#Declaração de cano cima e baixo
cano1Cima = pygame.image.load("./Objetos/Canos/Cano1/cima.png")
cano1Baixo = pygame.image.load("./Objetos/Canos/Cano1/baixo.png")
cano1Cima = pygame.transform.scale(cano1Cima, (100, 1550))
cano1Baixo = pygame.transform.scale(cano1Baixo, (100, 1550))

#Declaração de chão
chao1 = pygame.image.load("./Objetos/Choes/chao1.png")
chao1 = pygame.transform.scale(chao1, (400, 90))

tela.fill([0, 100, 220])

tela.blit(texto, [0, 0]) #Desenha o texto

tela.blit(fundo1, [10, -85]) #Desenha o fundo
tela.blit(imagem, [170, 250]) #Desenha a imagem
tela.blit(cano1Cima, [300, -1380]) #Desenha o cano 1 cima
tela.blit(cano1Baixo, [300, 310]) #Desenha o cano 1 baixo
tela.blit(chao1, [0, 510]) #Desenha o chão


pygame.display.update()

def main():  # Função onde o jogo inteiro irá rodar
    loop = True
    while loop:  # Criar um loop infinito
        for event in pygame.event.get():  # Pega os eventos que ocorrem no jogo
            if event.type == pygame.QUIT:  # Evento para quando o jogador apertar no "X" de nossa tela: sair do jogo
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Cima apertado")

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse pressionado")
    pygame.quit()


main()  # Executa o jogo