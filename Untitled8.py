#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import deque


class parenthesis_checker():
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    def Checker(self, myStr):
        
        self.stack = deque()
        
        for i in myStr:
            
            if i in self.open_list:
                self.stack.append(i)
                
            elif i in self.close_list:
                
                pos = self.close_list.index(i)
                
                if ((len(self.stack) > 0) and (self.open_list[pos] == self.stack[len(self.stack) - 1])):
                    self.stack.pop()
                    
                else:
                    return "FALSE"                 #unbalanced
                
                if len(self.stack) == 0:
                    return "TRUE"                #balanced 
                
                else:
                    return "FALSE"                 #unbalanced


object = parenthesis_checker()

string = "{[]{()}}"
print(object.Checker(string))

string = "[{}{})(]"
print(object.Checker(string))


# In[ ]:




