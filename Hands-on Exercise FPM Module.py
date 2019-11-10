
# coding: utf-8

# # Hands-on Exercise for  FPM Module

# ### 1. Exploring properties of the dataset accidents_10k.dat. Read more about it here:  http://fimi.uantwerpen.be/data/accidents.pdf

# In[1]:


get_ipython().system('head accidents_10k.dat')


# <span style="color:red">**Question 1a:** </span>. How many items are there in the data?

# In[2]:


I = get_ipython().getoutput("awk -- '{for (i = 1; i <= NF; i++) wc[$i] += 1}; END {print length(wc)}' accidents_10k.dat")
Items=int(I[0])
Items


# 310 items

# <span style="color:red">**Question 1b:** </span> How many transactions are present in the data?

# In[3]:


get_ipython().system('wc -l accidents_10k.dat ')


# 10000 transactions

# <span style="color:red">**Question 1c:** </span>.  What is the length of the smallest transaction?

# In[4]:


a = get_ipython().getoutput("awk '{print NF}' accidents_10k.dat")
b=a.sort()
print (int(b[0]))


# Length of smallest transaction is 23

# <span style="color:red">**Question 1d:** </span>  What is the length of the longest transaction?

# In[5]:


print (int(b[-1]))


# Length of longest transaction is 45

# <span style="color:red">**Question 1e:** </span>  What is the size of the search space of frequent itemsets in this data?

# In[6]:


2**(Items)


# <span style="color:green">**Answer:** </span> 

# <span style="color:red">**Question 1f:** </span> 
# Assume that you work for the deparment of transportation that collected this data. What benefit do you see in using itemset mining approaches on this data?

# I can find the most prevailing circumstances for the occurrence of accidents.

# <span style="color:red">**Question 1g:** </span>  What type of itemsets (frequent, maximial or closed) would you be interested in discovering this dataset? State your reason.

# I prefer closed itemsets. Frequent itemsets for the given data will be very high in number with which we run short of computation power. Maximal sets provide summary of the frequent itemsets but there turns out to be some loss in the support of each subset and we can't state the support of it's subsets whereas closed itemsets are a lossless summary of all possible frequent itemsets.

# <span style="color:red">**Question 1h:** </span>  What minsup threshold would you use and why?

# It depends upon the number of transactions and items. We can't predict the minsup by just observing the dataset. May be in this case, minsup of 6000 can be taken for better computation(Frequent itemsets are a bit less).
# 

# ### 2. Generating frequent, maximal and closed itemsets using $\color{red}{\text{Apriori}}$, $\color{red}{\text{ECLAT}}$, and $\color{red}{\text{FPGrowth}}$ algorihtms from the dataset accidents_10k.dat 

# <span style="color:red">**Question 2a:** </span> Generate frequent itemsets using Apriori, for minsup = 2000, 3000, and 4000. Which of these minsup thresholds results in a maximum number of frequent itemsets? Which of these minsup thresholds results in a least number of frequent itemsets? Provide a rationale for these observations.

# In[7]:


get_ipython().system('chmod u+x apriori eclat fpgrowth prefixspan seqwog')
get_ipython().system('./apriori')
get_ipython().system('./eclat')
get_ipython().system('./fpgrowth')
get_ipython().system('./prefixspan')
get_ipython().system('./seqwog')


# In[8]:


get_ipython().system('./apriori -ts -s-2000 accidents_10k.dat accidents_2000_sup.txt')


# In[9]:


get_ipython().system('./apriori -ts -s-3000 accidents_10k.dat accidents_3000_sup.txt')


# In[10]:


get_ipython().system('./apriori -ts -s-4000 accidents_10k.dat accidents_4000_sup.txt')


# Minsup 4000 gives least number of frequent sets because it checks for only those frequent sets whose support>=4000 and ignores all the others.

# <span style="color:red">**Question 2b:** </span>   Using Apriori, compare the execution time for finding frequent itemsets for minsup = 2000, 3000, and 4000. Which of these minsup thresholds takes the least amount of time? Provide a rationale for this observation.

