# Goal Inference
---

Inferring the underlying goal/task, given a user instruction (usually in spoken natural language). 

--- 

# Inference through Condition Checks: 

We now describe our goal inference procedure which integrates natural language processing tech- niques including synonym generation and SRL into the comprehension phases of MIDCA’s action- perception loop. To better explain the novelty of our model, we consider an environment where a human gives voice instructions and a self-regulated autonomous agent analyzes those instructions to infer a requested action or implied goal. Also For the purposes of this work, we assume that all voice instructions are rendered as text using an error-free process. To understand the intent of an instruction, the agent performs a simple test. In order for an instruction to be interpreted as an executable action, all preconditions on that action must be satisfied. If the test is passed, we infer that that action is the correct interpretation of the user’s intent. Otherwise, the agent assumes that the user intent must have been an end-state they desire. The end-state, when achieved, satisfies the postconditions of the operator. In this case, the agent infers that the user intended to specify a goal and constructs a plan to achieve it.

![Conceptual Model](/Conferences/ACS2020/model.png)

This was produced for ACS 2020 Conference. 

---
