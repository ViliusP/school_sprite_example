import pygame

class SpriteSheet:
    def __init__(self, filename, sprite_width, sprite_height):
        """Initialize the sprite sheet."""
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height

    def get_sprite(self, col, row, width=None, height=None):
        """Extracts and optionally scales a single sprite from the sprite sheet."""
        x = col * self.sprite_width
        y = row * self.sprite_height
        rectangle = pygame.Rect(x, y, self.sprite_width, self.sprite_height)
        sprite = self.sprite_sheet.subsurface(rectangle)
        if width and height:
            sprite = pygame.transform.scale(sprite, (width, height))
        return sprite
    
class AnimatedSprite:
    def __init__(self, sprite_sheet: SpriteSheet, frames_coordinates, frame_duration, scale_factor=2):
        """Initialize the animated sprite with scaling."""
        scaled_width = sprite_sheet.sprite_width * scale_factor
        scaled_height = sprite_sheet.sprite_height * scale_factor

        self.frames = []

        for col, row in frames_coordinates:
            sprite = sprite_sheet.get_sprite(col, row, scaled_width, scaled_height) 
            self.frames.append(sprite)

        self.current_frame = 0
        self.num_frames = len(self.frames)
        self.frame_duration = frame_duration
        self.last_update = pygame.time.get_ticks()

    def update(self):
        """Update the sprite to animate it based on time."""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.last_update = now

    def draw(self, screen, position):
        """Draw the current frame of the sprite at the given position."""
        screen.blit(self.frames[self.current_frame], position)