## Heroism_Reasoner_Alpha.py
## Joshua Fort
## CSC 594 Content Theory of Everyday Heroism

# Necessary Libraries
import random
import json 


try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

# import pickle 

global ResponseKnowledgeBase
global UserLibrary 
global OpportunityLibrary 

global CurrentUser
global CurrentOpportunity




## Knowledge Base
## getResponseKB() retrieves the response knowledge base for use and updating

def getResponseKB():
    rkb = json.loads(open('rkb.txt', 'r').read())
    global ResponseKnowledgeBase
    ResponseKnowledgeBase = rkb
    return
# rkb ## JDF Test
# rkb["Continuous"]["VillainousForce"]["Actualization"] ## JDF Test

# rkb["Continuous"]["VillainousForce"]["Actualization"].append("Actualization val5") ## JDF Test: Value addition
# rkb["Continuous"]["VillainousForce"]["Actualization"] ## JDF Test



def updateResponseKB():
    global ResponseKnowledgeBase
    rkb = ResponseKnowledgeBase
    with open('rkb.txt', 'w') as file:
        file.write(json.dumps(rkb)) # use `json.loads` to do the reverse
    return  


## User Creation


class User:
    def __init__(self, name, riskThreshold, reflections):
        self.name = name
        self.riskThreshold = riskThreshold
    
        #list of reflections user has engaged in ## JDF TODO 
        self.reflections = reflections


def getUserName():
    userName = input("Hi. What's your user name? ")
    return (userName)

# getUserName() # JDF Testing



def getUserRiskThreshold():
    riskThreshold = input("What's your risk tolerance? (H, M, L) ")
    return(riskThreshold)

# getUserRiskThreshold() # JDF Testing




def create_user():
    userName = getUserName()
    
    if userName.lower() == "quit":
        return (quitProgram()) ## JDF for tests 

    userRiskThreshold = getUserRiskThreshold()
    reflections = []
    user = User(userName, userRiskThreshold, reflections)

    return(user)
# create_user() ## JDF Test







## Opportunity Creation 

class Opportunity:
    def __init__(self, villainType, threatDuration, threatType):
        self.villainType = villainType
        self.threatDuration = threatDuration
        self.threatType = threatType




def getVillainType():
    while True:
        userInput = input("Is the cause of the threat an Agent, System, or Force? (A, S, F, or info) ")
        
        if userInput.lower() == "info":
            print('''
Villains are agents, systems, or forces that actively exploit and/or endanger human beings to advance its own interests.  
In the case of villainous agents, exploitation must be conscious. Someone is consciously creating the threat.
In the case of villainous systems, exploitation must perpetuate the system. A formal or informal policy furthers the threat.
In the case of villainous forces, exploitation or danger must be impersonal. An exteranal factor tied to a contingency rather than a person or structure.
            ''')
            pass
        
        elif userInput.upper() == "A":
            villainType = "VillainousAgent"
            break

        elif userInput.upper() == "S":
            villainType = "VillainousSystem"
            break
            
        elif userInput.upper() == "F":
            villainType = "VillainousForce"
            break
        
        elif userInput.lower() == ("quit"):
            return(quitProgram())
        
#         elif if villainType.upper() not in ['A', 'S', 'F']:
        else:
            print("Your options are 'A' for Agent, 'S' for System, or 'F' for Force. Type 'info' to learn more about these options.")
            print("You can also type 'quit' to end the program at any time.")
            pass
        


    return(villainType)
    
# getVillainType() # JDF Testing





def getThreatDuration():
    
    while True:
        userInput = input("Is the threat duration Episodic or Continuous? (E, C, or info) ")


        if userInput.lower() == "info":
            print('''
Heroic opportunities can be Episodic or Continuous as determined by the nature of the threat.
If the problem is a one time thing, mark it as Episodic. If it happens repeatedly, mark it as Continuous.
            ''')
            pass

        elif userInput.upper() == "E":
            threatDuration = "Episodic"
            break

        elif userInput.upper() == "C":
            threatDuration = "Continuous"
            break

        elif userInput.lower() == ("quit"):
            return(quitProgram())

        else:
            print("Your options are 'E' for Episodic or 'C' for Continuous. Type 'info' to learn more about these options.")
            print("You can also type 'quit' to end the program at any time.")
            pass


    
    
    return(threatDuration)
    
# getThreatDuration() # JDF Testing






