from graphics import *
class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        #create a rectangle with a center point at a given center, of given height and width
        centerx=center.getX()
        centery=center.getY()
        halfwidth=width//2
        self.leftX=centerx-halfwidth
        self.rightX=centerx+halfwidth
        halfheight=height//2
        self.leftY=centery-halfheight
        self.rightY=centery+halfheight
        
        pt1=Point(self.leftX,self.leftY)
        pt2=Point(self.rightX,self.rightY)
        self.button=Rectangle(pt1,pt2)
        

        #set it to gray
        self.button.setFill("lightgray")

        #set Button's label
        self.buttonLabel=Text(center,label)

        #draw button
        self.button.draw(win)
        self.buttonLabel.draw(win)

        #deactivate the button
        self.deactivate()

        

    def clicked(self, p):
        "Returns true if button active and p is inside"

        #implement the clicked function
        return(self.active and self.leftX<=p.getX()<=self.rightX and self.leftY<=p.getY()<=self.rightY)
        

    def getLabel(self):
        "Returns the label string of this button."
        #implement getLabel function
        return self.buttonLabel.getText()

    def activate(self):
        "Sets this button to 'active'."
        #highlight the button label, i.e. set it to black
        self.buttonLabel.setFill("black")
        self.button.setWidth(2)
        #set active instance variable to True
        self.active=True

    def deactivate(self):
        "Sets this button to 'inactive'."
        #shade the button label, i.e. set it to gray
        self.buttonLabel.setFill("darkgray")
        self.button.setWidth(1)
        #set active instance variable to False
        self.active=False

    def undraw(self):
        self.button.undraw()
        self.buttonLabel.undraw()
