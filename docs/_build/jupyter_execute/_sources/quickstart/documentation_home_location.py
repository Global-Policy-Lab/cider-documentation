#!/usr/bin/env python
# coding: utf-8

# # Home Location Inference

# In[1]:


from datastore import DataStore
from home_location import HomeLocator


# Load some CDR data, antennas data, and (optionally) spatial files, whose paths have been defined in `config.yml`. Define the geographic granularity for inference (options are ‘antenna_id’, ‘tower_id’ if a tower_id is provided in the antennas files, or any of the spatial files). Optionally load wealth prediction data to construct a poverty map and ground truth location data to evaluate accuracy.

# In[3]:


datastore = DataStore(cfg_dir='./configs/config.yml')
home_locator = HomeLocator(datastore=datastore, clean_folders=True)


# Filter to a specific date range.

# In[4]:


home_locator.ds.filter_dates('2020-01-05', '2020-02-01')


# Try running the three different home location algorithms, specifying towers as the requested geographic level of aggregation.

# ```{note}
# The three algorithms currently implemented are relatively simple; more sophisticate methods to infer users' home locations do exist.
# ```

# In[5]:


home_locator.get_home_locations(algo='count_transactions', geo='tower_id')
home_locator.get_home_locations(algo='count_days', geo='tower_id')
home_locator.get_home_locations(algo='count_modal_days', geo='tower_id')


# Generate a population map based on inferred home locations using the unique days algorithm. Use points at each of the tower locations.

# In[6]:


home_locator.map(algo='count_days', geo='tower_id', kind='population', voronoi=False)


# Evaluate the accuracy of the home location inference using the ground truth data. Generate maps and a table of precision and recall for each tower.

# In[7]:


home_locator.accuracy(algo='count_days', geo='tower_id')
home_locator.map(algo = 'count_days', geo='tower_id', kind='recall', voronoi=False)


# In[8]:


home_locator.accuracy_tables[('tower_id', 'count_days')].head()


# Use population density maps to identify which areas are over/under-represented in your sample.

# In[9]:


home_locator.pop_comparison(algo='count_days', geo='tower_id')

