#Jane Sternbach
#Kathryn Arroyo
#Com 110
#Final Project
#This class reads in text files of lists of different kinds of words
#and then allows the user to get a random one depending on what kind of word
#is needed for the story

from random import *

class RandomWord:

    def __init__(self):
        #read in all the different files and make them into lists
        #that are instance variables
        nounfile=open("List of Nouns.txt","r")
        self.nouns=nounfile.read()
        nounfile.close()
        self.nouns=self.nouns.upper()
        self.nouns=self.nouns.split(" ")

        verbfile=open("List of Verbs.txt","r")
        self.verbs=verbfile.read()
        verbfile.close()
        self.verbs=self.verbs.upper()
        self.verbs=self.verbs.split("\n")

        adjfile=open("List of Adjectives.txt","r")
        self.adj=adjfile.read()
        adjfile.close()
        self.adj=self.adj.upper()
        self.adj=self.adj.split("\n")

        gerundfile=open("List of Gerunds.txt","r")
        self.gerunds=gerundfile.read()
        gerundfile.close()
        self.gerunds=self.gerunds.upper()
        self.gerunds=self.gerunds.split("\n")

        plnounfile=open("List of Plural Nouns.txt","r")
        self.plnouns=plnounfile.read()
        plnounfile.close()
        self.plnouns=self.plnouns.upper()
        self.plnouns=self.plnouns.split("\n")

        BPfile=open("List of Body Parts.txt","r")
        self.bodyParts=BPfile.read()
        BPfile.close()
        self.bodyParts=self.bodyParts.upper()
        self.bodyParts=self.bodyParts.split("\n")

        Adverbfile=open("List of Adverbs.txt","r")
        self.adverbs=Adverbfile.read()
        Adverbfile.close()
        self.adverbs=self.adverbs.upper()
        self.adverbs=self.adverbs.split("\n")

        Animalfile=open("List of Animals.txt","r")
        self.animals=Animalfile.read()
        Animalfile.close()
        self.animals=self.animals.upper()
        self.animals=self.animals.split("\n")

        Celebfile=open("List of Male Celebrities.txt","r")
        self.celebs=Celebfile.read()
        Celebfile.close()
        self.celebs=self.celebs.upper()
        self.celebs=self.celebs.split("\n")

        placefile=open("List of Places.txt","r")
        self.places=placefile.read()
        placefile.close()
        self.places=self.places.upper().split("\n")

        propnounfile=open("List of Proper Nouns.txt","r")
        self.prnouns=propnounfile.read()
        propnounfile.close()
        self.prnouns=self.prnouns.upper().split("\n")
        
    #create a getter for each kind of word
    def getNoun(self):
        return self.nouns[randrange(0,len(self.nouns))]

    def getVerb(self):
        return self.verbs[randrange(0,len(self.verbs))]

    def getAdj(self):
        return self.adj[randrange(0,len(self.adj))]

    def getGerund(self):
        return self.gerunds[randrange(0,len(self.gerunds))]
    
    def getPlNoun(self):
        return self.plnouns[randrange(0,len(self.plnouns))]

    def getBodyPart(self):
        return self.bodyParts[randrange(0,len(self.bodyParts))]

    def getAdverb(self):
        return self.adverbs[randrange(0,len(self.adverbs))]

    def getAnimal(self):
        return self.animals[randrange(0,len(self.animals))]

    def getCeleb(self):
        return self.celebs[randrange(0,len(self.celebs))]

    def getPlace(self):
        return self.places[randrange(0,len(self.places))]

    def getPropNoun(self):
        return self.prnouns[randrange(0,len(self.prnouns))]

    #create a method that takes in the type of word necessary and returns a
    #random one of that type
    def getRandWord(self,typeofWord):
        print(typeofWord)
        if typeofWord=="noun":
            return self.getNoun()
        elif typeofWord=="verb":
            return self.getVerb()
        elif typeofWord=="adjective":
            return self.getAdj()
        elif typeofWord=="verb ending in \"ing\"":
            return self.getGerund()
        elif typeofWord=="plural noun":
            return self.getPlNoun()
        elif typeofWord=="number":
            return str(randrange(-100000,100000))
        elif typeofWord=="body part":
            return self.getBodyPart()
        elif typeofWord=="adverb":
            return self.getAdverb()
        elif typeofWord=="animal":
            return self.getAnimal()
        elif typeofWord=="celebrity":
            return self.getCeleb()
        elif typeofWord=="place":
            return self.getPlace()
        elif typeofWord=="proper noun":
            return self.getPropNoun()
        else:
            return ("JANE")


    
    
    
