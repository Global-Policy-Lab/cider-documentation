#!/usr/bin/env python
# coding: utf-8

# In[7]:


import sys
sys.path.insert(0, '../../cider/cider')


# # Featurizer

# In[8]:


from datastore import DataStore
from featurizer import Featurizer


# Load some mobile phone metadata. See {doc}`standardized data formats <../data_formats/cdr>` for file schemas. 

# In[11]:


datastore = DataStore(cfg_dir='../../cider/configs/config.yml')
featurizer = Featurizer(datastore=datastore, clean_folders=True)


# Remove duplicate records, filter to just a specific date range, remove outlier days and spammers based on call and text volumes, and remove duplicate records in CDR, recharges, mobile data records, and mobile money records.

# In[4]:


# Deduplication
featurizer.ds.deduplicate()

# Filter to just January 1 - February 28 (inclusive)
featurizer.ds.filter_dates('2020-01-01', '2020-02-28')

# Remove transactions involving spammers who place 1.8+ calls/texts per active day
spammers = featurizer.ds.remove_spammers(spammer_threshold=1.8)


# In[5]:


# Remove all records from days more than 2 standard deviations from the mean transaction volume
outlier_days = featurizer.ds.filter_outlier_days(num_sds=2)


# Produce summary statistics and plots.

# In[6]:


print(featurizer.diagnostic_statistics())


# In[7]:


featurizer.diagnostic_plots()


# Featurize the data

# In[12]:


featurizer.cdr_features()
featurizer.international_features()
featurizer.location_features()
featurizer.recharges_features()
featurizer.mobiledata_features()
featurizer.mobilemoney_features()
featurizer.all_features()


# In[5]:


import pandas as pd
pd.read_csv('./outputs/featurizer/datasets/features.csv').head()


# Plot the distributions of some of the features.

# In[6]:


featurizer.feature_plots()

