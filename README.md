# -AI-vacuum-cleaning-agent

Table-driven agents: 
oThe function consists in a lookup table of actions to be taken for every possible state of the environment.
oIf the environment has n variables, each with t possible states, then the table size is tn.
oOnly works for a small number of possible states for the environment.



Simple reflex agents: 

oDeciding on the action to take based only on the current perception and not on the history of perceptions.oBased on the condition-action rule: (if (condition) action)
oWorks if the environment is fully observable


Model-Based Reflex Agents:

oIf the world is not fully observable, the agent must remember observations about the parts of the environment it cannot currently observe.
oThis usually requires an internal representation of the world (or internal state).
oSince this representation is a model of the world, we call this model-based agent.