def getThreatType():
    
    while True:
    
        userInput = input("Is the threat Physiological, Safety, Belonging, Esteem, or Actualization related (P, S, B, E, A, or info) ")
    
        if userInput.lower() == "info":
            print('''
Physiological threats cause direct bodily damage to the person you're seeking to help. Threats to health, food and water, sleep, clothes, and shelter are included in this category. 
Safety threats cause damage to someone's personal, emotional, financial, or indirect risk of future physical harm.  
Belonging threats cause damage to social bonds, such as the bonds of family, friendship, or community. 
Esteem threats run the risk of damaging someone's self-respect or proper perception of self. 
Actualization threats run the risk of damaging someone's potential to pursue their goals, dreams, and utilize their gifts. 
            ''')
            pass

        elif userInput.upper() == "P":
            threatType = "Physiological"
            break

        elif userInput.upper() == "S":
            threatType = "Safety"
            break
            
        elif userInput.upper() == "B":
            threatType = "Belonging"
            break

        elif userInput.upper() == "E":
            threatType = "Esteem"
            break
            
        elif userInput.upper() == "A":
            threatType = "Actualization"
            break

        elif userInput.lower() == ("quit"):
            return(quitProgram())
        
        elif userInput.lower() == ("main"):
            return



        else:
            print("Your options are 'P', 'S', 'B', 'E', or 'A'. \nType 'info' to learn more about these options.")
            print("You can also type 'quit' to end the program at any time.")
            pass
    
    return(threatType)
    
# getThreatType() # JDF Testing








def getOpportunityDescription():
    userInput = input("Describe the situation in a single sentence. ")
    opportunityDescription = userInput
    if userInput.lower() == ("quit"):
        return(quitProgram())
    else:
        return(opportunityDescription)

# getOpportunityDescription() ## JDF Test




def create_opportunity():
    
    # Used for archiving opportunities 
    opportunityDescription = getOpportunityDescription()
    if opportunityDescription == quitProgram():
        return (quitProgram()) ## JDF for tests 
    
    villainType = getVillainType()
    if villainType == quitProgram():
        return (quitProgram()) ## JDF for tests 

    threatDuration = getThreatDuration()
    if threatDuration == quitProgram():
        return (quitProgram()) ## JDF for tests 

    
    threatType = getThreatType()
    if threatType == quitProgram(): ## JDF for tests 
        return (quitProgram())
    
    # Creates the opportunity
    opportunity = Opportunity(villainType, threatDuration, threatType)
    
    # Stores the opportunity as a global variable 
    CurrentOpportunity = opportunity

    # Stores the opporutnity with its description 
    OpportunityLibrary[opportunityDescription] = opportunity
    
    return(opportunity)

# create_opportunity() #JDF test






## Login Prompt

def login_prompt():
    
    global currentUser 
    
    while True:
        print("\nSIGN IN")
        userInput = input("Is this your first time here? (y, n, or menu) ")
        
        if userInput.lower() == 'menu':
            return

        elif userInput == quitProgram():
            return (quitProgram()) ## JDF for tests 
        
        elif userInput == "quit":
            return (quitProgram()) ## JDF for tests 
            
        elif userInput.lower() == 'y':
            newUser = create_user()
            
            if newUser == quitProgram():
                return (quitProgram()) ## JDF for tests 

#             elif userInput == "quit":
#                 return (quitProgram()) ## JDF for tests 
            
            UserLibrary[newUser.name] = newUser
            CurrentUser = UserLibrary[newUser.name]
            return(CurrentUser)
        
        elif userInput.lower() == 'n':
            userName = input("What's your username? ")
            
            if userName in list(UserLibrary.keys()):
                print("Welcome back,", userName + ".")
                CurrentUser = UserLibrary[userName]
                return(CurrentUser)
            else:
                print("I'm sorry, your username isn't in our database.")
                print("\nUsers include: ", list(UserLibrary.keys()))

        else:
            print('''I'm sorry. Your options are to type 'y' for yes or 'n' for no.
            \nYou can also return to the main menu by typing 'menu'. ''')
        

# login_prompt() ## JDF Test





## Opportunity Analysis

## Uses the villainType, threatDuration, threatType to access the expanding library of opportunities. 

def opportunityAnalysis():
    newOpportunity = create_opportunity()

    
    if newOpportunity == quitProgram():
        return (quitProgram())


#     elif newOpportunity.threatDuration == quitProgram():
#         return (quitProgram())
    
