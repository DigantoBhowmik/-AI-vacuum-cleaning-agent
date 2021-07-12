import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)

class Agent(Object):
    
    def __init__(self):        
        def program(percept):abstract
        self.program=program


loc_A,loc_B='A','B'

class vaccumEnvironemt(Object):

    def __init__(self):
        self.status={
            loc_A:random.choice(['Clean','Dirty']),
            loc_B:random.choice(['Clean','Dirty'])
            }
        
    def add_object(self,agent,location=None):
        agent.location=location or self.default_location()
    
    def default_location(self):
        return random.choice([loc_A,loc_B])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])


    def execute_action(self,agent,action):

        if action == 'Right': agent.location=loc_B
        elif action == 'Left': agent.location=loc_A
        elif action== 'Suck':
            self.status[agent.location]='Clean'




table={
        (('A', 'Clean'),): 'Right',
        (('A', 'Dirty'),): 'Suck',
        (('B', 'Clean'),): 'Left',
        (('B', 'Dirty'),): 'Suck',

        (('A', 'Clean'), ('B', 'Dirty')):'Suck',
        (('A', 'Clean'), ('B', 'Clean')):'Left',
        
        (('A', 'Dirty'), ('A', 'Clean')): 'Right',

        (('B', 'Clean'), ('A', 'Dirty')):'Suck',
        (('B', 'Clean'), ('A', 'Clean')):'Right',
        
        (('B', 'Dirty'), ('B', 'Clean')):'Right',
        (('B', 'Dirty'), ('B', 'Dirtry')):'Right',
        

    }

class tableDrivenAgent(Agent):

    def __init__(self,table):
        
        Agent.__init__(self)

        self.percepts=[]

        def program(percept):
            self.percepts.append(percept)
            action=table.get(tuple(self.percepts))
            print("Agent Has Perceived: ", percept, " And Performed Action: ", action)
            return action


        self.program=program



class simpleReflexVacuumAgent(Agent):

    def __init__(self,table):
        
        Agent.__init__(self)
        
        def program(percept):
            if percept[1] == 'Dirty': action= 'Suck'
            elif percept[0] == loc_A: action= 'Right'
            elif percept[0] == loc_B: action ='Left'


            print("Agent Has Perceived: ", percept, " And Performed Action: ", action)
            return action


        self.program=program

class modelBasedVacuumAgent(Agent):

    def __init__(self,table):
        
        Agent.__init__(self)s
        model = {'A': None, 'B': None}
        def program(percept):
            model[percept[0]] = percept[1]
            if model[loc_A] == model[loc_B] == 'Clean': return 'None'
            elif percept[1] == 'Dirty': action= 'Suck' 
            elif percept[0] == loc_A: action= 'Right'
            elif percept[0] == loc_B: action ='Left'

            
            print("Agent Has Perceived: ", percept, " And Performed Action: ", action)
            return action


        self.program=program
        
tAgent= simpleReflexVacuumAgent(table)
env=vaccumEnvironemt()
env.add_object(tAgent)

for _ in range(10):

    percept=env.percept(tAgent)
    action=tAgent.program(percept)
    env.execute_action(tAgent,action)


Agent= modelBasedVacuumAgent(table)
env=vaccumEnvironemt()
env.add_object(Agent)
print("Model Based")
for _ in range(10):

    percept=env.percept(Agent)
    action=Agent.program(percept)
    env.execute_action(Agent,action)

