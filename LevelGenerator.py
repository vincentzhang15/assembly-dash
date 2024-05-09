"""
Quick auxiliary program that generates artwork for game.asm.
@author Vincent Zhang
@since 2024-03-23 to 2024-04-03
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pyperclip
import colour

BLACK   = "0x00000000"
CLEAR   = "0xFFFFFFFF" # Set transparent color as background.
WHITE   = "0x00FFFFFF"
RED     = "0x00FF0000"
GREEN   = "0x0071aa35"
BLUE    = "0x000000FF"
GOLD    = "0x00FFD700"
GREY    = "0x00c2c3c7"
BROWN   = "0x00bf7b58"
SLATE   = "0x00c2c3c7"
SNOW    = "0x00fff1e8"
JUDGE_GRAY = "0x005f574f"
PIKA_YELLOW = "0x00ffff27"
PIKA_ORANGE = "0x00ffa200"
PIKA_RED    = "0x00ff004c"
PIKA_BROWN  = "0x00ab5236"
ALIEN_DBLUE = "0x00007ef3"
ALIEN_BLUE  = "0x003dbcfb"
ALIEN_LBLUE = "0x0094e8ff"
BIRD_DBLUE = "0x000d3e5d"
BIRD_LBLUE = "0x0000f6f9"
BIRD_DGREEN = "0x00058986"
CROWN_YELLOW = "0x00f8d978"
CROWN_DYELLOW = "0x00ffb33c"
CROWN_RED = "0x00ff3100"

def image_to_square(path):
    """Converts image to 8x8 hex grid. Used to generate hex colour grid for SYMBOLS map.
    @path: path to image
    @return: hex grid
    """
    # [Code Private - Contact to View]
    pass

SYMBOLS = { # Symbol: integer representation, 8x8 color representation.
    "^": (2, [
        [CLEAR, CLEAR, SNOW, CLEAR, CLEAR, CLEAR, SNOW, CLEAR],
        [CLEAR, CLEAR, SNOW, CLEAR, CLEAR, CLEAR, SNOW, CLEAR],
        [CLEAR, CLEAR, SNOW, CLEAR, CLEAR, CLEAR, SNOW, CLEAR],
        [CLEAR, SLATE, SNOW, SNOW, CLEAR, SLATE, SNOW, SNOW],
        [CLEAR, SLATE, SNOW, SNOW, CLEAR, SLATE, SNOW, SNOW],
        [JUDGE_GRAY, SLATE, SNOW, SLATE, JUDGE_GRAY, SLATE, SNOW, SLATE],
        [JUDGE_GRAY, SLATE, SLATE, SLATE, JUDGE_GRAY, SLATE, SLATE, SLATE],
        [JUDGE_GRAY, SLATE, SLATE, SLATE, JUDGE_GRAY, SLATE, SLATE, SLATE],
    ]),
    "F": (3, [
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
        [CROWN_DYELLOW, CLEAR, CLEAR, CROWN_DYELLOW, CLEAR, CLEAR, CLEAR, CROWN_DYELLOW],
        [CROWN_YELLOW, CROWN_DYELLOW, CLEAR, CROWN_YELLOW, CROWN_DYELLOW, CLEAR, CROWN_YELLOW, CROWN_DYELLOW],
        [CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_DYELLOW],
        [CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_RED,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_DYELLOW],
        [CROWN_YELLOW,CROWN_RED, CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW, CROWN_RED, CROWN_YELLOW, CROWN_DYELLOW],
        [CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_YELLOW,CROWN_DYELLOW],
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
    ]),
    "1": (1, image_to_square("images/1x1.png")),
    "Q": (1, image_to_square("images/1x3_L.png")),
    "E": (1, image_to_square("images/1x3_R.png")),
    "#": (1, image_to_square("images/1.png")),

    "T": (1, image_to_square("images/3x1_T.png")),
    "*": (1, image_to_square("images/3x1_M.png")),

    "[": (1, image_to_square("images/Corner_BL.png")),
    "]": (1, image_to_square("images/Corner_BR.png")),

    "P": (None, [
        [CLEAR, BLACK, BLACK, CLEAR, CLEAR, CLEAR, CLEAR, BLACK],
        [CLEAR, CLEAR, PIKA_YELLOW, PIKA_ORANGE, CLEAR, CLEAR, CLEAR, PIKA_ORANGE],
        [CLEAR, CLEAR, CLEAR, PIKA_YELLOW, PIKA_YELLOW, PIKA_YELLOW, PIKA_YELLOW, PIKA_ORANGE],
        [PIKA_ORANGE, PIKA_ORANGE, CLEAR, PIKA_YELLOW, BLACK, PIKA_YELLOW, PIKA_YELLOW, BLACK],
        [PIKA_ORANGE, PIKA_ORANGE, CLEAR, PIKA_RED, PIKA_YELLOW, PIKA_YELLOW, PIKA_YELLOW, PIKA_ORANGE],
        [CLEAR, PIKA_ORANGE, CLEAR, PIKA_YELLOW, PIKA_ORANGE, PIKA_ORANGE, PIKA_ORANGE, CLEAR],
        [CLEAR, PIKA_ORANGE, PIKA_YELLOW, PIKA_ORANGE, PIKA_YELLOW, PIKA_ORANGE, PIKA_YELLOW, CLEAR],
        [CLEAR, CLEAR, PIKA_YELLOW, PIKA_ORANGE, PIKA_BROWN, PIKA_BROWN, PIKA_ORANGE, CLEAR],
    ]),
    "L": (None, [
        [CLEAR, CLEAR, ALIEN_BLUE, CLEAR, CLEAR, ALIEN_BLUE, CLEAR, CLEAR],
        [ALIEN_DBLUE, CLEAR, ALIEN_BLUE, ALIEN_BLUE, ALIEN_BLUE, ALIEN_BLUE, CLEAR, ALIEN_DBLUE],
        [ALIEN_DBLUE,ALIEN_DBLUE,BLACK, ALIEN_BLUE, BLACK, ALIEN_BLUE, ALIEN_DBLUE, ALIEN_DBLUE],
        [ALIEN_BLUE,ALIEN_DBLUE,ALIEN_BLUE,BLACK,ALIEN_BLUE,ALIEN_BLUE,ALIEN_DBLUE, ALIEN_BLUE],
        [ALIEN_BLUE,ALIEN_BLUE,ALIEN_LBLUE,ALIEN_LBLUE,ALIEN_LBLUE,ALIEN_BLUE,ALIEN_BLUE,ALIEN_BLUE],
        [CLEAR, ALIEN_BLUE, ALIEN_LBLUE,ALIEN_LBLUE, ALIEN_LBLUE, ALIEN_BLUE, ALIEN_BLUE, CLEAR],
        [CLEAR, CLEAR, ALIEN_LBLUE,ALIEN_LBLUE,ALIEN_BLUE, ALIEN_BLUE, CLEAR, CLEAR],
        [CLEAR, CLEAR, ALIEN_BLUE, CLEAR, CLEAR, ALIEN_BLUE, CLEAR, CLEAR],
    ]),
    "C": (1, [
        [CLEAR, CLEAR, BIRD_DBLUE, BIRD_DBLUE, BIRD_DBLUE, CLEAR, CLEAR, CLEAR],
        [CLEAR, BIRD_DBLUE, BLACK, BLACK, BLACK, BIRD_DBLUE, CLEAR, CLEAR],
        [CLEAR, BIRD_DBLUE, BLACK, BIRD_LBLUE, BLACK, BIRD_DBLUE, CLEAR, CLEAR],
        [BIRD_LBLUE, BIRD_LBLUE, BLACK, BLACK, BLACK, BIRD_DBLUE, BIRD_DBLUE, BIRD_DBLUE],
        [BIRD_DBLUE, BIRD_DGREEN, BIRD_DGREEN, BIRD_DBLUE, BIRD_DBLUE, BIRD_DBLUE, BIRD_DBLUE, CLEAR],
        [CLEAR, BIRD_DGREEN, BIRD_DGREEN, BIRD_DGREEN, BIRD_DBLUE, BIRD_DBLUE, CLEAR, CLEAR],
        [CLEAR, CLEAR, BIRD_DGREEN, BIRD_DGREEN, BIRD_DBLUE, BIRD_DBLUE, CLEAR, CLEAR],
        [CLEAR, CLEAR, BIRD_LBLUE, CLEAR,CLEAR, BIRD_LBLUE, CLEAR, CLEAR],
    ]),
    "O": (None, [
        [CLEAR,CLEAR,BIRD_DGREEN,BIRD_DGREEN,BIRD_DGREEN,BIRD_DGREEN,CLEAR,CLEAR],
        [CLEAR,BIRD_DGREEN,BIRD_DGREEN,BIRD_DBLUE, BIRD_DBLUE,BIRD_DGREEN,BIRD_DGREEN,CLEAR],
        [BIRD_DGREEN,BIRD_DGREEN,BIRD_LBLUE,BIRD_LBLUE,BIRD_DBLUE,BIRD_DBLUE,BIRD_DGREEN,BIRD_DGREEN],
        [BIRD_DGREEN,BIRD_DBLUE,BIRD_LBLUE,BIRD_DBLUE,BIRD_DBLUE,BIRD_DBLUE,BIRD_DBLUE,BIRD_DGREEN],
        [BIRD_DGREEN,BIRD_DBLUE,BIRD_DBLUE,BIRD_DBLUE,BIRD_LBLUE,BIRD_DBLUE,BIRD_DBLUE,BIRD_DGREEN],
        [BIRD_DGREEN,BIRD_DGREEN,BIRD_DBLUE,BIRD_DBLUE,BIRD_DBLUE,BIRD_DBLUE,BIRD_DGREEN,BIRD_DGREEN],
        [CLEAR,BIRD_DGREEN,BIRD_DGREEN,BIRD_DBLUE,BIRD_DBLUE,BIRD_DGREEN,BIRD_DGREEN,CLEAR],
        [CLEAR,CLEAR,BIRD_DGREEN,BIRD_DGREEN,BIRD_DGREEN,BIRD_DGREEN,CLEAR,CLEAR],
    ]),
    "_": (0, [
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
        [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR],
    ])
}

PLAYER = "P"
LRAGENT = "L"
LAGENT = "O"

LEVEL1 = """
________________________________
____________________________F___
________________________Q###E___
________________________________
___1__________1_________________
________________T______C________
________________*______T________
________________[######]________
________________________________
________________________________
_____________QE_________________
________________________________
_______Q#E______________________
______________Q#E_______________
________________________________
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
LEVEL2 = """
________________________________
____________________________F___
____________________________1___
________________________________
________________________________
____1________________________C__
_____1_______________________1__
______1_________________________
_______1____________________1___
________1_______________________
_________1_________________1____
__________1_____________________
___________Q################E___
________________________________
________________________________
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
LEVEL3 = """
________________________________
________________________________
________________________________
___#____________________________
________________________________
____#__________________C_#______
______#__________#_____#________
________________________________
_________________________#____#_
_____________________#__________
__________#____#________________
___________________#____________
______________________________F_
____________________________#_#_
________________________________
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

levelart = []
LEVEL_WIDTH = 256
LEVEL_HEIGHT = 128
def generate_gradient(start, end):
    """ Generate gradient using <start> <end> colours.
    @start: Gradient start colour.
    @end: Gradient end colour.
    @return: Colour list, single colour for each row.
    """
    # [Code Private - Contact to View]
    pass
def init_level(start="#424093", end="#c383f7"):
    """ Inits <levelart> with gradient by expanding gradient list from <generate_gradient> to cover all columns.
    @start: Gradient start colour.
    @end: Gradient end colour.
    @return: void
    """
    # [Code Private - Contact to View]
    pass

def color_map(level, varname):
    """Loops through level provided and colours the map pixels.
    @level: A level defined by LEVEL1, LEVEL2, or LEVEL3.
    @varname: What the assembly variable name will be.
    @return: Assembly code of the level. Copied to clipboard.
    """
    # [Code Private - Contact to View]
    pass

def generate_map(level, varname, newline=False, hex=True):
    """Colors for each pixel.
    @level: A level defined by LEVEL1, LEVEL2, or LEVEL3.
    @varname: What the assembly variable name will be.
    @newline: separates each row into a new line (useful for smaller map sizes)
    @hex: hex colour code if True otherwise integer code.
    @return: Assembly code of the level. Copied to clipboard.
    """
    # [Code Private - Contact to View]
    pass


def get_int_map(level, varname):
    """Integer representation of map.
    @level: A level defined by LEVEL1, LEVEL2, or LEVEL3.
    @varname: What the assembly variable name will be.
    @return: Assembly code of the level. Copied to clipboard.
    """
    # [Code Private - Contact to View]
    pass


def generate_textart(text, size=36, double=True):
    """Generate ASCII art of text.
    @text: The text to draw.
    @size: Text size.
    @double: Whether to double text height to improve readability.
    @return: Text ASCII art in a list.
    """
    # [Code Private - Contact to View]
    pass


def insert_text(result, varname, data=[['0x00000000' for _ in range(LEVEL_WIDTH)] for _ in range(LEVEL_HEIGHT)], x=None, y=None):
    """Insert generated ASCII art level. Works both for score text and menu screens.
    @result: ASCII art list.
    @varname: What the assembly variable name will be.
    @data: default to black screen the same size as the screen. Otherwise the current level is passed in.
    @x: Text starting row.
    @y: Text starting column.
    """
    # [Code Private - Contact to View]
    pass


def generate_asciiart(varname, text, target_width=0.8):
    """Generate white text on black canvas. Copies to clipboard and prints to stdout.
    @varname: What the assembly variable name will be.
    @text: Text to generate ASCII art for.
    @target_width: max percentage of screen width the text can take up.
    @return: void
    """
    def find_text(text, target_width):
        """Find the largest font size that fits in a percentage of the screen.
        @text: Text to generate ASCII art for.
        @target_width: max percentage of screen width the text can take up.
        @return: ASCII art list if successful Exception otherwise.
        """
        # [Code Private - Contact to View]
        pass

    # [Code Private - Contact to View]
    pass

def main():
    # init_level(start="#c383f7", end="#424093")
    # color_map(LEVEL1, "LEVEL1")
    # insert_text(generate_textart("SCORE: 000", 10, double=False), "LEVEL1", data=levelart, x=3, y=2)
    # generate_map(LEVEL1, "LEVEL1I", hex=False)

    init_level(start="#50e1b9", end="#2a7560")
    color_map(LEVEL2, "LEVEL2")
    insert_text(generate_textart("SCORE: 100", 10, double=False), "LEVEL2", data=levelart, x=3, y=2)
    generate_map(LEVEL2, "LEVEL2I", hex=False)

    # init_level(start="#00d4ff", end="#090979")
    # color_map(LEVEL3, "LEVEL3")
    # insert_text(generate_textart("SCORE: 200", 10, double=False), "LEVEL3", data=levelart, x=3, y=2)
    # generate_map(LEVEL3, "LEVEL3I", hex=False)


    # generate_map(PLAYER, "PLAYER")
    # generate_map(LRAGENT, "LRAGENT")
    # generate_map(LAGENT, "LAGENT")

    # generate_map(LEVEL1, "LEVEL1")
    # get_int_map(LEVEL1, "LEVEL1I")


    # generate_asciiart("LOSE", "Game Over")
    # insert_text(generate_textart("SCORE: 000", 12, double=False), "LOSE_0", x=75, y=85)
    # generate_asciiart("LOSE", "Game Over")
    # insert_text(generate_textart("SCORE: 100", 12, double=False), "LOSE_1", x=75, y=85)
    # generate_asciiart("LOSE", "Game Over")
    # insert_text(generate_textart("SCORE: 200", 12, double=False), "LOSE_2", x=75, y=85)
    # generate_asciiart("WIN", "You Win!")
    # insert_text(generate_textart("SCORE: 300", 14, double=False), "WIN", x=95, y=80)

    # generate_asciiart("START_MENU", "ASSEMBLY DASH", target_width=0.90)
    # insert_text(generate_textart("<space> start game", 12, double=False), "START_MENU", x=75, y=59)
    # insert_text(generate_textart("<q> quit game", 12, double=False), "START_MENU", x=95, y=78)


    # print("\n".join(r))
    pass

if __name__=="__main__":main()