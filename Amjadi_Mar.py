import pygame, sys, random

pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Simple Snake Game")
clock = pygame.time.Clock()

BLACK, GREEN, RED, WHITE = (0,0,0), (0,255,0), (255,0,0), (255,255,255)
BLOCK = 20

font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 24)

def draw_text(text, color, x, y, font_obj=font):
    img = font_obj.render(text, True, color)
    rect = img.get_rect(center=(x, y))
    screen.blit(img, rect)

def game_loop():
    snake = [[100,100]]
    direction = 'RIGHT'
    change = direction
    food = [random.randrange(1, W//BLOCK)*BLOCK, random.randrange(1, H//BLOCK)*BLOCK]

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP and direction != 'DOWN': change = 'UP'
                elif e.key == pygame.K_DOWN and direction != 'UP': change = 'DOWN'
                elif e.key == pygame.K_LEFT and direction != 'RIGHT': change = 'LEFT'
                elif e.key == pygame.K_RIGHT and direction != 'LEFT': change = 'RIGHT'

        direction = change
        head = snake[0][:]
        if direction == 'UP': head[1] -= BLOCK
        elif direction == 'DOWN': head[1] += BLOCK
        elif direction == 'LEFT': head[0] -= BLOCK
        elif direction == 'RIGHT': head[0] += BLOCK

        if head[0]<0 or head[0]>=W or head[1]<0 or head[1]>=H or head in snake:
            return

        snake.insert(0, head)
        if head == food:
            food = [random.randrange(1, W//BLOCK)*BLOCK, random.randrange(1, H//BLOCK)*BLOCK]
        else:
            snake.pop()

        screen.fill(BLACK)
        for seg in snake:
            pygame.draw.rect(screen, GREEN, (*seg, BLOCK, BLOCK))
        pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))
        pygame.display.flip()
        clock.tick(10)

def game_over_screen():
    while True:
        screen.fill(BLACK)
        draw_text("Game Over!", WHITE, W//2, H//3)
        draw_text("Press R to Restart", WHITE, W//2, H//2)
        draw_text("Press Q to Quit", WHITE, W//2, H//2 + 50)
        draw_text("Builder Game : alireza amjadi", WHITE, W//2, H - 30, small_font)
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r: return
                if e.key == pygame.K_q: pygame.quit(); sys.exit()

def main():
    while True:
        game_loop()
        game_over_screen()

if __name__ == "__main__":
    main()
