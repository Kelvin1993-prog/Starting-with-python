#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Employee():
    """Employees annaul salary"""
    
    def __init__(self, first, last, salary):
        """Employees details"""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
        
    def give_raise(self, salary=5000):
        """Give the employee an add on"""
        self.salary += salary
    


# In[ ]:




