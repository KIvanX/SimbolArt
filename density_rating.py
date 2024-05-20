import pygame


def density(e):
    x, y = (ord(e) - 32) // 10, (ord(e) - 32) % 10

    k = 0
    for i in range(x * 50, (x + 1) * 50):
        for j in range(y * 50, (y + 1) * 50):
            if screen.get_at((j, i)) == (0, 0, 0):
                k += 1

    return k


W, H = 500, 500
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Символы")
font = pygame.font.Font(None, 50)
symbols = [chr(i + 32) for i in range(95)]

show = True
while show:
    screen.fill((150, 150, 180))

    for i in range(10):
        for j in range(10):
            pygame.draw.line(screen, (0, 0, 0), (i * 50, 0), (i * 50, H))
            pygame.draw.line(screen, (0, 0, 0), (0, j * 50), (W, j * 50))
            if i * 10 + j < len(symbols):
                text_surface = font.render(symbols[i * 10 + j], True, (0, 0, 0))
                screen.blit(text_surface, (j * 50 + 10, i * 50 + 10))
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            show = False

        if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
            symbols.sort(key=lambda e: density(e))
            print(symbols)
