##########################################################################
# Copyright (c) 2022-2024 Reinhard Caspary                               #
# <reinhard.caspary@phoenixd.uni-hannover.de>                            #
# This program is free software under the terms of the MIT license.      #
##########################################################################
#
# Single stroke font data based on the font characters from the ancient
# vector display HP1345A known from the movie "Wargames". The character
# strokes were extracted from the original ROMs using the scripts
# provided by Poul-Henning Kamp (http://phk.freebsd.dk/hacks/Wargames).
# Thanks alot!
#
# Three new characters were added:
#
#   * "Vertical Line": based on "Broken Bar"
#   * "Latin Small Letter Dotless I": based on "Latin Small Letter I"
#   * "Latin Small Letter Dotless J": based on "Latin Small Letter J"
#
# The original font contains six accents: acute, grave, circumflex,
# diaeresis, tilde, and dot. These accents were combined with the
# according latin capital and small letters to add the respective
# unicode characters.
#
# All greek letters from the original font are included and other greek
# letters are copied from latin letters where appropriate. However, the
# greek alphabet is not complete.
#
# The small sharp s is copied from the greek beta. The micro sign is
# copied from the greek small mu.
#
##########################################################################

# The following font dictionary maps unicode characters to lists of line
# strokes. Each stroke is a list of integer (x, y) points (polyline).
# The font is a fixed-width font with width=18. The standard height is
# also y=18 above the baseline y=0 for characters without accent. The
# maximum height of characters with accent is y=26, characters with
# descender can reach y=-7. Therefore, the bounding box [0, -7, 18, 26]
# covers every character completely.

