import pygame


color_palettes = {
    "mysterious": ["#581b98", "#9c1de7", "#f3558e", "#faee1c", "#8cff75"],
    "freezing": ['#7d8aff', '#6db3de', '#84f5e4', '#6dde8e', '#cdfab6']
}

for color_palette_name in color_palettes:
    for color_index in range(len(color_palettes[color_palette_name])):
        color_palettes[color_palette_name][color_index] = pygame.Color(color_palettes[color_palette_name][color_index])
