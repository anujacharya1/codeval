'''
Created on Sep 12, 2013

@author: anujacharya
'''
import sys

class ReverseWords:
    
    def __init__(self,input):
        self.input = input
        self.stack = list()
        
    
    def one_liner(self):
        if self.input is not '':
            print " ".join(self.input.split()[::-1])
    
    def reverse_logic(self):
        
        if self.input is not '':
            
            word =''
            for char in self.input:
                word +=char
                if char is ' ':    
                    self.stack.append(word)
                    word = ''
            self.stack.append(word)
            
            newResultString = ''
            # Pop all elements on stack thats your answer
            while len(self.stack) is not 0:
                newResultString += self.stack.pop()+ ' '
            
            print newResultString
        
if __name__ == '__main__':
    # file = open('/Users/anujacharya/Documents/workspace/CodeEval/test.txt','r')
    with open('/Users/anujacharya/Documents/workspace/CodeEval/test.txt', 'r') as f:
        for line in f:
            line = line.strip()
            rw = ReverseWords(line)
            rw.one_liner()