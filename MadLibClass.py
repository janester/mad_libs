#Jane Sternbach
#Kathryn Arroyo
#Com 110
#Final Project
#This class has methods that ask for user input and piece together the mad lib
from graphics import *
from random import *
from button3 import *
from RandomWord import *
from time import *

class createMadLib:

    #constructor takes in the textfiles necessary to read in
    #splits them into lists, and makes instance variables out of the lists
    def __init__(self,win,storyName,missingWords):

        self.win=win

        inputfile=open(storyName,"r")
        self.story=inputfile.read()
        inputfile.close()
        self.story=self.story.split("___")

        inputfile2=open(missingWords,"r")
        self.missingWords=inputfile2.read()
        inputfile2.close()
        self.missingWords=self.missingWords.split("\n")

        #constructor also creates its own GUI button, so when the main
        #function calls this class, it passes over the button clicking
        #ability as well
        self.Quit=Button(win,Point(900,100),50,50,"Quit")
        self.Quit.activate()
        
        self.Enter=Button(win,Point(775,500),50,50,"Enter")
        self.Enter.activate()

        self.Random=Button(win,Point(850,500),50,50,"Random")
        self.Random.activate()

        #Empty list for user input that will be automaticall populated
        #based on user button clicking
        self.inp=[]
        #Empty string that will be populated once all user input is collected
        self.complete=""

        self.q=False

        self.pt=self.win.getMouse()

        #Calling the randomWord class that already exists
        self.rWord=RandomWord()

    #This method gets all the user input via entry objects and buttons
    def getInput(self,fontsize):
        for i in range(len(self.missingWords)):
            #allows the user to quit in the middle, if necessary
            if self.Quit.clicked(self.pt)==True:
                self.win.close()
                self.q=True
                break
            #asks the user for the right type of word each time through the loop
            whattoent="Please enter a(n) "+str(self.missingWords[i])+":"
            self.instru=Text(Point(200,500),whattoent)
            self.instru.setSize(fontsize)
            self.instru.setStyle("bold")
            self.instru.draw(self.win)
            
            self.entryob=Entry(Point(500,500),40)
            self.entryob.draw(self.win)

            self.pt=self.win.getMouse()

            if self.Enter.clicked(self.pt)==True:
                #gets text from the entry object
                userinput=self.entryob.getText()
                #appends that texts to the input list
                self.inp.append(userinput)

            elif self.Random.clicked(self.pt)==True:
                #gets random word from random word class
                genWord=self.rWord.getRandWord(self.missingWords[i])
                #appends random word to input list
                self.inp.append(genWord)
            #have undraw the instructions so that the next time through the loop
            #the instructions are not covering each other
            self.instru.undraw()
            #clears the entry object and memory
            self.entryob.undraw()

    #this method puts together the exist textfile with blanks and the
    #new user input list
    #takes in parameters to help with individualizing the word cloud aspect
    def makeStory(self,fontsize,x1,x2,x3,x4,y1,y2,y3,y4):
        #if the fuction wasn't quit in the middle, then continue to make
        #the story
        if self.q==False:
            #undraw all of the input areas and buttons
            self.instru.undraw()
            self.entryob.undraw()
            self.Enter.undraw()
            self.Random.undraw()

            #loop through adding a piece of story and then a piece of user input
            #to the empty string
            for i in range(len(self.story)):
                self.complete+=self.story[i]
                if i<len(self.inp):
                    self.complete+=self.inp[i]

            #this method really takes in parameters to that they can be fed
            #to this method that is only called here
                    #this method places the inputted words randomly
            self.initiateWordCloud(x1,x2,x3,x4,y1,y2,y3,y4)
            #then the whole story is put into a text object
            self.wholeStory=Text(Point(500,500),self.complete)
            #taking in a parameter for fontsize, so that each story can be adjusted
            #separately.
            #this is necessary because the stories are different lengths, and need
            #to have the font size adjusted in order to fit well on the screen
            self.wholeStory.setSize(fontsize)
            self.wholeStory.setStyle("bold")
            #font color is randomized
            self.wholeStory.setFill(color_rgb(randrange(256),randrange(256),randrange(256)))
            #the story is drawn on top of the word cloud words, hopefully making it more readable
            self.wholeStory.draw(self.win)

            
            self.pt=self.win.getMouse()
            #allows the user to quit once the story and word cloud is displayed
            while not self.Quit.clicked(self.pt):
                self.pt=self.win.getMouse()
            self.win.close()
        else:
            self.win.close()
    #this method is used to check whether the makeStory method was correctly putting the words in the
    #right places
    def printStory(self):
        print(self.complete)

    #this method takes in the areas to randomly place words
    #these areas hopefully lessen the over lap because every time through the loop
    #a word goes to a random area in the grid not just directly on top of the previous word
    def initiateWordCloud(self,x1,x2,x3,x4,y1,y2,y3,y4):
        #lists of styles and fonts allow for easy randomization
        self.styles=["bold","italic","bold italic"]
        self.fonts=['helvetica','arial','courier','times roman']
        #outside counters for font and words
        self.n=10
        i=0
        #this list allows my to randomly choose which areas of the grid section I'd like the word to
        #to instead of having each word go in all the areas equally
        xy=[[x1,x2,y1,y2],[x1,x2,y3,y4],[x3,x4,y1,y2],[x3,x4,y3,y4]]
        #goes through the inputs
        for self.item in self.inp:
            #until it gets to the 17th input
            #without this there is too much overlap in longer stories with more input
            if i<17:
                #increment i
                i=i+1
                #call the method that randomly chooses all the options for these words
                self.forWordCloud(xy[randrange(0,len(xy))])
                #except for font, which cannot go above 100
                if self.n<  100:
                    self.n=self.n+5
                #waits before placing the word again in a different location
                sleep(.05)
                self.forWordCloud(xy[randrange(0,len(xy))])
                sleep(.05)
                self.forWordCloud(xy[randrange(0,len(xy))])
                sleep(.05)
                self.forWordCloud(xy[randrange(0,len(xy))])
                sleep(.05)
            

    #this method is called by initiator above
    #randomized everything for each individual word
    def forWordCloud(self,xylist):
        #for color randomization
        r=randrange(256)
        g=randrange(256)
        b=randrange(256)
        #randomly chosen point from one of the 4 grid areas
        newWord=Text(Point(randrange(xylist[0],xylist[1]),randrange(xylist[2],xylist[3])),self.item)
        #set random color
        newWord.setFill(color_rgb(r,g,b))
        #set size as long as it it smaller than 100
        newWord.setSize(self.n)
        #set random font style
        newWord.setStyle(self.styles[randrange(0,len(self.styles))])
        #set random font face
        newWord.setFace(self.fonts[randrange(0,len(self.fonts))])
        #draw the word
        newWord.draw(self.win)
        