#     elif newOpportunity.threatType == quitProgram():
#         return (quitProgram())
    
    else:
        ## Save 
        global ResponseKnowledgeBase
        opportunityResponse = ResponseKnowledgeBase[newOpportunity.threatDuration][newOpportunity.villainType][newOpportunity.threatType]
        recommendedResponse = random.choice(opportunityResponse)
        return (recommendedResponse)

# opportunityAnalysis() ## JDF Test




## Main Menu & Program Navigation


def aboutProgram():
    print('''
The world of tomorrow needs heroes. Not superheroes with fancy powers or flashy costumes, but everyday heroes who engage in intentional, everyday actions that better the lives of those within reach. This program is designed to support you in the pursuit of everyday heroism. It will give you the opportunity to answer questions about situations you're facing and it will point out risks and provide recommendations concerning the situation.
The program also gives you the opportunity to reflect on situations you haven't been in personally. Your advice and reflections will be added to the knowledge base to support future users.
    ''')
    
    return





def mainMenu():
    
    #Initializes the user as a guest 
    global CurrentUser 
    CurrentUser = User("GUEST", "M", [])

    
    while True:
        userInput = input('''\nMENU
        Type the letter that corresponds with the menu item you would like to select.
        
        About the Heroism Reasoner (a)
        
        Launch the Heroism Reasoner (l)
        
        Sign-in (s)
        
        User Library (u)
                
        (You can also type 'quit' to end the program at any time.)
        ''')
        
        if userInput.lower() == ("a"):
            userInput = aboutProgram()
            if userInput == quitProgram():
                return (quitProgram()) ## JDF for tests 
            else:
                pass 

        elif userInput.lower() == ("l"):
            responseToUser = opportunityAnalysis() 
            if userInput == quitProgram():
                return (quitProgram()) ## JDF for tests 
            else:
                print(responseToUser)
                pass

        elif userInput.lower() == ("s"):
            userInput = login_prompt()
            if userInput == quitProgram():
                return (quitProgram()) ## JDF for tests 
            else:
                pass
            
        elif userInput.lower() == ("u"):
            print("\nUsers include: ", list(UserLibrary.keys()))
            pass
        
        elif userInput.lower() == ("quit"):
            return(quitProgram())
        else:
            print("Sorry. Choose from the menu options above or 'quit' to end the program at any time")
            
        
        ## print(userInput)  ##JDF Debugging



# mainMenu() ##JDF Test






## Housekeeping Functions

def quitProgram():
#     print("Come again soon. We have much to discuss. You've exited the program.") ## Actual quit program 
#     return(exit(0)) ## Actual quit program
    
    global UserLibrary
    save_object(UserLibrary, 'UserLibrary.pkl')
    
    
    global OpportunityLibrary
    save_object(OpportunityLibrary, 'OpportunityLibrary.pkl')
    
    updateResponseKB()
    
    return("Come again soon. We have much to discuss. You've exited the program.") ## Helpful for tests




## Save User Library (or any object)

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    return 

# ## JDF Test
# global UseerLibrary
# save_object(UserLibrary, 'UserLibrary.pkl')






## Opportunity Library

## Import Opportunity Library 
def getOpportunityLibrary():
    global OpportunityLibrary 
    OpportunityLibrary = pickle.load(open("OpportunityLibrary.pkl", "rb"))
    return

# list(UserLibrary.keys()) ## JDF Test

# ## JDF Testing
# create_opportunity() #JDF test
# save_object(OpportunityLibrary, 'OpportunityLibrary.pkl')
# # list(OpportunityLibrary.keys()) ## JDF Test



## User Library
## Import User Library 
def getUserLibrary():
    global UserLibrary
    UserLibrary = pickle.load(open("UserLibrary.pkl", "rb"))
    return

# list(UserLibrary.keys()) ## JDF Test

# ## UserLibrary = {} ## UserLibrary Reset
# login_prompt() ## JDF Test: Admin. Input additional users.


## Running the Program

def run():
    getResponseKB()
    getUserLibrary()
    getOpportunityLibrary()
    while True:
        print('''Welcome to the Heroism Reasoner.  
        \nYou can also type 'quit' to end the program at any time.''')
        mainMenu()
        return(quitProgram())
# run() #JDF Test



if __name__ == '__main__':
    run()





# list(OpportunityLibrary.keys()) ## JDF Test


# list(UserLibrary.keys()) ## JDF Test


# ResponseKnowledgeBase



### Future Implementation Notes 
## Collect all text descriptions of the issue, record opportunity type with it
## Run KNN to retrieve similar instances
## Spit back instance description and check to see if it sounds right 





