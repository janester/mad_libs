#Jane Sternbach
#Kathryn Arroyo
#Com 110
#Final Project
#Mad Libs/Word Cloud
#This program will allow the user to create stories by either entering words
#or randomly selecting them, and inserting them into the right spaces in the
#preset stories
#Once the stories are made, the words that were entered (or randomly chosen)
#will appear on the screen in random places, locations, sizes, fonts, and colors
#Then the new story will appear as well

#import all the necessary classes
from graphics import *
from random import *
from button3 import *
#these are the two self-created classes for this project
from MadLibClass import *
from RandomWord import *


def main():
    #graphical window 
    win=GraphWin("Mab Libs",1000,1000)
    #random background color
    win.setBackground(color_rgb(randrange(256),randrange(256),randrange(256)))

    #these lists allow me to easily randomize font and style
    styles=["bold","italic","bold italic"]
    fonts=['helvetica','arial','courier','times roman']
    #half of welcome will be randomized one way
    intro1=Text(Point(randrange(200,800),randrange(100,500)),"Welcome to")
    intro1.setSize(randrange(5,100))
    intro1.setStyle(styles[randrange(0,len(styles))])
    intro1.setFace(fonts[randrange(0,len(fonts))])
    intro1.setFill(color_rgb(randrange(256),randrange(256),randrange(256)))
    intro1.draw(win)
    #half the other way
    intro2=Text(Point(randrange(200,800),randrange(500,900)),"MAD LIBS!")
    intro2.setSize(randrange(5,100))
    intro2.setStyle(styles[randrange(0,len(styles))])
    intro2.setFace(fonts[randrange(0,len(fonts))])
    intro2.setFill(color_rgb(randrange(256),randrange(256),randrange(256)))
    intro2.draw(win)

    #mouse click
    win.getMouse()

    #random background color change
    win.setBackground(color_rgb(randrange(256),randrange(256),randrange(256)))
    
    intro1.undraw()
    intro2.undraw()
    #new instructions on how to use the program
    instructions=Text(Point(500,100),"Please select the story you would\n like to create.")
    instructions.setSize(48)
    instructions.draw(win)

    #buttons created for each story and a quit button
    story1=Button(win,Point(250,500),100,50,"Love Letter")
    story1.activate()

    story2=Button(win,Point(500,500),100,50,"Dream Man")
    story2.activate()

    story3=Button(win,Point(750,500),100,50,"Part of Your World")
    story3.activate()

    Quit=Button(win,Point(900,100),50,50,"Quit")
    Quit.activate()
    
    pt=win.getMouse()

    #makes the buttos work
    if story1.clicked(pt)==True:
        #new background color again
        win.setBackground(color_rgb(randrange(256),randrange(256),randrange(256)))
        #undraw all the old instructions
        instructions.undraw()
        Quit.undraw()
        story1.undraw()
        story2.undraw()
        story3.undraw()
        #give more instructions
        instructions2=Text(Point(500,300),"You can either enter what the field asks for and press Enter, \nor generate a random answer by pressing Random.\n Please click anywhere to continue.")
        instructions2.setSize(20)
        instructions2.setStyle("bold italic")
        instructions2.draw(win)
        pt=win.getMouse()
        #change background color
        win.setBackground(color_rgb(randrange(256),randrange(256),randrange(256)))
        instructions2.undraw()
        #get the mad lib creator class to do the rest of the work
        loveLetter=createMadLib(win,"LoveLetter.txt","LoveLetterWords.txt")
        #passing in fontsize to make the input instructions look nice
        loveLetter.getInput(17)
        #passing in fontsize, and then the areas for the grid for the word cloud
        loveLetter.makeStory(16,0,500,500,1000,0,400,600,1000)
        
    #same for the next two stories
    elif story2.clicked(pt)==True:
        win.setBackground(color_rgb(randrange(256),randrange(256),randrange(256)))
        instructions.undraw()
        Quit.undraw()
        story1.undraw()
        story2.undraw()
        story3.undraw()
        instructions2=Text(Point(500,300),"You can either enter what the field asks for and press Enter, \nor generate a random answer by pressing Random.\n Please click anywhere to continue.")
        instructions2.setSize(20)
        instructions2.setStyle("bold italic")
        instructions2.draw(win)
        pt=win.getMouse()
        win.setBackground(color_rgb(randrange(256),randrange(256),randrange(256)))
        instructions2.undraw()
        dreamMan=createMadLib(win,"DreamMan.txt","DreamManWords.txt")
        dreamMan.getInput(17)
        dreamMan.makeStory(16,0,500,500,1000,0,400,600,1000)

    elif story3.clicked(pt)==True:
        win.setBackground(color_rgb(randrange(256),randrange(256),randrange(256)))
        instructions.undraw()
        Quit.undraw()
        story1.undraw()
        story2.undraw()
        story3.undraw()
        instructions2=Text(Point(500,300),"You can either enter what the field asks for and press Enter, \nor generate a random answer by pressing Random.\n Please click anywhere to continue.")
        instructions2.setSize(20)
        instructions2.setStyle("bold italic")
        instructions2.draw(win)
        pt=win.getMouse()
        win.setBackground(color_rgb(randrange(256),randrange(256),randrange(256)))
        instructions2.undraw()
        POYW=createMadLib(win,"Part of Your World.txt","Part of Your World Words.txt")
        POYW.getInput(13)
        POYW.makeStory(14,0,200,800,1000,0,500,500,1000)
    #or the person can quit right away
    elif Quit.clicked(pt)==True:
        win.close()
    
    else:
        pt=win.getMouse()
  
main()
