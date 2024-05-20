import os
import pygame


def load_image(k: int):
    img_big = pygame.image.load('static/' + os.listdir('static')[k])
    img_low = pygame.transform.scale(img_big, (K, K))
    img = pygame.transform.scale(img_low, (W, H))
    screen.blit(img, (0, 0))
    arr = [[''] * K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            c = 255 - sum(screen.get_at((i * (W // K) + 2, j * (H // K) + 2))[:3]) // 3
            arr[i][j] = symbols[int(c / 256 * len(symbols))]
    return arr, img


W, H, K = 500, 500, 100
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Символы")
font = pygame.font.Font(None, 10)
symbols = [' ', '`', '.', '\\', '/', "'", ',', '*', '~', '_', ':', '-', ';', '"', '>', '|', '^', '<', '!', 'r', '(', ')', '{', '1', 'i', '}', 'f', '+', 'I', 'l', 't', 'j', 'v', '[', ']', 'c', '?', '=', 'x', 's', '7', 'J', 'y', 'n', 'a', '%', 'o', 'L', 'z', 'e', 'u', '3', 'Y', 'V', '2', '4', '5', 'k', '$', 'C', '6', 'T', '0', '9', 'h', '8', 'd', '#', 'F', 'b', 'q', 'X', 'w', 'p', 'S', 'U', 'g', 'Z', 'O', 'K', 'P', '&', 'm', 'A', 'G', '@', 'Q', 'H', 'D', 'E', 'N', 'R', 'B', 'W', 'M']
a, img = load_image(0)

show, pic, ind = True, True, 0
while show:
    screen.fill((0, 0, 0))
    screen.blit(img, (0, 0))

    if not pic:
        screen.fill((250, 250, 250))
        for i in range(K):
            for j in range(K):
                text_surface = font.render(a[i][j], False, (0, 0, 0))
                screen.blit(text_surface, (i * (W // K), j * (H // K)))

    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            show = False

        if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
            pic = not pic

        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            ind -= 1
            ind = len(os.listdir('static')) - 1 if ind < 0 else ind
            a, img = load_image(ind)

        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            ind += 1
            ind = 0 if ind == len(os.listdir('static')) else ind
            a, img = load_image(ind)

        if e.type == pygame.KEYUP and e.key == pygame.K_RETURN:
            with open('return.txt', 'w') as f:
                for i in range(K):
                    f.write(' '.join([a[j][i] for j in range(K)]) + '\n')
                    print(*[a[j][i] for j in range(K)])
