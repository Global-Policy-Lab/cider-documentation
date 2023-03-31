#!/usr/bin/env python
# coding: utf-8

# # Featurizer

# In[9]:


from cider.datastore import DataStore
from cider.featurizer import Featurizer


# Load some mobile phone metadata. See {doc}`standardized data formats <../data_formats/cdr>` for file schemas. 

# In[2]:


# This path should point to your cider installation, where configs and data for this demo are located.
from pathlib import Path
cider_installation_directory = Path('../../cider')

datastore = DataStore(config_file_path_string= cider_installation_directory / 'configs' / 'config_quickstart.yml')
featurizer = Featurizer(datastore=datastore, clean_folders=True)


# Remove duplicate records, filter to just a specific date range, remove outlier days and spammers based on call and text volumes, and remove duplicate records in CDR, recharges, mobile data records, and mobile money records.

# In[3]:


# Deduplication
featurizer.ds.deduplicate()

# Filter to just January 1 - February 28 (inclusive)
featurizer.ds.filter_dates('2020-01-01', '2020-02-28')

# Remove transactions involving spammers who place 1.8+ calls/texts per active day
spammers = featurizer.ds.remove_spammers(spammer_threshold=1.8)


# In[4]:


# Remove all records from days more than 2 standard deviations from the mean transaction volume
outlier_days = featurizer.ds.filter_outlier_days(num_sds=2)


# Produce summary statistics and plots.

# In[5]:


print(featurizer.diagnostic_statistics())


# In[6]:


featurizer.diagnostic_plots()


# Featurize the data

# In[26]:


featurizer.cdr_features_spark()
featurizer.international_features()
featurizer.location_features()
featurizer.recharges_features()
featurizer.mobiledata_features()
featurizer.mobilemoney_features()

featurizer.all_features()


# Now we read the features back with pandas in to see what the table looks like. This works fine because our synthetic dataset is small, but such files can be too large to fit in memory if the number of subscribers is large; Cider uses [pyspark](https://spark.apache.org/docs/latest/api/python/) to manage large datasets. Another option for working with large datasets is [dask](https://www.dask.org/).

# In[32]:


import pandas as pd
path_to_all_features = datastore.cfg.path.working.directory_path / 'featurizer' / 'datasets' / 'features.csv'
pd.read_csv(path_to_all_features).head()


# Plot the distributions of some of the features.

# In[51]:


featurizer.feature_plots()


# In[ ]:




