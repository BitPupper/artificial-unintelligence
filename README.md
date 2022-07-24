# Artificial Unintelligence: solving social interaction awkwardness with even more awkward AIs
Created for SOSP week 4 PyGame project 

## What It Does / Motivation
This is just a small simulation/game which may provide a small amount of entertainment for those who try it out. 
My goal was to create an AI system which can fake having some intentionallity behind their actions -- that is, seemingly strategize for better results.
I chose the setting to be social interaction because it was the most unpredictable situation requiring strategy that I could think of. 

## How it Works
An agent has a limited number of emotional states it can be in: happy, sad, angry, and neutral. It can also perform certain actions based on what emotion it is currently experiencing: attack, insult, give a gift, compliment, and stare. What emotions the agent gets and what actions it takes are determined by what emotion it previously had/currently has through a simple markov state transition model (found in Agent.py).  The agent's actions are rewarded or punished through a q-learning function. The basic rule is that an agent gets points if it acts self-servingly (attacking when mad, giving a gift to make the other happy, etc)

Two of these agents are pitted against each other in the game, and by changing the PRETRAINED boolean variable in main.py, the user may change whether the agents are trained against each other for 100 iterations, or not. Be warned: setting PRETRAINED to True will cause the agents to prefer certain actions more than others, so if you want to see all that the actions the simulation has to offer, it may be better to leave it as False first.

## How to Contribute
I'd be delighted to hear about any ideas anyone has! Ways to make it more complex, or ways to make it more simple... Feel free to complain abaout my bad programming habits, too!

## How to use
It works best if all the files are downloaded to the same directory and then run main.py. The fallback plan if the code raises an error is this Repl (make sure to fullscreen it, otherwise screen gets cut off): [Link to repl](https://replit.com/@BitPupper/Socializing-Simulator)

## Reflections / Plans for the future
I plan to keep working on this, though I may end up re-writing the code entirely. 

### Current flaws of the project
1. It fails the initial objective: the AI agents don't really have any semblance of intentionality to their actions. It only takes into account their current emotion when performing an action, and whether that action has been rewarded before. 
2. It offers no gameplay/interaction on the player's side. Pretty boring after 1 minute.
  a. The main reason for this is probably because the agent's actions and range of emotions are too simple to be interesting.
  b. Another reason is that the only thing the player does is press space.

### Potential solutions (to corresponding numbered flaws above)
1. With my current resources and knowledge, I can't really make an AI system that can strategize through a social interaction with infinite possibilities. I was imagining putting two AIs in a little box and watching them squabble freely, hoping that they would suddenly do something smart, but that's not going to happen anytime soon. I should accept that and change my approach: make it a controlled simulation where the results are more predictable, like those educational simulations from [Nicky Case](https://ncase.me/) (idea credit goes to Harsh Deep). Now the big idea is to **Pit AI agents that are trained/coded differently against each other**, which simulates a situation where people from different cultures, norms, and perspectives all try to get along. This is a universal problem! It would be useful to be able to visualize it in a simplified manner using a handful of single brain-celled AIs, hunger games style!
2a. Add different emotions and actions depending on how the agents were trained! It's like knowing different languages giving you access to expressing unique emotions and thoughts.
2b. The player gets their own character amoung the AI agents, they get to choose what actions and emotions they have access to!
- Maybe add a gossip system?
