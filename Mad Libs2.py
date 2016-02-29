from graphics import *
from random import *
from button3 import *
from MadLibClass import *


def getRandomWord(typeofWord):
    nounfile=open("List of Nouns.txt","r")
    nouns=nounfile.read()
    nounfile.close()
    nouns=nouns.upper()
    nouns=nouns.split(" ")

    verbfile=open("List of Verbs.txt","r")
    verbs=verbfile.read()
    verbfile.close()
    verbs=verbs.upper()
    verbs=verbs.split("\n")

    adjfile=open("List of Adjectives.txt","r")
    adj=adjfile.read()
    adjfile.close()
    adj=adj.upper()
    adj=adj.split("\n")

    gerundfile=open("List of Gerunds.txt","r")
    gerunds=gerundfile.read()
    gerundfile.close()
    gerunds=gerunds.upper()
    gerunds=gerunds.split("\n")

    plnounfile=open("List of Plural Nouns.txt","r")
    plnouns=plnounfile.read()
    plnounfile.close()
    plnouns=plnouns.upper()
    plnouns=plnouns.split("\n")

    BPfile=open("List of Body Parts.txt","r")
    bodyParts=BPfile.read()
    BPfile.close()
    bodyParts=bodyParts.upper()
    bodyParts=bodyParts.split("\n")

    Adverbfile=open("List of Adverbs.txt","r")
    adverbs=Adverbfile.read()
    Adverbfile.close()
    adverbs=adverbs.upper()
    adverbs=adverbs.split("\n")

    numNouns=randrange(0,len(nouns))
    numVerbs=randrange(0,len(verbs))
    numAdj=randrange(0,len(adj))
    numGerunds=randrange(0,len(gerunds))
    numPlNouns=randrange(0,len(plnouns))
    numBodyParts=randrange(0,len(bodyParts))
    numAdverbs=randrange(0,len(adverbs))

    if typeofWord=="noun":
        return (nouns[numNouns])
    elif typeofWord=="verb":
        return (verbs[numVerbs])
    elif typeofWord=="adjective":
        return (adj[numAdj])
    elif typeofWord=="verb ending in \"ing\"":
        return (gerunds[numGerunds])
    elif typeofWord=="plural noun":
        return (plnouns[numPlNouns])
    elif typeofWord=="number":
        return str(randrange(-100000,100000))
    elif typeofWord=="body part":
        return (bodyParts[numBodyParts])
    elif typeofWord=="adverb":
        return (adverbs[numAdverbs])
    else:
        return ("JANE")

def LoveLetterStory(win,pt):
    inputfile=open("LoveLetter.txt","r")
    story=inputfile.read()
    story=story.split("___")
    inputfile.close()
    
    wordfile=open("LoveLetterWords.txt","r")
    missingWords=wordfile.read()
    missingWords=missingWords.split("\n")
    wordfile.close()

    inp=[]

    Quit=Button(win,Point(900,100),50,50,"Quit")
    Quit.activate()
    
    Enter=Button(win,Point(775,500),50,50,"Enter")
    Enter.activate()

    Random=Button(win,Point(850,500),50,50,"Random")
    Random.activate()

    q=False


    for i in range(len(missingWords)):
        if Quit.clicked(pt)==True:
            win.close()
            q=True
            break
        
        whattoent="Please enter a "+str(missingWords[i])+":"
        instru=Text(Point(200,500),whattoent)
        instru.draw(win)
        
        entryob=Entry(Point(500,500),50)
        entryob.draw(win)
        
        
        pt=win.getMouse()
        
        if Enter.clicked(pt)==True:
            userinput=entryob.getText()
            inp.append(userinput)

        elif Random.clicked(pt)==True:
            genWord=getRandomWord(missingWords[i])
            inp.append(genWord)
            
        instru.undraw()
        entryob.undraw()

    if q==False:
        instru.undraw()
        entryob.undraw()
        Enter.undraw()
        Random.undraw()
        
        complete=""
        for i in range(len(story)):
            complete+=story[i]
            if i<len(inp):
                complete+=inp[i]

        wholeStory=Text(Point(500,500),complete)
        wholeStory.draw(win)

        pt=win.getMouse()
        while not Quit.clicked(pt):
            pt=win.getMouse()
        win.close()
    else:
        win.close()

def main():
    win=GraphWin("Mab Libs",1000,1000)
    
    intro=Text(Point(500,500),"Welcome to MAD LIBS!")
    intro.draw(win)
    
    win.getMouse()
    
    intro.undraw()
    instructions=Text(Point(500,100),"Please select the story you would like to create.")
    instructions.draw(win)
    
    story1=Button(win,Point(500,500),100,50,"Love Letter")
    story1.activate()

    Quit=Button(win,Point(900,100),50,50,"Quit")
    Quit.activate()
    
    pt=win.getMouse()


    if story1.clicked(pt)==True:
        instructions.undraw()
        Quit.undraw()
        story1.undraw()
        instructions2=Text(Point(500,300),"You can either enter what the field asks for and press Enter, or generate a random answer by pressing Random.\n Please click anywhere to continue.")
        instructions2.draw(win)
        pt=win.getMouse()
        instructions2.undraw()
        LoveLetterStory(win,pt)
    elif Quit.clicked(pt)==True:
        win.close()
    
    else:
        pt=win.getMouse()

main()
