import pygame
from spritesheet import AnimatedSprite, SpriteSheet

STATE_IDLE = "IDLE"
STATE_JUMP = "JUMP"
STATE_HIT = "HIT"
STATE_RUN = "RUN"

class Player:
    def __init__(self):
        animation_speed=20
        scale = 3

        jump_spritesheet = SpriteSheet("ninja_frog/Jump (32x32).png", 32, 32)
        self.jump_animation = AnimatedSprite(jump_spritesheet, [(0,0)], animation_speed, scale)

        idle_spritesheet = SpriteSheet("ninja_frog/Idle (32x32).png", 32, 32)
        self.idle_animation = AnimatedSprite(idle_spritesheet, [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0), (10,0)], animation_speed, scale)

        hit_spritesheet = SpriteSheet("ninja_frog/Hit (32x32).png", 32, 32)
        self.hit_animation = AnimatedSprite(hit_spritesheet, [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)], animation_speed, scale)

        run_spritesheet = SpriteSheet("ninja_frog/Run (32x32).png", 32, 32)
        self.run_animation = AnimatedSprite(run_spritesheet, [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0), (10,0), (11,0)], animation_speed, scale)

        self.state = STATE_IDLE

    def update(self, dt: float):
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_a]:
                self.state = STATE_IDLE
            if pressed_keys[pygame.K_s]:
                self.state = STATE_JUMP
            if pressed_keys[pygame.K_d]:
                self.state = STATE_HIT
            if pressed_keys[pygame.K_f]:
                self.state = STATE_RUN

            # Update the current animation based on the state
            if self.state == STATE_IDLE:
                self.idle_animation.update()
            if self.state == STATE_JUMP:
                self.jump_animation.update()
            if self.state == STATE_HIT:
                self.hit_animation.update()
            if self.state == STATE_RUN:
                self.run_animation.update()

    def draw(self, screen: pygame.Surface):
        
        screen_center = screen.get_rect().center
        
        # Draw the current animation frame based on the state
        if self.state == STATE_IDLE:
            self.idle_animation.draw(screen, screen_center)  # Adjust position as needed
        if self.state == STATE_JUMP:
            self.jump_animation.draw(screen, screen_center)
        if self.state == STATE_HIT:
            self.hit_animation.draw(screen, screen_center)
        if self.state == STATE_RUN:
            self.run_animation.draw(screen, screen_center)