HP1345A = {
    # Exclamation Mark
    chr(0x0021): [
        [(6,0),(6,0)],
        [(6,5),(6,18)],
        ],
    # Quotation Mark
    chr(0x0022): [
        [(3,14),(4,18)],
        [(7,14),(8,18)],
        ],
    # Number Sign
    chr(0x0023): [
        [(2,0),(4,18)],
        [(8,0),(10,18)],
        [(0,13),(12,13)],
        [(0,5),(12,5)],
        ],
    # Dollar Sign
    chr(0x0024): [
        [(0,3),(3,1),(9,1),(12,3),(12,7),(9,9),(3,9),(0,11),(0,15),(3,17),(9,17),(12,15)],
        [(6,19),(6,-1)],
        ],
    # Percent Sign
    chr(0x0025): [
        [(0,0),(12,18)],
        [(6,14),(3,10),(0,14),(3,18),(6,14)],
        [(9,8),(12,4),(9,0),(6,4),(9,8)],
        ],
    # Ampersand
    chr(0x0026): [
        [(12,5),(8,0),(2,0),(0,4),(9,14),(7,18),(3,18),(1,14),(12,0)],
        ],
    # Apostrophe
    chr(0x0027): [
        [(5,14),(7,18),(7,18)],
        ],
    # Left Parenthesis
    chr(0x0028): [
        [(12,-2),(6,4),(6,14),(12,20)],
        ],
    # Right Parenthesis
    chr(0x0029): [
        [(0,-2),(6,4),(6,14),(0,20)],
        ],
    # Asterisk
    chr(0x002A): [
        [(3,2),(9,16)],
        [(3,16),(9,2)],
        [(0,9),(12,9)],
        ],
    # Plus Sign
    chr(0x002B): [
        [(6,2),(6,16)],
        [(0,9),(12,9)],
        ],
    # Comma
    chr(0x002C): [
        [(4,-4),(6,1),(6,1)],
        ],
    # Hyphen-minus
    chr(0x002D): [
        [(0,9),(12,9)],
        ],
    # Full Stop
    chr(0x002E): [
        [(6,0),(6,0),(6,0)],
        ],
    # Solidus
    chr(0x002F): [
        [(0,0),(12,18)],
        ],
    # Digit Zero
    chr(0x0030): [
        [(1,2),(11,16)],
        [(12,12),(12,6),(9,0),(3,0),(0,6),(0,12),(3,18),(9,18),(12,12)],
        ],
    # Digit One
    chr(0x0031): [
        [(3,0),(9,0)],
        [(6,0),(6,18),(3,15)],
        ],
    # Digit Two
    chr(0x0032): [
        [(0,15),(3,18),(9,18),(12,15),(12,11),(2,5),(0,0),(12,0)],
        ],
    # Digit Three
    chr(0x0033): [
        [(0,16),(3,18),(9,18),(12,15),(12,11),(9,9),(3,9)],
        [(9,9),(12,7),(12,3),(9,0),(3,0),(0,2)],
        ],
    # Digit Four
    chr(0x0034): [
        [(9,0),(9,18),(0,6),(12,6)],
        ],
    # Digit Five
    chr(0x0035): [
        [(0,2),(3,0),(9,0),(12,2),(12,8),(9,10),(3,10),(0,9),(2,18),(12,18)],
        ],
    # Digit Six
    chr(0x0036): [
        [(0,7),(3,10),(9,10),(12,7),(12,3),(9,0),(3,0),(0,3),(0,10),(3,15),(7,18)],
        ],
    # Digit Seven
    chr(0x0037): [
        [(0,18),(12,18),(4,0)],
        ],
    # Digit Eight
    chr(0x0038): [
        [(3,10),(0,13),(0,16),(3,19),(9,19),(12,16),(12,13),(9,10),(3,10),(0,7),(0,3),(3,0),(9,0),(12,3),(12,7),(9,10)],
        ],
    # Digit Nine
    chr(0x0039): [
        [(5,0),(9,3),(12,8),(12,15),(9,18),(3,18),(0,15),(0,11),(3,8),(9,8),(12,11)],
        ],
    # Colon
    chr(0x003A): [
        [(6,4),(6,4)],
        [(6,14),(6,14)],
        ],
    # Semicolon
    chr(0x003B): [
        [(5,-4),(7,0),(7,0)],
        [(7,10),(7,10)],
        ],
    # Less-than Sign
    chr(0x003C): [
        [(12,0),(0,9),(12,18)],
        ],
    # Equals Sign
    chr(0x003D): [
        [(0,4),(12,4)],
        [(0,14),(12,14)],
        ],
    # Greater-than Sign
    chr(0x003E): [
        [(0,0),(12,9),(0,18)],
        ],
    # Question Mark
    chr(0x003F): [
        [(0,15),(3,18),(9,18),(12,15),(12,11),(6,7),(6,4)],
        [(6,0),(6,0)],
        ],
    # Commercial At
    chr(0x0040): [
        [(12,2),(10,0),(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,6),(5,6),(5,13),(12,13)],
        ],
    # Latin Capital Letter A
    chr(0x0041): [
        [(0,0),(6,18),(12,0)],
        [(3,9),(9,9)],
        ],
    # Latin Capital Letter B
    chr(0x0042): [
        [(0,0),(0,18),(9,18),(12,15),(12,12),(9,9),(0,9)],
        [(9,9),(12,6),(12,3),(9,0),(0,0)],
        ],
    # Latin Capital Letter C
    chr(0x0043): [
        [(12,3),(9,0),(3,0),(0,3),(0,15),(3,18),(9,18),(12,15)],
        ],
    # Latin Capital Letter D
    chr(0x0044): [
        [(0,0),(0,18),(9,18),(12,15),(12,3),(9,0),(0,0)],
        ],
    # Latin Capital Letter E
    chr(0x0045): [
        [(0,0),(0,18),(12,18)],
        [(0,9),(9,9)],
        [(0,0),(12,0)],
        ],
    # Latin Capital Letter F
    chr(0x0046): [
        [(0,0),(0,18),(12,18)],
        [(0,9),(9,9)],
        ],
    # Latin Capital Letter G
    chr(0x0047): [
        [(12,15),(9,18),(3,18),(0,15),(0,3),(3,0),(9,0),(12,3),(12,8),(5,8)],
        ],
    # Latin Capital Letter H
    chr(0x0048): [
        [(0,0),(0,18)],
        [(12,0),(12,18)],
        [(0,9),(12,9)],
        ],
    # Latin Capital Letter I
    chr(0x0049): [
        [(2,0),(10,0)],
        [(6,0),(6,18)],
        [(2,18),(10,18)],
        ],
    # Latin Capital Letter J
    chr(0x004A): [
        [(0,2),(3,0),(5,0),(8,2),(8,18)],
        [(4,18),(12,18)],
        ],
    # Latin Capital Letter K
    chr(0x004B): [
        [(0,0),(0,18)],
        [(12,18),(0,6)],
        [(3,9),(12,0)],
        ],
    # Latin Capital Letter L
    chr(0x004C): [
        [(0,0),(0,18)],
        [(0,0),(12,0)],
        ],
    # Latin Capital Letter M
    chr(0x004D): [
        [(0,0),(0,18),(6,5),(12,18),(12,0)],
        ],
    # Latin Capital Letter N
    chr(0x004E): [
        [(0,0),(0,18),(12,0),(12,18)],
        ],
    # Latin Capital Letter O
    chr(0x004F): [
        [(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,3),(9,0),(3,0)],
        ],
    # Latin Capital Letter P
    chr(0x0050): [
        [(0,0),(0,18),(9,18),(12,15),(12,11),(9,8),(0,8)],
        ],
    # Latin Capital Letter Q
    chr(0x0051): [
        [(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,3),(9,0),(3,0)],
        [(7,5),(14,-2)],
        ],
    # Latin Capital Letter R
    chr(0x0052): [
        [(0,0),(0,18),(9,18),(12,15),(12,11),(9,8),(0,8)],
        [(7,8),(12,0)],
        ],
    # Latin Capital Letter S
    chr(0x0053): [
        [(0,2),(3,0),(9,0),(12,3),(12,6),(9,9),(3,9),(0,12),(0,15),(3,18),(9,18),(12,16)],
        ],
    # Latin Capital Letter T
    chr(0x0054): [
        [(6,0),(6,18)],
        [(0,18),(12,18)],
        ],
    # Latin Capital Letter U
    chr(0x0055): [
        [(0,18),(0,3),(3,0),(9,0),(12,3),(12,18)],
        ],
    # Latin Capital Letter V
    chr(0x0056): [
        [(0,18),(6,0),(12,18)],
        ],
    # Latin Capital Letter W
    chr(0x0057): [
        [(0,18),(3,0),(6,14),(9,0),(12,18)],
        ],
    # Latin Capital Letter X
    chr(0x0058): [
        [(0,0),(12,18)],
        [(0,18),(12,0)],
        ],
    # Latin Capital Letter Y
    chr(0x0059): [
        [(6,0),(6,7),(0,18)],
        [(6,7),(12,18)],
        ],
    # Latin Capital Letter Z
    chr(0x005A): [
        [(0,0),(12,18),(0,18)],
        [(12,0),(0,0)],
        ],
    # Left Square Bracket
    chr(0x005B): [
        [(12,20),(6,20),(6,-2),(12,-2)],
        ],
    # Reverse Solidus
    chr(0x005C): [
        [(0,18),(12,0)],
        ],
    # Right Square Bracket
    chr(0x005D): [
        [(0,-2),(6,-2),(6,20),(0,20)],
        ],
    # Circumflex Accent
    chr(0x005E): [
        [(0,7),(6,16),(12,7)],
        ],
    # Low Line
    chr(0x005F): [
        [(0,-5),(18,-5)],
        ],
    # Grave Accent
    chr(0x0060): [
        [(5,18),(5,18),(7,14)],
        ],
    # Latin Small Letter A
    chr(0x0061): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        ],
    # Latin Small Letter B
    chr(0x0062): [
        [(0,0),(0,18)],
        [(0,9),(6,11),(12,9),(12,2),(6,0),(0,2)],
        ],
    # Latin Small Letter C
    chr(0x0063): [
        [(11,9),(6,11),(0,9),(0,2),(6,0),(11,2)],
        ],
    # Latin Small Letter D
    chr(0x0064): [
        [(12,2),(6,0),(0,2),(0,9),(6,11),(12,9)],
        [(12,18),(12,0)],
        ],
    # Latin Small Letter E
    chr(0x0065): [
        [(0,6),(12,7),(9,12),(3,12),(0,9),(0,2),(3,0),(9,0),(12,2)],
        ],
    # Latin Small Letter F
    chr(0x0066): [
        [(4,0),(4,16),(8,18),(12,16)],
        [(0,9),(8,9)],
        ],
    # Latin Small Letter G
    chr(0x0067): [
        [(11,2),(6,0),(0,2),(0,9),(6,11),(11,9)],
        [(11,11),(11,-5),(6,-7),(0,-5)],
        ],
    # Latin Small Letter H
    chr(0x0068): [
        [(0,0),(0,18)],
        [(0,9),(6,11),(12,9),(12,0)],
        ],
    # Latin Small Letter I
    chr(0x0069): [
        [(7,0),(7,11),(4,11)],
        [(7,18),(7,18)],
        ],
    # Latin Small Letter J
    chr(0x006A): [
        [(0,-5),(4,-7),(8,-5),(8,11)],
        [(8,18),(8,18)],
        ],
    # Latin Small Letter K
    chr(0x006B): [
        [(0,0),(0,18)],
        [(0,5),(12,11)],
        [(4,7),(12,0)],
        ],
    # Latin Small Letter L
    chr(0x006C): [
        [(3,0),(9,0)],
        [(6,0),(6,18),(3,18)],
        ],
    # Latin Small Letter M
    chr(0x006D): [
        [(0,0),(0,12)],
        [(0,9),(4,12),(6,9),(6,0)],
        [(6,9),(10,12),(12,9),(12,0)],
        ],
    # Latin Small Letter N
    chr(0x006E): [
        [(0,0),(0,11)],
        [(0,8),(6,11),(12,8),(12,0)],
        ],
    # Latin Small Letter O
    chr(0x006F): [
        [(6,0),(0,2),(0,9),(6,11),(12,9),(12,2),(6,0)],
        ],
    # Latin Small Letter P
    chr(0x0070): [
        [(0,-7),(0,11)],
        [(0,9),(6,11),(12,9),(12,2),(6,0),(0,2)],
        ],
    # Latin Small Letter Q
    chr(0x0071): [
        [(11,2),(6,0),(0,2),(0,9),(6,11),(11,9)],
        [(11,11),(11,-6),(13,-8)],
        ],
    # Latin Small Letter R
    chr(0x0072): [
        [(0,0),(0,11)],
        [(0,8),(6,11),(12,8)],
        ],
    # Latin Small Letter S
    chr(0x0073): [
        [(0,2),(6,0),(12,2),(12,5),(0,7),(0,10),(6,12),(12,10)],
        ],
    # Latin Small Letter T
    chr(0x0074): [
        [(12,2),(8,0),(4,2),(4,18)],
        [(0,11),(8,11)],
        ],
    # Latin Small Letter U
    chr(0x0075): [
        [(0,11),(0,2),(6,0),(12,2),(12,11)],
        ],
    # Latin Small Letter V
    chr(0x0076): [
        [(0,11),(6,0),(12,11)],
        ],
    # Latin Small Letter W
    chr(0x0077): [
        [(0,11),(3,0),(6,8),(9,0),(12,11)],
        ],
    # Latin Small Letter X
    chr(0x0078): [
        [(0,0),(11,11)],
        [(0,11),(11,0)],
        ],
    # Latin Small Letter Y
    chr(0x0079): [
        [(0,11),(7,1)],
        [(3,-7),(12,11)],
        ],
    # Latin Small Letter Z
    chr(0x007A): [
        [(0,11),(12,11),(0,0),(12,0)],
        ],
    # Left Curly Bracket
    chr(0x007B): [
        [(12,-2),(7,1),(7,6),(4,9),(7,12),(7,17),(12,20)],
        ],
    # Vertical Line
    chr(0x007C): [
        [(6,0),(6,18)],
        ],
    # Right Curly Bracket
    chr(0x007D): [
        [(0,-2),(5,1),(5,6),(8,9),(5,12),(5,17),(0,20)],
        ],
    # Inverted Exclamation Mark
    chr(0x00A1): [
        [(12,0),(12,13)],
        [(12,18),(12,18)],
        ],
    # Pound Sign
    chr(0x00A3): [
        [(3,9),(9,9)],
        [(12,17),(8,18),(6,15),(6,2),(3,0),(0,0),(0,2),(3,2),(6,0),(9,0),(12,2)],
        ],
    # Broken Bar
    chr(0x00A6): [
        [(6,0),(6,6)],
        [(6,12),(6,18)],
        ],
    # Degree Sign
    chr(0x00B0): [
        [(6,16),(4,18),(4,21),(6,23),(9,23),(11,21),(11,18),(9,16),(6,16)],
        ],
    # Micro Sign
    chr(0x00B5): [
        [(0,-7),(2,11)],
        [(1,2),(6,0),(10,2),(11,11)],
        [(10,2),(13,0)],
        ],
    # Inverted Question Mark
    chr(0x00BF): [
        [(12,3),(6,0),(0,3),(0,7),(6,10),(6,14)],
        [(6,18),(6,18)],
        ],
    # Latin Capital Letter A With Grave
    chr(0x00C0): [
        [(0,0),(6,18),(12,0)],
        [(3,9),(9,9)],
        [(1,26),(11,22)],
        ],
    # Latin Capital Letter A With Acute
    chr(0x00C1): [
        [(0,0),(6,18),(12,0)],
        [(3,9),(9,9)],
        [(1,22),(10,25)],
        ],
    # Latin Capital Letter A With Circumflex
    chr(0x00C2): [
        [(0,0),(6,18),(12,0)],
        [(3,9),(9,9)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Capital Letter A With Tilde
    chr(0x00C3): [
        [(0,0),(6,18),(12,0)],
        [(3,9),(9,9)],
        [(0,23),(3,26),(9,23),(12,26)],
        ],
    # Latin Capital Letter A With Diaeresis
    chr(0x00C4): [
        [(0,0),(6,18),(12,0)],
        [(3,9),(9,9)],
        [(3,23),(3,23)],
        [(9,23),(9,23)],
        ],
    # Latin Capital Letter Ae
    chr(0x00C6): [
        [(0,0),(4,18),(7,18),(7,0),(12,0)],
        [(12,9),(2,9)],
        [(7,18),(12,18)],
        ],
    # Latin Capital Letter E With Grave
    chr(0x00C8): [
        [(0,0),(0,18),(12,18)],
        [(0,9),(9,9)],
        [(0,0),(12,0)],
        [(1,26),(11,22)],
        ],
    # Latin Capital Letter E With Acute
    chr(0x00C9): [
        [(0,0),(0,18),(12,18)],
        [(0,9),(9,9)],
        [(0,0),(12,0)],
        [(1,22),(10,25)],
        ],
    # Latin Capital Letter E With Circumflex
    chr(0x00CA): [
        [(0,0),(0,18),(12,18)],
        [(0,9),(9,9)],
        [(0,0),(12,0)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Capital Letter E With Diaeresis
    chr(0x00CB): [
        [(0,0),(0,18),(12,18)],
        [(0,9),(9,9)],
        [(0,0),(12,0)],
        [(3,23),(3,23)],
        [(9,23),(9,23)],
        ],
    # Latin Capital Letter I With Grave
    chr(0x00CC): [
        [(2,0),(10,0)],
        [(6,0),(6,18)],
        [(2,18),(10,18)],
        [(1,26),(11,22)],
        ],
    # Latin Capital Letter I With Acute
    chr(0x00CD): [
        [(2,0),(10,0)],
        [(6,0),(6,18)],
        [(2,18),(10,18)],
        [(1,22),(10,25)],
        ],
    # Latin Capital Letter I With Circumflex
    chr(0x00CE): [
        [(2,0),(10,0)],
        [(6,0),(6,18)],
        [(2,18),(10,18)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Capital Letter I With Diaeresis
    chr(0x00CF): [
        [(2,0),(10,0)],
        [(6,0),(6,18)],
        [(2,18),(10,18)],
        [(3,23),(3,23)],
        [(9,23),(9,23)],
        ],
    # Latin Capital Letter N With Tilde
    chr(0x00D1): [
        [(0,0),(0,18),(12,0),(12,18)],
        [(0,23),(3,26),(9,23),(12,26)],
        ],
    # Latin Capital Letter O With Grave
    chr(0x00D2): [
        [(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,3),(9,0),(3,0)],
        [(1,26),(11,22)],
        ],
    # Latin Capital Letter O With Acute
    chr(0x00D3): [
        [(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,3),(9,0),(3,0)],
        [(1,22),(10,25)],
        ],
    # Latin Capital Letter O With Circumflex
    chr(0x00D4): [
        [(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,3),(9,0),(3,0)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Capital Letter O With Tilde
    chr(0x00D5): [
        [(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,3),(9,0),(3,0)],
        [(0,23),(3,26),(9,23),(12,26)],
        ],
    # Latin Capital Letter O With Diaeresis
    chr(0x00D6): [
        [(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,3),(9,0),(3,0)],
        [(3,23),(3,23)],
        [(9,23),(9,23)],
        ],
    # Latin Capital Letter O With Stroke
    chr(0x00D8): [
        [(0,3),(0,15),(6,18),(12,15),(12,3),(6,0),(0,3),(12,15)],
        ],
    # Latin Capital Letter U With Grave
    chr(0x00D9): [
        [(0,18),(0,3),(3,0),(9,0),(12,3),(12,18)],
        [(1,26),(11,22)],
        ],
    # Latin Capital Letter U With Acute
    chr(0x00DA): [
        [(0,18),(0,3),(3,0),(9,0),(12,3),(12,18)],
        [(1,22),(10,25)],
        ],
    # Latin Capital Letter U With Circumflex
    chr(0x00DB): [
        [(0,18),(0,3),(3,0),(9,0),(12,3),(12,18)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Capital Letter U With Diaeresis
    chr(0x00DC): [
        [(0,18),(0,3),(3,0),(9,0),(12,3),(12,18)],
        [(3,23),(3,23)],
        [(9,23),(9,23)],
        ],
    # Latin Capital Letter Y With Acute
    chr(0x00DD): [
        [(6,0),(6,7),(0,18)],
        [(6,7),(12,18)],
        [(1,22),(10,25)],
        ],
    # Latin Small Letter Sharp S
    chr(0x00DF): [
        [(0,-7),(1,7),(3,16),(7,18),(12,16),(12,10),(8,8),(2,8)],
        [(8,8),(11,7),(12,3),(9,0),(5,0),(1,3)],
        ],
    # Latin Small Letter A With Grave
    chr(0x00E0): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(1,19),(11,15)],
        ],
    # Latin Small Letter A With Acute
    chr(0x00E1): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(1,15),(10,18)],
        ],
    # Latin Small Letter A With Circumflex
    chr(0x00E2): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Small Letter A With Tilde
    chr(0x00E3): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(0,16),(3,18),(9,16),(12,18)],
        ],
    # Latin Small Letter A With Diaeresis
    chr(0x00E4): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(3,17),(3,17)],
        [(9,17),(9,17)],
        ],
    # Latin Small Letter Ae
    chr(0x00E6): [
        [(0,11),(6,11),(6,0),(0,0),(2,5),(13,5),(13,8),(10,11),(7,8),(7,2),(9,0),(13,0)],
        ],
    # Latin Small Letter C With Cedilla
    chr(0x00E7): [
        [(11,9),(5,11),(0,9),(0,2),(5,0),(11,2)],
        [(5,0),(5,-4),(8,-7),(5,-10)],
        ],
    # Latin Small Letter E With Grave
    chr(0x00E8): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(1,19),(11,15)],
        ],
    # Latin Small Letter E With Acute
    chr(0x00E9): [
        [(0,6),(12,7),(9,12),(3,12),(0,9),(0,2),(3,0),(9,0),(12,2)],
        [(1,15),(10,18)],
        ],
    # Latin Small Letter E With Circumflex
    chr(0x00EA): [
        [(0,6),(12,7),(9,12),(3,12),(0,9),(0,2),(3,0),(9,0),(12,2)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Small Letter E With Diaeresis
    chr(0x00EB): [
        [(0,6),(12,7),(9,12),(3,12),(0,9),(0,2),(3,0),(9,0),(12,2)],
        [(3,17),(3,17)],
        [(9,17),(9,17)],
        ],
    # Latin Small Letter I With Grave
    chr(0x00EC): [
        [(7,0),(7,11),(4,11)],
        [(1,19),(11,15)],
        ],
    # Latin Small Letter I With Acute
    chr(0x00ED): [
        [(7,0),(7,11),(4,11)],
        [(1,15),(10,18)],
        ],
    # Latin Small Letter I With Circumflex
    chr(0x00EE): [
        [(7,0),(7,11),(4,11)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Small Letter I With Diaeresis
    chr(0x00EF): [
        [(7,0),(7,11),(4,11)],
        [(3,17),(3,17)],
        [(9,17),(9,17)],
        ],
    # Latin Small Letter N With Tilde
    chr(0x00F1): [
        [(0,0),(0,11)],
        [(0,8),(6,11),(12,8),(12,0)],
        [(0,16),(3,18),(9,16),(12,18)],
        ],
    # Latin Small Letter O With Grave
    chr(0x00F2): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(1,19),(11,15)],
        ],
    # Latin Small Letter O With Acute
    chr(0x00F3): [
        [(6,0),(0,2),(0,9),(6,11),(12,9),(12,2),(6,0)],
        [(1,15),(10,18)],
        ],
    # Latin Small Letter O With Circumflex
    chr(0x00F4): [
        [(6,0),(0,2),(0,9),(6,11),(12,9),(12,2),(6,0)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Small Letter O With Tilde
    chr(0x00F5): [
        [(6,0),(0,2),(0,9),(6,11),(12,9),(12,2),(6,0)],
        [(0,16),(3,18),(9,16),(12,18)],
        ],
    # Latin Small Letter O With Diaeresis
    chr(0x00F6): [
        [(6,0),(0,2),(0,9),(6,11),(12,9),(12,2),(6,0)],
        [(3,17),(3,17)],
        [(9,17),(9,17)],
        ],
    # Latin Small Letter O With Stroke
    chr(0x00F8): [
        [(0,0),(12,10)],
        [(12,8),(9,10),(3,10),(0,8),(0,2),(3,0),(9,0),(12,2),(12,8)],
        ],
    # Latin Small Letter U With Grave
    chr(0x00F9): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(1,19),(11,15)],
        ],
    # Latin Small Letter U With Acute
    chr(0x00FA): [
        [(0,11),(0,2),(6,0),(12,2),(12,11)],
        [(1,15),(10,18)],
        ],
    # Latin Small Letter U With Circumflex
    chr(0x00FB): [
        [(0,11),(0,2),(6,0),(12,2),(12,11)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Small Letter U With Diaeresis
    chr(0x00FC): [
        [(0,11),(0,2),(6,0),(12,2),(12,11)],
        [(3,17),(3,17)],
        [(9,17),(9,17)],
        ],
    # Latin Small Letter Y With Acute
    chr(0x00FD): [
        [(0,11),(7,1)],
        [(3,-7),(12,11)],
        [(1,15),(10,18)],
        ],
    # Latin Small Letter Y With Diaeresis
    chr(0x00FF): [
        [(0,11),(7,1)],
        [(3,-7),(12,11)],
        [(3,17),(3,17)],
        [(9,17),(9,17)],
        ],
    # Latin Capital Letter C With Acute
    chr(0x0106): [
        [(12,3),(9,0),(3,0),(0,3),(0,15),(3,18),(9,18),(12,15)],
        [(1,22),(10,25)],
        ],
    # Latin Small Letter C With Acute
    chr(0x0107): [
        [(11,9),(6,11),(0,9),(0,2),(6,0),(11,2)],
        [(1,15),(10,18)],
        ],
    # Latin Capital Letter C With Circumflex
    chr(0x0108): [
        [(12,3),(9,0),(3,0),(0,3),(0,15),(3,18),(9,18),(12,15)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Small Letter C With Circumflex
    chr(0x0109): [
        [(11,9),(6,11),(0,9),(0,2),(6,0),(11,2)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Capital Letter C With Dot Above
    chr(0x010A): [
        [(12,3),(9,0),(3,0),(0,3),(0,15),(3,18),(9,18),(12,15)],
        [(6,23),(6,23)],
        ],
    # Latin Small Letter C With Dot Above
    chr(0x010B): [
        [(11,9),(6,11),(0,9),(0,2),(6,0),(11,2)],
        [(6,17),(6,17)],
        ],
    # Latin Capital Letter E With Dot Above
    chr(0x0116): [
        [(0,0),(0,18),(12,18)],
        [(0,9),(9,9)],
        [(0,0),(12,0)],
        [(6,23),(6,23)],
        ],
    # Latin Small Letter E With Dot Above
    chr(0x0117): [
        [(0,6),(12,7),(9,12),(3,12),(0,9),(0,2),(3,0),(9,0),(12,2)],
        [(6,17),(6,17)],
        ],
    # Latin Capital Letter G With Circumflex
    chr(0x011C): [
        [(12,15),(9,18),(3,18),(0,15),(0,3),(3,0),(9,0),(12,3),(12,8),(5,8)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Small Letter G With Circumflex
    chr(0x011D): [
        [(11,2),(6,0),(0,2),(0,9),(6,11),(11,9)],
        [(11,11),(11,-5),(6,-7),(0,-5)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Capital Letter G With Dot Above
    chr(0x0120): [
        [(12,15),(9,18),(3,18),(0,15),(0,3),(3,0),(9,0),(12,3),(12,8),(5,8)],
        [(6,23),(6,23)],
        ],
    # Latin Small Letter G With Dot Above
    chr(0x0121): [
        [(11,2),(6,0),(0,2),(0,9),(6,11),(11,9)],
        [(11,11),(11,-5),(6,-7),(0,-5)],
        [(6,17),(6,17)],
        ],
    # Latin Capital Letter H With Circumflex
    chr(0x0124): [
        [(0,0),(0,18)],
        [(12,0),(12,18)],
        [(0,9),(12,9)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Small Letter H With Circumflex
    chr(0x0125): [
        [(11,2),(6,0),(0,2),(0,9),(6,11),(11,9)],
        [(11,11),(11,-5),(6,-7),(0,-5)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Capital Letter I With Tilde
    chr(0x0128): [
        [(2,0),(10,0)],
        [(6,0),(6,18)],
        [(2,18),(10,18)],
        [(0,23),(3,26),(9,23),(12,26)],
        ],
    # Latin Small Letter I With Tilde
    chr(0x0129): [
        [(7,0),(7,11),(4,11)],
        [(0,16),(3,18),(9,16),(12,18)],
        ],
    # Latin Capital Letter I With Dot Above
    chr(0x0130): [
        [(2,0),(10,0)],
        [(6,0),(6,18)],
        [(2,18),(10,18)],
        [(6,23),(6,23)],
        ],
    # Latin Small Letter Dotless I
    chr(0x0131): [
        [(7,0),(7,11),(4,11)],
        ],
    # Latin Capital Letter J With Circumflex
    chr(0x0134): [
        [(0,2),(3,0),(5,0),(8,2),(8,18)],
        [(4,18),(12,18)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Small Letter J With Circumflex
    chr(0x0135): [
        [(0,-5),(4,-7),(8,-5),(8,11)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Capital Letter L With Acute
    chr(0x0139): [
        [(0,0),(0,18)],
        [(0,0),(12,0)],
        [(1,22),(10,25)],
        ],
    # Latin Small Letter L With Acute
    chr(0x013A): [
        [(3,0),(9,0)],
        [(6,0),(6,18),(3,18)],
        [(1,22),(10,25)],
        ],
    # Latin Capital Letter N With Acute
    chr(0x0143): [
        [(0,0),(0,18),(12,0),(12,18)],
        [(1,22),(10,25)],
        ],
    # Latin Small Letter N With Acute
    chr(0x0144): [
        [(0,0),(0,11)],
        [(0,8),(6,11),(12,8),(12,0)],
        [(1,15),(10,18)],
        ],
    # Latin Capital Letter S With Circumflex
    chr(0x015C): [
        [(0,2),(3,0),(9,0),(12,3),(12,6),(9,9),(3,9),(0,12),(0,15),(3,18),(9,18),(12,16)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Small Letter S With Circumflex
    chr(0x015D): [
        [(0,2),(6,0),(12,2),(12,5),(0,7),(0,10),(6,12),(12,10)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Capital Letter U With Tilde
    chr(0x0168): [
        [(0,18),(0,3),(3,0),(9,0),(12,3),(12,18)],
        [(0,23),(3,26),(9,23),(12,26)],
        ],
    # Latin Small Letter U With Tilde
    chr(0x0169): [
        [(0,11),(0,2),(6,0),(12,2),(12,11)],
        [(0,16),(3,18),(9,16),(12,18)],
        ],
    # Latin Capital Letter W With Circumflex
    chr(0x0174): [
        [(0,18),(3,0),(6,14),(9,0),(12,18)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Small Letter W With Circumflex
    chr(0x0175): [
        [(0,11),(3,0),(6,8),(9,0),(12,11)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Capital Letter Y With Circumflex
    chr(0x0176): [
        [(6,0),(6,7),(0,18)],
        [(6,7),(12,18)],
        [(1,22),(6,25),(11,22)],
        ],
    # Latin Small Letter Y With Circumflex
    chr(0x0177): [
        [(0,11),(7,1)],
        [(3,-7),(12,11)],
        [(1,15),(6,18),(11,15)],
        ],
    # Latin Capital Letter Y With Diaeresis
    chr(0x0178): [
        [(6,0),(6,7),(0,18)],
        [(6,7),(12,18)],
        [(3,23),(3,23)],
        [(9,23),(9,23)],
        ],
    # Latin Capital Letter Z With Dot Above
    chr(0x017B): [
        [(0,0),(12,18),(0,18)],
        [(12,0),(0,0)],
        [(6,23),(6,23)],
        ],
    # Latin Small Letter Z With Dot Above
    chr(0x017C): [
        [(0,11),(12,11),(0,0),(12,0)],
        [(6,17),(6,17)],
        ],
    # Latin Capital Letter N With Grave
    chr(0x01F8): [
        [(0,0),(0,18),(12,0),(12,18)],
        [(1,26),(11,22)],
        ],
    # Latin Small Letter N With Grave
    chr(0x01F9): [
        [(0,10),(5,12),(11,10),(11,2),(8,0),(4,0),(0,2),(0,5),(11,6)],
        [(11,2),(13,0)],
        [(1,19),(11,15)],
        ],
    # Latin Small Letter Dotless J
    chr(0x0237): [
        [(0,-5),(4,-7),(8,-5),(8,11)],
        ],
    # Modifier Letter Vertical Line
    chr(0x02C8): [
        [(6,13),(6,18)],
        ],
    # Greek Capital Letter Alpha
    chr(0x0391): [
        [(0,0),(6,18),(12,0)],
        [(3,9),(9,9)],
        ],
    # Greek Capital Letter Beta
    chr(0x0392): [
        [(0,0),(0,18),(9,18),(12,15),(12,12),(9,9),(0,9)],
        [(9,9),(12,6),(12,3),(9,0),(0,0)],
        ],
    # Greek Capital Letter Gamma
    chr(0x0393): [
        [(0,0),(4,0)],
        [(2,0),(2,18)],
        [(0,18),(12,18),(12,14)],
        ],
    # Greek Capital Letter Delta
    chr(0x0394): [
        [(0,0),(6,15),(12,0),(0,0)],
        ],
    # Greek Capital Letter Epsilon
    chr(0x0395): [
        [(0,0),(0,18),(12,18)],
        [(0,9),(9,9)],
        [(0,0),(12,0)],
        ],
    # Greek Capital Letter Zeta
    chr(0x0396): [
        [(0,0),(12,18),(0,18)],
        [(12,0),(0,0)],
        ],
    # Greek Capital Letter Eta
    chr(0x0397): [
        [(0,0),(0,18)],
        [(12,0),(12,18)],
        [(0,9),(12,9)],
        ],
    # Greek Capital Letter Theta
    chr(0x0398): [
        [(7,0),(2,0),(0,4),(0,10),(2,15),(5,18),(10,18),(12,14),(12,8),(10,3),(7,0)],
        [(0,9),(12,9)],
        ],
    # Greek Capital Letter Iota
    chr(0x0399): [
        [(2,0),(10,0)],
        [(6,0),(6,18)],
        [(2,18),(10,18)],
        ],
    # Greek Capital Letter Kappa
    chr(0x039A): [
        [(0,0),(0,18)],
        [(12,18),(0,6)],
        [(3,9),(12,0)],
        ],
    # Greek Capital Letter Mu
    chr(0x039C): [
        [(0,0),(0,18),(6,5),(12,18),(12,0)],
        ],
    # Greek Capital Letter Nu
    chr(0x039D): [
        [(0,0),(0,18),(12,0),(12,18)],
        ],
    # Greek Capital Letter Omicron
    chr(0x039F): [
        [(3,0),(0,3),(0,15),(3,18),(9,18),(12,15),(12,3),(9,0),(3,0)],
        ],
    # Greek Capital Letter Rho
    chr(0x03A1): [
        [(0,0),(0,18),(9,18),(12,15),(12,11),(9,8),(0,8)],
        ],
    # Greek Capital Letter Tau
    chr(0x03A4): [
        [(6,0),(6,18)],
        [(0,18),(12,18)],
        ],
    # Greek Capital Letter Upsilon
    chr(0x03A5): [
        [(6,0),(6,7),(0,18)],
        [(6,7),(12,18)],
        ],
    # Greek Capital Letter Chi
    chr(0x03A7): [
        [(0,0),(12,18)],
        [(0,18),(12,0)],
        ],
    # Greek Capital Letter Omega
    chr(0x03A9): [
        [(0,0),(4,0),(1,7),(1,12),(4,16),(9,16),(12,12),(12,7),(9,0),(13,0)],
        ],
    # Greek Small Letter Beta
    chr(0x03B2): [
        [(0,-7),(1,7),(3,16),(7,18),(12,16),(12,10),(8,8),(2,8)],
        [(8,8),(11,7),(12,3),(9,0),(5,0),(1,3)],
        ],
    # Greek Small Letter Lamda
    chr(0x03BB): [
        [(0,0),(6,10)],
        [(0,17),(3,18),(9,2),(12,0)],
        ],
    # Greek Small Letter Mu
    chr(0x03BC): [
        [(0,-7),(2,11)],
        [(1,2),(6,0),(10,2),(11,11)],
        [(10,2),(13,0)],
        ],
    # Greek Small Letter Omicron
    chr(0x03BF): [
        [(6,0),(0,2),(0,9),(6,11),(12,9),(12,2),(6,0)],
        ],
    # Greek Small Letter Pi
    chr(0x03C0): [
        [(3,0),(4,12)],
        [(9,0),(9,12)],
        [(0,10),(4,12),(9,12),(12,14)],
        ],
    # Greek Small Letter Rho
    chr(0x03C1): [
        [(0,-7),(3,9),(7,12),(11,11),(13,8),(13,4),(10,0),(5,0),(2,3)],
        ],
    # Leftwards Arrow
    chr(0x2190): [
        [(6,3),(0,9),(6,15)],
        [(0,9),(12,9)],
        ],
    # Upwards Arrow
    chr(0x2191): [
        [(0,10),(6,18),(12,10)],
        [(6,18),(6,0)],
        ],
    # Rightwards Arrow
    chr(0x2192): [
        [(6,3),(12,9),(6,15)],
        [(0,9),(12,9)],
        ],
    # Downwards Arrow
    chr(0x2193): [
        [(0,8),(6,0),(12,8)],
        [(6,0),(6,18)],
        ],
    # Square Root
    chr(0x221A): [
        [(0,3),(3,0),(6,20),(13,20)],
        ],
    # Right Tack
    chr(0x22A2): [
        [(0,0),(0,18)],
        [(0,9),(12,9)],
        ],
    # Black Right-pointing Triangle
    chr(0x25B6): [
        [(0,0),(0,18),(12,9),(0,0)],
        [(0,3),(4,3),(4,15),(0,15)],
        [(0,6),(8,6),(8,12),(0,12)],
        [(0,9),(12,9)],
        ],
    }
