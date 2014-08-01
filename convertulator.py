import sys
import re

from functools import partial
from decimal import Decimal, ROUND_UP

usage = "Usage: convertulator.py textFile 'op' precision\n"
usage += "(e.g: convertulator.py convert.tex ' * 100' 0.01)"

class Convertulator(object):
    """
        Perform a mathmatical operation on all floating point numbers in a document

        Input:
            Text file with floating point values
            Literal string of mathematical operation - IN QUOTES
            Required output precision - e.g., 0.001

        Output:
            Input text file with the mathematical operation applied to all floating point numbers
    """

    def __init__(self, inText, expr, precision):
        self.inText = inText
        self.expr = expr
        self.precision = precision

    @staticmethod
    def op(self, matchObj):

        val = float(matchObj.group(0)) 
        newVal = eval('val ' + self.expr)
        roundVal = Decimal(str(newVal)).quantize(Decimal(self.precision), rounding = ROUND_UP)

        return str(roundVal)

    def replNumbers(self):
        opSingle = partial(self.op, self) # has to only take one arg
        return re.sub(r"[-+]?\d*\.\d+\d+", opSingle, self.inText)

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print usage
        sys.exit(1)

    fileName = sys.argv[1]
    expr = sys.argv[2].strip("'").strip('"')
    precision = sys.argv[3]

    inFile = open(fileName, 'r')

    text = ''

    for line in inFile:
        text += line

    inFile.close()

    print Convertulator(text, expr, precision).replNumbers()