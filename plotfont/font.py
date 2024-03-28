##########################################################################
# Copyright (c) 2022-2024 Reinhard Caspary                               #
# <reinhard.caspary@phoenixd.uni-hannover.de>                            #
# This program is free software under the terms of the MIT license.      #
##########################################################################

import math
from .fonttable import HP1345A


class Font(object):

    """ Class which uses a monospaced character table to convert a given
    string into a list of line strokes, which can be used to print the
    string on a plotter device. """

    # Default font parameters
    _defaults = {
        "size": 5.0,        # Nominal font size
        "width": 5.0,       # Horizontal step size
        "divisor": 1.0,     # Font size of the character table
        "halign": "left",   # Horizontal string alignment
        "valign": "base",   # Vertical string alignment
        "rotate": 0,        # Rotation angle in degrees
        "mirrorx": False,   # Mirror at x axis
        "mirrory": False,   # Mirror at y axis
        }

    # Valid values for given font parameters
    _valid = {
        "halign": ("left", "center", "right"),
        "valign": ("top", "center", "base", "bottom"),
        }

    ######################################################################
    # Public methods
    ######################################################################

    def __init__(self, table=None, **kwargs):

        """ Initialize the character table and default font parameters.
        The default character table is based on the famous HP1345A font.
        """

        # Store default parameters modified by kwargs
        self.defaults = {k: v for k, v in self._defaults.items()}
        self.defaults = self._parse(**kwargs)
        

        # Dictionary mapping unicode characters to a list of polylines
        if table is None:
            self.table = HP1345A
            if "divisor" not in kwargs:
                self.defaults["divisor"] = 18.0
        else:
            self.table = table

    def string(self, text, x0=0, y0=0, **kwargs):

        """ Main public method. Return list of line strokes resembling
        the given text string. Each stroke is a list of one or more
        (x,y) tuples. A reference point (x0,y0) may be given as well as
        font parameters as keyword arguments. """

        # Merge kwargs into the font parameters
        args = self._parse(**kwargs)

        # Polylines for the string scaled to font size
        scale = float(args["size"]) / args["divisor"]
        width = args["width"]
        lines = self._strokes(text, scale, width)
        #print("Init", self.bbox(lines))

        # Apply mirror
        if args["mirrorx"] and args["mirrory"]:
            lines = self._mirror(lines, "xy")
            #lines = self.flop(lines, 2)
        elif args["mirrorx"]:
            lines = self._mirror(lines, "x")
        elif args["mirrory"]:
            lines = self._mirror(lines, "y")
        #print("Mirror", self.bbox(lines))

        # Determine bounding box
        bbox = self.bbox(lines)

        # Horizonal alignment offset
        if args["halign"] == "left":
            dx = -bbox[0]            
        elif args["halign"] == "right":
            dx = -bbox[2]
        else:
            dx = -0.5*(bbox[0] + bbox[2])

        # Vertical alignment offset
        if args["valign"] == "bottom":
            dy = -bbox[1]            
        elif args["valign"] == "top":
            dy = -bbox[3]
        elif args["valign"] == "base":
            dy = 0.0
        else:
            dy = -0.5*(bbox[1] + bbox[3])

        # Apply alignment offset
        if dx or dy:
            lines = self._shift(lines, dx, dy)
        #print("Align", self.bbox(lines))

        # Apply rotation
        angle = args["rotate"]
        if angle:
            lines = self._rotate(lines, angle)
        #print("Rotate", self.bbox(lines))

        # Apply global offset
        if x0 or y0:
            lines = self._shift(lines, x0, y0)
        #print("Global", self.bbox(lines))

        # Return list of polylines
        return lines


    def bbox(self, lines):

        """ Return bounding box of the given list of strokes as list
        [llx, lly, urx, ury]. """

        bbox = None
        for line in lines:
            for x, y in line:
                if bbox is None:
                    bbox = [x, y, x, y]
                else:
                    bbox[0] = min(bbox[0], x)
                    bbox[1] = min(bbox[1], y)
                    bbox[2] = max(bbox[2], x)
                    bbox[3] = max(bbox[3], y)
        return bbox


    ######################################################################
    # Private methods
    ######################################################################

    def _parse(self, **kwargs):

        """ Return a parameter dictionary with kwargs merged into the
        font defaults. """
        
        args = {k: v for k, v in self.defaults.items()}
        for key, value in kwargs.items():
            if not key in args:
                raise RuntimeError("Unknown parameter '%s'!" % key)
            if key in self._valid:
                if isinstance(value, str):
                    value = value.lower()
                if value not in self._valid[key]:
                    raise RuntimeError("Invalid value '%s' for parameter %s!" % (value, key))
            args[key] = value
        return args
    

    def _strokes(self, text, scale, width):

        """ Return the list of strokes resembling the given test string.
        """

        lines = []
        for i, c in enumerate(text):

            # Space character
            if c == " ":
                continue

            # Unknown character
            if c not in self.table:
                raise RuntimeError("Unknown character code %04X!" % ord(c))

            # Add polylines of character
            x = i*width
            y = 0
            lines += self._char(c, x, y, scale)

        return lines


    def _char(self, c, x0, y0, scale):

        """ Return the list of strokes resembling the given unicode
        character relative to the position (x0,y0). """

        lines = []
        for line in self.table[c]:
            line = [(x0+x*scale, y0+y*scale) for x, y in line]
            lines.append(line)
        return lines
                

    def _mirror(self, lines, axis):

        """ Mirror transform of the given lists of line strokes with
        respect to the x or y axis. """

        axis = "".join(sorted(axis.lower()))
        if axis not in ("x", "y", "xy"):
            raise RuntimeError("Unknown mirror axis '%s'!" % axis)

        if axis == "x":
            lines = [[(-x, y) for x, y in line] for line in lines]
        elif axis == "y":
            lines = [[(x, -y) for x, y in line] for line in lines]
        else:
            lines = [[(-x, -y) for x, y in line] for line in lines]
            
        return lines


    def _shift(self, lines, dx, dy):

        """ Translation of the given list of line strokes. """

        newlines = []
        for line in lines:
            line = [(x+dx, y+dy) for x, y in line]
            newlines.append(line)
        return newlines


    def _rotate(self, lines, angle):

        """ Rotate the given list of line strokes by the given angle in
        degrees. """

        # Rotate by multiples of 90 degrees
        if isinstance(angle, int) and angle % 90 == 0:
            num = (angle // 90) % 4
            if angle < 0:
                num = 4 - num
            return self._flip(lines, num)

        # Rotate by arbitrary angle
        sin = math.sin(angle*math.pi/180)
        cos = math.cos(angle*math.pi/180)
        newlines = []
        for line in lines:
            line = [(x*cos-y*sin, x*sin+y*cos) for x, y in line]
            newlines.append(line)
        return newlines


    def _flip(self, lines, num):

        """ Rotate the given list of line strokes by the given multiple
        of 90°. """

        # Remainder of num modulo 4
        num = int(num) % 4

        # No rotation
        if num == 0:
            return lines

        # Rotation by 90°, 180°, or 270°
        newlines = []
        for line in lines:
            if num == 1:
                line = [(-y, x) for x, y in line]
            if num == 2:
                line = [(-x, -y) for x, y in line]
            else:
                line = [(y, -x) for x, y in line]
            newlines.append(line)
        return newlines


##    def _scale(self, lines, scale):
##
##        """ Scale the given list of line strokes. """
##
##        newlines = []
##        for line in lines:
##            line = [(scale*x, scale*y) for x, y in line]
##            newlines.append(line)
##        return newlines
