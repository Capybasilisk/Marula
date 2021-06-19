import math
import collections




class Marula:
    
    """
    
    This is a simple stack machine that can carry out 
    arbitrarily complex mathematical computations. 
    It's not a universal machine as it lacks logical 
    operators, conditional branching, and iteration, 
    but the language it accepts can nevertheless 
    approximate a wide range of functions.
    
    A program for the machine is fed through the 
    "run" method as a list of instructions and numbers. 
    This serves as the input tape. Instructions are
    strings that are defined in the opcode tables below. 
    These functions all take their arguments from the 
    stack and return their results to the stack. 
    Numbers can  be integers or floats.
    
    If the input tape's read-head encounters a number, 
    it gets pushed onto the stack. If it comes across 
    an instruction, it will check that there are an 
    adequate number of arguments on the stack, pop 
    them if there are, carry out the instruction, and 
    push the result back on to the stack. Invalid items 
    on the tape are ignored.
    
    If there are no relevant arguments on the stack, 
    the instruction gets skipped. The run method
    returns the number at the stop of the stack after 
    the read-head comes to the end of the tape. Empty 
    and invalid programs return 0.
    
    Example programs: 
    
    stack.run([5, 5, "op_mul"])  # returns 25
    
    stack.run([2, 80, "op_div"]) # 80/2 returns 40.0
    
    stack.run([5.7, "op_tanh"])  # returns 0.999977

    stack.run([17, 8, "op_max"]) # returns 17    
    
    """
    

    def __init__(self):
          
        #Initiate stack
          
        self.STACK = collections.deque()
        
        
        #OPCode dictionaries
        
        self.STACK_OPS = {
            
            "op_size" : self.size,
            "op_peek" : self.peek,
            "op_pop"  : self.pop,
            "op_push" : self.push
            
            }
        
    
        self.MATH_OPS = {
        
            "op_add" : self.add,
            "op_sub" : self.sub,
            "op_mul" : self.mul,
            "op_div" : self.div,
            "op_mod" : self.mod,
            "op_flr" : self.floor, 
            "op_cei" : self.ceil,
            "op_sig" : self.sign,
            "op_abs" : self.fabs,
            "op_neg" : self.neg,
            "op_min" : self.argmin,
            "op_max" : self.argmax,
            "op_sqrt" : self.sqrt,
            "op_pwr" : self.pwr,
            "op_log" : self.log,
            "op_exp" : self.exp,
            "op_gma": self.gamma,
            "op_sin" : self.sin,
            "op_cos" : self.cos,
            "op_tan" : self.tan,
            "op_asin" : self.asin,
            "op_acos" : self.acos,
            "op_atan" : self.atan,
            "op_sinh" : self.sinh,
            "op_cosh" : self.cosh,
            "op_tanh" : self.tanh,
            "op_asinh" : self.sinh,
            "op_acosh" : self.acosh,
            "op_atanh" : self.atanh

            }
        
        
        self.OP_CODES = {
            
            **self.STACK_OPS, 
            **self.MATH_OPS
            
            }
    
    
    #Stack manipulation methods
    
    def size(self):
        """Get size of stack"""
        return len(self.STACK)
    
    
    def peek(self):
        """Get the top items of the
        stack without removing it."""
        if self.STACK:
            return self.STACK[0]
        else:
            return 0

    
    def pop(self):
        "Pop item off the stack"
        return self.STACK.pop()
    
    
    def push(self, num):
        "Push item onto the stack"
        return self.STACK.append(
            num)
    
    
    #Mathematical operations
    
    def add(self):
        if self.size() > 1:
            a = self.pop()
            b = self.pop()
            self.push(a+b)
    
    
    def sub(self):
        if self.size() > 1:
            a = self.pop()
            b = self.pop()
            self.push(a-b)
    
    
    def mul(self):
        if self.size() > 1:
            a = self.pop()
            b = self.pop()
            self.push(a*b)
    
    
    def div (self):
        if self.size() > 1:
            a = self.pop()
            b = self.pop()
            self.push(a/b)
    
    
    def mod(self):
        """C standard modulo"""
        if self.size() > 1:
            a = self.pop()
            b = self.pop()
            self.push(math.fmod(a,b))
    
    
    def floor(self):
        if self.size() > 0 and isinstance(
            self.peek(),float):
            a = self.pop()
            self.push(math.floor(a))
    
    
    def ceil(self):
        if self.size() > 0 and isinstance(
            self.peek(),float):
            a = self.pop()
            self.push(math.ceil(a))
    
    
    def sign(self):
        """Get sign bit of number"""
        if self.size() > 0:
            a = self.pop()
            if a > 0:
                self.push(1)
            elif a < 0:
                self.push(-1)
            else:
                self.push(0)
    
    
    def fabs(self):
        """Absolute value"""
        if self.size() > 0:
            a = self.pop()
            self.push(abs(a))
    
    
    def neg(self):
        """Inverter"""
        if self.size() > 0:
            a = self.pop()
            self.push(-a)
    
    
    def argmin(self):
        if self.size() > 1:
            a = self.pop()
            b = self.pop()
            self.push(min(a,b))

    
    def argmax(self):
        if self.size() > 1:
            a = self.pop()
            b = self.pop()
            self.push(max(a,b))
           
    
    
    def sqrt(self):
        if (self.size() > 0 
            and self.peek() > 0):
            a = self.pop()
            self.push(math.sqrt(a))
    
    
    def pwr(self):
        if (self.size() > 1
           and self.peek() > 0):
            a = self.pop()
            b = self.pop()
            self.push(math.pow(a,b)) 
    
    
    def log(self):
        if (self.size() > 0 
            and self.peek() > 0):
            a = self.pop()
            self.push(math.log(a))
    
    
    def exp(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.exp(a))
        
    
    def gamma(self):
        if (self.size() > 0
            and self.peek() > 0):
            a = self.pop()
            self.push(math.gamma(a))
    
    
    def sin(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.sin(a))
    
    
    def cos(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.cos(a))
    
    
    def tan(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.tan(a))
   
    
    def asin(self):
        if (self.size() > 0
            and not self.peek() > 1
            and not self.peek() < -1):
            a = self.pop()
            self.push(math.asin(a))
    
   
    def acos(self):
        if (self.size() > 0
            and not self.peek() > 1
            and not self.peek() < -1):
            a = self.pop()
            self.push(math.acos(a))
    
   
    def atan(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.atan(a))
    
    
    def sinh(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.sinh(a))
    
    
    def cosh(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.cosh(a))
            
            
    def tanh(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.tanh(a))
    
    
    def asinh(self):
        if self.size() > 0:
            a = self.pop()
            self.push(math.asinh(a))
    
    
    def acosh(self):
        if (self.size() > 0
            and not self.peek() < 1):
            a = self.pop()
            self.push(math.acosh(a))
    
    
    def atanh(self):
        if (self.size() > 0
            and self.peek() < 1
            and self.peek() > -1):
            self.push(math.atanh(a))
            
            
    # Main method
    
    def run(self, program):
       
       """
       
       This is the input tape for the stack machine.
       Programs must be in the in the form of a list
       of instructions and numbers.
        
       """
        
        
       if not isinstance(program, list):
           raise ValueError(
               "Inputs must be in a list.")
        
       for element in program:
           if isinstance(element, (int, float)):
               self.push(element)
           else:  
               if element in self.MATH_OPS:
                   try:
                       self.MATH_OPS[element]()
                   except:
                       continue
            
       if self.STACK:
           return self.STACK[-1]
       
       self.push(0)
       
       return self.STACK[0]
   
   
   
   
   