# In[11]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-2000 accidents_2000_sup.dat ')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# In[12]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-3000 accidents_3000_sup.dat ')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# In[13]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-4000 accidents_4000_sup.dat ')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# Minsup 4000 takes less time  

# <span style="color:red">**Question 2c:** </span> Using Apriori, find the frequent itemsets for minsup = 2000, 3000, and 4000. Determine the number of itemsets for each size (1 to max length of an itemset). What trends do you see that are common for all three minsup thresholds? What trends do you see that are different? Provide a rationale for these observations.

# In[14]:


from collections import Counter 
a = get_ipython().getoutput("awk '{print NF-1}' accidents_2000_sup.txt")
b=list(zip(Counter(a).keys(), Counter(a).values()))
b.sort(key = lambda x: int(x[0]))
b


# In[15]:


get_ipython().system("awk '{print NF-1}' accidents_3000_sup.txt|sort -n|uniq -c")


# In[16]:


get_ipython().system("awk '{print NF-1}' accidents_4000_sup.txt|sort -n|uniq -c")


# Number of itemsets are greatly reduced from minsup 2000 to 4000. 
# Similarity : Count of frequent itemsets with length 1 to 6 increase and then it decreases which is similar to the normal distribution.
# Difference : Count of frequent itemsets (for every length) decreases from minsup 2000 to minsup 4000.
# Rationale : We only check for the itemsets whose support >= 4000 in minsup 4000 case which rules out itemsets.

# <span style="color:red">**Question 2d:** </span>  Using Apriori with minsup=2000, compare the number of frequent, maximal, and closed itemsets. Which is the largest set and which is the smallest set? Provide a rationale for these observations.

# In[17]:


get_ipython().system('./apriori -tm -s-4000 accidents_4000_sup.txt ')


# In[18]:


get_ipython().system('./apriori -tc -s-4000 accidents_4000_sup.txt')


# In[19]:


get_ipython().system('./apriori -ts -s-4000 accidents_10k.dat accidents_4000_sup.txt')


# Largest  : Frequent itemsets(F)
# Smallest : Maximal itemsets(M=Itemsets which have no frequent supersets)
# Closed itemsets(C) are the ones which have no frequent supersets of same support.
# Rationale : 
# M ⊆ C ⊆ F

# <span style="color:red">**Question 2e:** </span> For a minsup = 2000, compare the execution time for Apriori, ECLAT and FPGrowth. Which of these algorithms took the least amount of time. Provide a rationale for this observation.

# In[20]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-2000 accidents_10k.dat')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# In[21]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./eclat -ts -s-2000 accidents_10k.dat ')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# In[22]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./fpgrowth -ts -s-2000 accidents_10k.dat')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# fp Growth perform much better than the other two. 
# In Apriori, candidate set generation and Database scans(equal to the max length of the itemset) happens. Database scan is highly expensive incase of large Database.
# Whereas in ECLAT, although candidate set generation and Database scan happens. Database is scanned only once because it uses an inverted index to store the dataset which is better compared to Apriori.
# 

# <span style="color:red">**Question 2f:** </span> For a minsup = 4000, compare the execution time for Apriori, ECLAT and FPGrowth. Which of these algorithms took the least amount of time. Provide a rationale for this observation.

# In[23]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-4000 accidents_10k.dat')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# In[24]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./eclat -ts -s-4000 accidents_10k.dat')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# In[25]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./fpgrowth -ts -s-4000 accidents_10k.dat')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# FpGrowth performs better.In Apriori, candidate set generation and Database scans(equal to the max length of the itemset) happens. Database scan is highly expensive incase of large Database.
# Whereas in ECLAT, although candidate set generation and Database scan happens. Database is scanned only once because it uses an inverted index to store the dataset which is better compared to Apriori.

# <span style="color:red">**Question 2g:** </span>  For a minsup = 6000, compare the execution time for Apriori, ECLAT and FPGrowth. Which of these algorithms took the least amount of time. Provide a rationale for this observation.

