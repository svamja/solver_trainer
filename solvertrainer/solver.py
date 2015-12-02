import copy
import random

advancement_size = 100
alternative_size = 6
step_range = (1, 10)
attempt_size = 10

def do_attempt(state_manager):
    prev_distance = 999
    attempt = { "path": [] }
    for i in range(advancement_size):
        alternative = do_try_alternatives(state_manager)
        if(alternative["distance"] < prev_distance):
            attempt["path"] += alternative["path"]
            attempt["distance"] = alternative["path"]
            state_manager = alternative["state_manager"]
    return attempt

def do_try_alternatives(state_manager):
    best_advancement = { "distance" : 999 }
    for i in range(alternative_size):
        state_manager2 = copy.deepcopy(state_manager)
        advancement = do_advance(state_manager)
        if(advancement["distance"] < best_advancement["distance"]):
            best_advancement["distance"] = advancement["distance"]
            best_advancement["state_manager"] = state_manager2
            best_advancement["path"] = advancement["path"]
    return best_advancement

def do_advance(state_manager):
    step_count = random.randint(*step_range)
    advancement = { "path" : [] }
    for i in range(step_count):
        step = do_take_step(state_manager)
        advancement["path"].append(step)
        advancement["distance"] = step["distance"]
        if(step["distance"] == 0): break
    return advancement

def do_take_step(state_manager):
    allowed_operations = state_manager.get_allowed_operations()
    operation = random.choice(allowed_operations)
    arguments = []
    for arg in operation["arguments"]:
        if(arg["type"] == "list"):
            arguments.append(random.choice(arg["items"]))
    getattr(state_manager, operation["name"])(*arguments)
    distance = state_manager.get_distance()
    step = { "operation" : operation["name"], "arguments" : arguments, "distance" : distance }
    return step

def solve(state_manager):
    best_attempt = False
    for i in range(1, attempt_size):
        state_manager2 = copy.deepcopy(state_manager)
        attempt = do_attempt(state_manager2)
        if(best_attempt == False or attempt["distance"] < best_attempt["distance"]):
            best_attempt = attempt
        if(best_attempt["distance"] == 0):
            break
    return best_attempt





