import pygame
import math

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 600, 400
FPS = 60
PLAYER_SIZE = 50
PLAYER_SPEED = 5
BULLET_SPEED = 7
MAX_HEALTH = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Combat Game with Bullet Directions")

# Player class
class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = color
        self.health = MAX_HEALTH
        self.controls = controls
        self.bullets = []
        self.direction = pygame.Vector2(1, 0)  # Default direction is to the right

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        # Draw health bar
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y - 10, PLAYER_SIZE, 5))
        pygame.draw.rect(screen, GREEN, (self.rect.x, self.rect.y - 10, PLAYER_SIZE * (self.health / MAX_HEALTH), 5))
        # Draw bullets
        for bullet in self.bullets:
            pygame.draw.rect(screen, BLACK, bullet['rect'])

    def move(self, keys):
        if keys[self.controls['left']]:
            self.rect.x -= PLAYER_SPEED
            self.direction = pygame.Vector2(-1, 0)  # Move left
        if keys[self.controls['right']]:
            self.rect.x += PLAYER_SPEED
            self.direction = pygame.Vector2(1, 0)   # Move right
        if keys[self.controls['up']]:
            self.rect.y -= PLAYER_SPEED
            self.direction = pygame.Vector2(0, -1)  # Move up
        if keys[self.controls['down']]:
            self.rect.y += PLAYER_SPEED
            self.direction = pygame.Vector2(0, 1)   # Move down

    def shoot(self):
        # Create a bullet with its direction based on the current player direction
        bullet = {
            'rect': pygame.Rect(self.rect.centerx, self.rect.centery, 10, 5),
            'direction': self.direction.normalize()  # Normalize to get unit vector
        }
        self.bullets.append(bullet)

    def update_bullets(self, other_player):
        # Move bullets and check collision
        for bullet in self.bullets[:]:
            bullet['rect'].x += bullet['direction'].x * BULLET_SPEED
            bullet['rect'].y += bullet['direction'].y * BULLET_SPEED
            if bullet['rect'].colliderect(other_player.rect):
                other_player.health -= 10
                self.bullets.remove(bullet)
            elif bullet['rect'].x > WIDTH or bullet['rect'].x < 0 or bullet['rect'].y > HEIGHT or bullet['rect'].y < 0:
                self.bullets.remove(bullet)

# Main game loop
def main():
    clock = pygame.time.Clock()

    # Create two players
    player1 = Player(50, HEIGHT // 2, BLUE, {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s})
    player2 = Player(WIDTH - 100, HEIGHT // 2, RED, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN})

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Player 1 shoots
                    player1.shoot()
                if event.key == pygame.K_RETURN:  # Player 2 shoots
                    player2.shoot()

        # Get keys
        keys = pygame.key.get_pressed()

        # Move players
        player1.move(keys)
        player2.move(keys)

        # Update bullets and check for hits
        player1.update_bullets(player2)
        player2.update_bullets(player1)

        # Draw everything
        player1.draw()
        player2.draw()

        # Check win condition
        if player1.health <= 0 or player2.health <= 0:
            running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
