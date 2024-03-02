import random
from rpi_ws281x import Color


def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return Color(r, g, b)


# a simple implementation of a color wheel, where the input position (pos) is
# used to determine the color in the RGB color space. The color transitions
# smoothly through different hues as the position value increases.
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rgb_int2tuple(rgbint):
    return (rgbint // 256 // 256 % 256, rgbint // 256 % 256, rgbint % 256)


def hex_to_color(hex_color):
    """
    Convert HEX color code to rpi_ws281x Color type.

    Parameters:
    - hex_color (str): HEX color code (e.g., "#RRGGBB").

    Returns:
    - Color: rpi_ws281x Color type.
    """
    # Remove the "#" from the HEX color code
    hex_color = hex_color.lstrip("#")

    # Convert HEX to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Create and return Color object
    return Color(r, g, b)
