
from __future__ import print_function
from midca import base
from midca.worldsim import domainread, stateread, worldsim
from midca.modules import simulator, perceive, note, guide, evaluate, intend, planning, act
# from midca.domains.blocksworld.plan import methods_midca, operators_midca
from midca.domains.blocksworld.plan import methods, operators
from midca.domains.blocksworld import util
import inspect, os
import sys
import midca

'''
MIDCA 

 world
 Memory()
 phases = []
 metaPhases = []
 modules = {}
 metaModules = {}
 verbose


Cognitive Phases: 

1. Perceive (perceive.py)

2. Interpret 
  - note (note.py) [sub phases]
  - assess (assess.py) [sub phases]
  - guide (guide.py) [sub phases]

3. Evaluate (evaluate.py)

4. Intend (intend.py)

5. Plan (planning.py)

6. Act (act.py)


pyhop.py 

State 

Goal 

tasks 

plan

declare_operators 

declare_methods 

seek_plan

util.py 

state from world 

tasks from goal

  (need to add other predicates )


'''


'''

Initital world:



      -----
	  | B | (blue)
	  -----             -----
      | A | (red)       | C | (green)       / \
                                           / D \ (yellow)
-------------------------------------

Possible predicates:
	['on', 'arm-empty', 'triangle', 'color', 'clear', 'holding', 'on-table', 'table', 'block']
Possible arguments:
	['A', 'BLUE', 'C', 'B', 'D', 'YELLOW', 'GREEN', 'table', 'RED']

Operators:

Methods:

for a goal:  Goal(B, predicate: on-table)

Plan:
  unstack(D, B)
  putdAbwn(D)
  unstack(B, A)
  putdown(B)

for a action:


'''



thisDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(thisDir)
MIDCA_ROOT = thisDir + "/midca/"
DISPLAY_FUNC = print
# DISPLAY_FUNC = util.asqiiDisplay
DOMAIN_FILE = MIDCA_ROOT + "domains/blocksworld/domains/gi_domain.sim"
STATE_FILE = MIDCA_ROOT + "domains/blocksworld/states/gi_state.sim"
# DECLARE_METHODS_FUNC = methods_midca.declare_methods
# DECLARE_OPERATORS_FUNC = operators_midca.declare_ops

DECLARE_METHODS_FUNC = methods.declare_methods
DECLARE_OPERATORS_FUNC = operators.declare_ops

argsPyHopPlanner = [util.pyhop_state_from_world,
					util.pyhop_tasks_from_goals,
					DECLARE_METHODS_FUNC,
					DECLARE_OPERATORS_FUNC]

world = domainread.load_domain(DOMAIN_FILE)
stateread.apply_state_file(world, STATE_FILE)
#creates a PhaseManager object, which wraps a MIDCA object
myMidca = base.PhaseManager(world, display = DISPLAY_FUNC, verbose=2)
#add phases by name
for phase in ["Simulate", "Perceive", "Interpret", "Eval", "Intend", "Plan", "Act"]:
    myMidca.append_phase(phase)

myMidca.append_module("Simulate", simulator.MidcaActionSimulator())
myMidca.append_module("Simulate", simulator.ASCIIWorldViewer(display=DISPLAY_FUNC))
myMidca.append_module("Perceive", perceive.PerfectObserver()) ## add in SRL
myMidca.append_module("Interpret", note.ADistanceAnomalyNoter())

#UserGoalInput getUserInstruction  world, mem, verbose
myMidca.append_module("Interpret", guide.GoalInference(world))
# myMidca.append_module("Interpret", guide.UserGoalInput())

myMidca.append_module("Eval", evaluate.SimpleEval())
myMidca.append_module("Intend", intend.SimpleIntend())
myMidca.append_module("Plan", planning.PyHopPlanner(*argsPyHopPlanner))
myMidca.append_module("Act", act.GoalInferenceAct(world))

print(myMidca.get_phases())
#tells the PhaseManager to copy and store MIDCA states so they can be accessed later.
myMidca.storeHistory = True
myMidca.init()
myMidca.run()
