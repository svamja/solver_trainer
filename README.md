# Solver Trainer

A Machine Learning Framework

### Philosophy

* Easy to use for developers
* Black Box approach to what problem is being solved
* Learns like a kid - starts very inefficiently, but grows smart too soon!

### Framework Overview

Please see this 
<a href="https://docs.google.com/presentation/d/19FL5I4YY1C8wIJ0FeWxuIIuz4m4u7IcpsZsSe_9f5II/pub?start=false&loop=false&delayms=5000" target="_blank">Google Slides Presentation</a> (Opens in new window)

### Sample Developer's Implementation

    class SlidingPuzzleStateManager(StateManager):
    	state = []
    	def __init__(self): ..
    	def get_solution_distance: ..
    	def alllowed_operations:
    		return [“go_top”, “go_left”, “go_right”, “go_bottom”];
    	def go_top: ..
    	def go_left: ..
    	..
    state_manager = SlidingPuzzleStateManager()
    state_manager.change_state_to([....])
    Solver.solve(state_manager)
    state_manager.print_solution() # or whatever
    


