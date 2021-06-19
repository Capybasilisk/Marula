This is a simple stack machine that can carry out arbitrarily complex 
mathematical computations. It's not a universal machine as it lacks logical 
operators, conditional branching, and iteration, but the language it accepts can 
nevertheless approximate a wide range of functions.
    
A program for the machine is fed through the "run" method as a list of 
instructions and numbers. This serves as the input tape. Instructions are 
strings that are defined in the opcode tables below. These functions all take 
their arguments from the stack and return their results to the stack. Numbers 
can be integers or floats.
    
If the input tape's read-head encounters a number, it gets pushed onto the 
stack. If it comes across an instruction, it will check that there are an 
adequate number of arguments on the stack, pop them if there are, carry out the 
instruction, and push the result back on to the stack. Invalid items on the tape 
are ignored.
    
If there are no relevant arguments on the stack, the instruction gets 
skipped. The run method returns the number at the stop of the stack after the 
read-head comes to the end of the tape. Empty and invalid programs return 0.
    
Example programs:

stack = Marula()
    
stack.run([5, 5, "op_mul"])  #returns 25
    
stack.run([2, 80, "op_div"]) #80/2 returns 40.0

stack.run([5.7, "op_tanh"])  #returns 0.999978

stack.run([17, 8, "op_max"]) #returns 17