# In[26]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-6000 accidents_10k.dat')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# In[27]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./eclat -ts -s-6000 accidents_10k.dat')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# In[28]:


import datetime 
start = datetime.datetime.now()
get_ipython().system('./fpgrowth -ts -s-6000 accidents_10k.dat')
end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds,"secs ",elapsed.microseconds,"microsecs");


# FpGrowth performs better.In Apriori, candidate set generation and Database scans(equal to the max length of the itemset) happens. Database scan is highly expensive incase of large Database. Whereas in ECLAT, although candidate set generation and Database scan happens. Database is scanned only once because it uses an inverted index to store the dataset which is better compared to Apriori.

# <span style="color:red">**Question 2h:** </span> Fill the following table based on execution times computed in __2e__, __2f__, and __2g__. State your observations on the relative computational efficiency at different support thresholds. Based on your knowledge of these algorithms, provide the reasons behind your observations.

# |   Algorithm                |minsup=2000         |minsup=4000         |minsup=6000         |
# |----------------------------|--------------------|--------------------|--------------------|    
# |Apriori                     |19 secs  691012 ms  |1 secs  567695ms    |          304428    |
# |Eclat                       |557436              |288465              |          270384    |
# |FPGrowth                    |343202              |275427              |          265278    |

# FpGrowth performs better.In Apriori, candidate set generation and Database scans(equal to the max length of the itemset) happens. Database scan is highly expensive incase of large Database. Whereas in ECLAT, although candidate set generation and Database scan happens. Database is scanned only once because it uses an inverted index to store the dataset which is better compared to Apriori.

# ### 3. Discovering frequent subsequences and substrings

# Assume that roads in a Cincinnati are assigned numbers. Participants are enrolled in a transportation study and for every trip they make using their car, the sequence of roads taken are recorded. Trips that involves freeways are excluded. This data is in the file <span style="color:blue">road_seq_data.dat</span>.

# <span style="color:red">**Question 3a:** </span>  What 'type' of sequence mining will you perform to determine frequently taken 'paths'? Paths are sequences of roads traveresed consecutively in the same order.

# Projection or vertical based

# <span style="color:red">**Question 3b:** </span> How many sequences are there in this sequence database?

# In[29]:


get_ipython().system('wc -l road_seq_data.dat')


# 1000 sequences

# <span style="color:red">**Question 3c:** </span> What is the size of the alphabet in this sequence database?

# In[30]:


S = get_ipython().getoutput("awk -- '{for (i = 1; i <= NF; i++) wc[$i] += 1}; END {print length(wc)}' road_seq_data.dat")
ns=int (S[0])
ns


# 1283 

# <span style="color:red">**Question 3d:** </span> What are the total number of possible subsequences of length 2 in this dataset?

# In[31]:


ns*ns


# <span style="color:red">**Question 3e:** </span> What are the total number of possible substrings of length 2 in this dataset?

# In[32]:


ns-2+1


# <span style="color:red">**Question 3f:** </span> Discover frequent __subsequences__ with minsup = 10 and report the number of subsequences discovered.

# In[33]:


get_ipython().system('./prefixspan -min_sup 10 road_seq_data.dat')


# In[34]:


get_ipython().system("./prefixspan -min_sup 10 road_seq_data.dat| sed -n 'p;n'| wc -l")


# 4589 sequences

# <span style="color:red">**Question 3g:** </span>  Discover frequent __substrings__ with minsup = 10 and report the number of substrings discovered.

# In[35]:


get_ipython().system('./seqwog -ts -s-10 road_seq_data.dat road_sub_string')


# In[36]:


get_ipython().system('wc -l road_sub_string')


# 613 substrings

# <span style="color:red">**Question 3h:** </span> Explain the difference in the number of frequent subsequences and substrings found in __3f__ and __3g__ above.

# Consecutive sequence of symbols is substring whereas a subsequence need not have consecutive symbols(There can be gaps between symbols). Hence we can have many combination of subsequence when compared to substring.
