#!/usr/bin/env python
# coding: utf-8

# In[5]:


def make_car(name, model, **car_info):
    """Displays info of a car in a dict"""
    car_profile = {}
    car_profile['name'] = name.title()
    car_profile['model'] = model
    for key, value in car_info.items():
        car_profile[key.title()] = value.title()
    return car_profile


# In[ ]:




