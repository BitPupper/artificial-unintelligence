# The more "happy" states an agent recieves, the stronger the "optmist" trait is
# The optimist trait reduces chance of being violent when attacked, makes negative gossip less affective, and 
#
from random import random, seed, choice, choices

class Agent:
    class TwoWayDict(dict):
        def __setitem__(self, key, value):
            # Remove any previous connections with these values
            if key in self:
                del self[key]
            if value in self:
                del self[value]
            dict.__setitem__(self, key, value)
            dict.__setitem__(self, value, key)

        def __delitem__(self, key):
            dict.__delitem__(self, self[key])
            dict.__delitem__(self, key)

        def __len__(self):
            """Returns the number of connections"""
            return dict.__len__(self) // 2
    
    #gamma: next state q value modifier
    #alpha: learning rate
    #epsilon: exploration/randomness factor
    #epsilon_decay_factor: name
    state_index_map = TwoWayDict()
    
    action_index_map = TwoWayDict()
    
    params = {"gamma":0.99, "alpha":0.2, "epsilon":1, "epsilon_decay_factor":100, "min_epsilon":0.1}
    
    rewards = [[1,1,1,0,0],[0,1,1,0,0],[1,1,1,1,1],[0,0,1,1,1]]
    
    reactions = [[-3,-2,-1,1,3],[-2,-2,0,1,3],[-2,-1,1,1,5],[-2,-1,1,2,5]]
    state_to_action_transitions = {"sad":("stare", "insult"), "mad":("stare", "attack","insult"), "happy":("compliment", "gift"), "neutral":("stare", "compliment", "insult")}
    
    action_to_state_transitions = {"attack":(("mad", "sad"),(0.5,0.5)), "insult":(("mad", "sad", "neutral"),(0.45,0.45,0.1)), "stare":(("neutral", "sad"),(0.8,0.1)), "compliment":(("sad","mad","happy"),(0.1,0.1,0.9)), "gift":(("sad","mad","happy"),(0.1,0.1,0.9))}
    
    def __init__(self, name, initial_happiness=0, q_preset=False, gamma = 0.99, alpha = 0.2, epsilon = 1, epsilon_decay_factor = 100):
        for k,v in enumerate(["mad", "sad", "neutral", "happy"]):
            self.state_index_map[k]=v
        for k,v in enumerate(["attack", "insult", "stare", "compliment", "gift"]):
            self.action_index_map[k]=v
        self.happiness = initial_happiness
        self.state = 2
        self.id = name
        self.last_action = "stare"
        if(not q_preset):
            self.q_table = [[0.0 for j in range(len(self.action_index_map))] for i in range(len(self.state_index_map))]
        else:
            self.q_table = q_preset
    
    def update(self, opponent_action=None):
        seed()
        if (not opponent_action):
            return choice(["attack", "insult", "stare", "compliment", "gift"])
        #print("recieved ",opponent_action)
        next_state = self.state_index_map[choices(self.action_to_state_transitions[opponent_action][0], weights=self.action_to_state_transitions[opponent_action][1], k=1)[0]]
        opponent_action = self.action_index_map[opponent_action]
        #print(self.state, next_state)
        #get negative feedback from action = do action less
        
        
        #self.state = self.state_index_map[self.state]
        #print(self.state, self.last_action, opponent_action)
        points = self.reactions[self.state][opponent_action]
        self.happiness += points
        if points <= 0:
            self.rewards[self.state][self.action_index_map[self.last_action]] -= 0.1
        if points > 0:
            self.rewards[self.state][self.action_index_map[self.last_action]] += 0.1
        del points
        #self.state = self.state_index_map[self.state]
        
        if (random() < self.params["epsilon"]):
            #print("choosing random action...")
            action = self.action_index_map[choice(["attack", "insult", "stare", "compliment", "gift"])]
        else:
            #print("decding action from q table")
            action = self.q_table[self.state].index(max(self.q_table[self.state]))
        
        #print(self.state, next_state, action)
        #da big q equation
        self.q_table[self.state][action] = self.q_table[self.state][action] + self.params["alpha"] * (self.rewards[self.state][action] + self.params["gamma"] * max(self.q_table[next_state]) - self.q_table[self.state][action])
        
        self.happiness += self.rewards[self.state][action]
        
        self.state = next_state
        self.last_action = self.action_index_map[action]
        #print(self.state, next_state, action)
        
        self.params["epsilon"] = max(self.params["min_epsilon"], self.params["epsilon"] * (1-self.params["epsilon_decay_factor"]))
        #print(self.id + " is now " + self.state_index_map[self.state])
        #print(self.id + " acts " + self.action_index_map[action]+"!")
        #print(self.id, self.last_action)
        return self.last_action
        
        
    def modify_params(self, gamma = None, alpha = None, epsilon = None, epsilon_decay_factor = None):
        if (gamma):
            self.params["gamma"] = gamma
        if (alpha):
            self.params["alpha"] = alpha
        if (epsilon):
            self.params["epsilon"] = epsilon
        if (epsilon_decay_factor):
            self.params["epsilon_decay_factor"] = epsilon_decay_factor
        print("parameters successfully modified")
    