from fractions import Fraction

class line:
    def __init__(self, gradient, intercept):
        self.gradient = gradient
        self.intercept = intercept
    
    def PerpendicularLineGoingThrough(self,x,y):
        newGradient = self.PerpendicularTo()
        newIntercept = y -  (newGradient * x)
        return line(newGradient, newIntercept)

    def PerpendicularTo(self):
        return -1 / self.gradient
    
    def AsString(self):
        return "y = {0}x + {1}".format(self.NumberString(self.gradient), self.NumberString(self.intercept))
    
    def NumberString(self, number):
        # Checks for integers
        if number % 1 == 0: 
            return "{0}".format(number)
        else:
            fract = Fraction(number)
            return "({0} / {1})".format(fract.numerator, fract.denominator )
    
with open ('questions.csv')as f:
    for lin in f:
        items = lin.split(',')
        gradient = Fraction(items[0])
        intercept = Fraction(items[1])
        xCoord = Fraction(items[2])
        yCoord = Fraction(items[3])
        firstLine = line(gradient, intercept)
        prepLine = firstLine.PerpendicularLineGoingThrough(xCoord, yCoord)
        print ("The line {0} is Perpendicular to {1} and goes through the point ( {2} , {3} )".format(
            prepLine.AsString()
            , firstLine.AsString()
            ,xCoord
            , yCoord
            ))
input('press that any key')
