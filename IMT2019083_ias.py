from IMT2019083_ac import *
from IMT2019083_ibr import *
from IMT2019083_ir import *
from IMT2019083_mar import *
from IMT2019083_mbr import *
from IMT2019083_memory import *
from IMT2019083_mq import *
from IMT2019083_pc import *
from IMT2019083_aux import *

class IAS:

    def __init__(self):
        self.memory = Memory()
        self.pc = PC()
        self.mbr = MBR()
        self.mar = MAR(self.pc)
        self.ibr = IBR()
        self.ir = IR()
        self.mq = MQ()
        self.ac = AC()
        self.halt = False

    def Cycles(self):
        print("Initial Memory State -")
        print()
        self.memory.printall()
        print()
        self.Fetch()
        print("Final Memory State -")
        print()
        self.memory.printall()
        
    
    def Fetch(self):  
        while not self.halt:
        
            if (self.ibr.get() == ""): 
            
                self.mar.set_address(self.pc.get_address()) 
                self.mbr.set(self.memory.get(self.mar.get_address()))  
                self.ibr.set(self.mbr.get()[20:]) 
                self.ir.set(self.mbr.get()[0:8])  
                self.mar.set_address(self.mbr.get()[8:20])  
                self.pc.set_address(dec_to_unsign(unsign_to_dec(self.pc.get_address()) + 1))  
                
            else:
            
                self.ir.set(self.ibr.get()[0:8]) 
                self.mar.set_address(self.ibr.get()[8:20])  
                self.ibr.set("") 

            self.Execute()
            

    def Execute(self):
        
        
        mapping = {"00001010":self.LOAD_MQ, "00001001":self.LOAD_MQ_MX,"00100001":self.STOR_MX, "00000001":self.LOAD_MX, "00000010":self.LOAD_negMX,
                    "00000011":self.LOAD_MODMX, "00000100":self.LOAD_NEGMODMX, "00001101":self.JUMP_MX_LEFT,"00001110":self.JUMP_MX_RIGHT,"00001111":self.JUMP_posMX_LEFT,
                    "00010000":self.JUMP_posMX_RIGHT,"00000101":self.ADD_MX,"00000111":self.ADD_MODMX,"00000110":self.SUB_MX,"00001000":self.SUB_MODMX,"00001100":self.DIV_MX,
                    "00010100":self.LSH, "00010101":self.RSH, "11111111":self.HALT}

        mapping[self.ir.get()]()
        

    def LOAD_MQ(self):  

        self.ac.set(self.mq.get())    

    def LOAD_MQ_MX(self):
    
        self.mq.set(self.memory.get(self.mar.get_address()))

    def STOR_MX(self):  
    
        self.memory.set(self.mar.get_address(), self.ac.get())

    def LOAD_MX(self):
        self.ac.set(self.memory.get(self.mar.get_address()))    

    def LOAD_negMX(self):
        
        self.ac.set(dec_to_sign(-sign_to_dec(self.memory.get(self.mar.get_address()))))    

    def LOAD_MODMX(self):
    
        self.ac.set(dec_to_sign(abs(sign_to_dec(self.memory.get(self.mar.get_address())))))    

    def LOAD_NEGMODMX(self):
    
        self.ac.set(dec_to_sign(-abs(sign_to_dec(self.memory.get(self.mar.get_address())))))            

    def JUMP_MX_LEFT(self):
    
        self.ibr.set("") 
        self.pc.set_address(self.mar.get_address()) 
        

    def JUMP_MX_RIGHT(self):
    
        self.ibr.set(self.memory.get(self.mar.get_address())[20:40]) 
        self.pc.set_address(dec_to_sign(unsign_to_dec(self.mar.get_address()) + 1)) 
        

    def JUMP_posMX_LEFT(self):
    
        if (sign_to_dec(self.ac.get()) > 0):
        
            self.ibr.set("")
            self.pc.set_address(self.mar.get_address())

    def JUMP_posMX_RIGHT(self):
    
        if (sign_to_dec(self.ac.get()) > 0):
        
            self.ibr.set(self.memory.get(self.mar.get_address())[20:40]) 
            self.pc.set_address(dec_to_sign(unsign_to_dec(self.mar.get_address()) + 1)) 
        

    def ADD_MX(self):
    
        self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) + sign_to_dec(self.memory.get(self.mar.get_address()))))

    def ADD_MODMX(self):
    
        if (sign_to_dec(self.memory.get(self.mar.get_address())) > 0):
            self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) + sign_to_dec(self.memory.get(self.mar.get_address()))))
        else:
            self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) - sign_to_dec(self.memory.get(self.mar.get_address()))))

    def SUB_MX(self): 
    
        self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) - sign_to_dec(self.memory.get(self.mar.get_address()))))

    def SUB_MODMX(self):
    
        if (sign_to_dec(self.memory.get(self.mar.get_address())) > 0):
            self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) - sign_to_dec(self.memory.get(self.mar.get_address()))))
        else:
            self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) + sign_to_dec(self.memory.get(self.mar.get_address()))))

    def DIV_MX(self):

        self.mq.set(dec_to_sign(int(sign_to_dec(self.ac.get()) / sign_to_dec(self.memory.get(self.mar.get_address())))))
        self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) % sign_to_dec(self.memory.get(self.mar.get_address()))))

    def LSH(self):
    
        self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) << 1))

    def RSH(self):
        self.ac.set(dec_to_sign(sign_to_dec(self.ac.get()) >> 1))
        

    def HALT(self):
        self.halt = True 
    