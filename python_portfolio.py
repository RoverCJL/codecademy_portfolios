#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[18]:


import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#access csv file and retrieve insurance list into dictionary
def get_insurance_list():
    
    insurance_list = []
    
    with open("insurance.csv") as insurance:
        insurance_reader = csv.DictReader(insurance)
        for row in insurance_reader:
            user = {}
            user["Age"] = row["age"]
            user["Sex"] = row["sex"]
            user["BMI"] = row["bmi"]
            user["Children"] = row["children"]
            user["Smoker"] = row["smoker"]
            user["Region"] = row["region"]
            user["TotalCost"] = row["charges"]
            insurance_list.append(user)
    return insurance_list


# In[8]:


#find average age of patients
def get_average_age(insurance_list):
    total_age = 0
    count = 0
    for person in insurance_list:
        total_age += int(person["Age"])
        count += 1
    return total_age/count
print("The average age of all patients(to 2s.f) is " + "{:.2f}".format(get_average_age(get_insurance_list())) + ".")
   


# In[44]:


#find the most common region that patients originate from
def get_most_common_region(insurance_list):
    region_list = []
    for person in insurance_list:
        region_list.append(person["Region"])
    return max(region_list,key=region_list.count)
print("The most common region that patients originate from is the " + get_most_common_region(get_insurance_list()) + ".")


# In[12]:


#analyse cost between smokers and non-smokers
def smoker_diff(insurance_list):
    smoker_count = 0
    smoker_total = 0.0
    non_smoker_count = 0
    non_smoker_total = 0.0
    for person in insurance_list:
        if person["Smoker"] == "yes":
            smoker_total += float(person["TotalCost"])
            smoker_count += 1
        else:
            non_smoker_total += float(person["TotalCost"])
            non_smoker_count += 1
    smoker_average = smoker_total / smoker_count
    non_smoker_average = non_smoker_total / non_smoker_count
    return int((smoker_average-non_smoker_average)/non_smoker_average*100)
print("On average, a smoker pays " + str(smoker_diff(get_insurance_list())) + "% more than a non-smoker for their health insurance.")


# In[16]:


#find average age of someone who has at least 1 child
def get_average_age_of_parent(insurance_list):
    total_age = 0
    parent_list = []
    for person in insurance_list:
        if int(person["Children"]) >= 1:
            parent_list.append(person)
    for parent in parent_list:
        total_age += int(parent["Age"])
    return total_age/len(parent_list)
print("The average age of someone who has at least 1 child is " + "{:.0f}".format(get_average_age_of_parent(get_insurance_list())) + " years old.")


# In[99]:


#plot graph for age against insurance cost



userdata = pd.read_csv("insurance.csv")
primaryDF = pd.DataFrame(userdata)

age = primaryDF["age"]
totalcost = primaryDF["charges"]
ax = sns.barplot(x=age,y=totalcost,data=primaryDF)

ax.set_yticks([0,5000,10000,15000,20000,25000,30000])
ax.set_yticklabels(["0K","5K","10K","15K","20K","25K","30K"])

ax.set_xticks([0,20,40,60,80])
ax.set_xticklabels(["0","20","40","60","80"])

plt.xlabel("Age")
plt.ylabel("Insurance Cost")
plt.title("Relation between Age and Insurance Cost",fontsize=20)

plt.show()


# In[ ]:


plt.close()

