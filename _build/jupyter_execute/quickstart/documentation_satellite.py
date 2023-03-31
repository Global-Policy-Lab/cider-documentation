#!/usr/bin/env python
# coding: utf-8

# # Satellite

# In[1]:


from cider.datastore import DataStore
from cider.satellite import Satellite


# We first load some datasets - whose paths have been specified in the config file - using the datastore. The satellite module will by default try to load antenna/tower coordinates, shapefiles defining (administrative) boundaries, the Relative Wealth Index for the country of interest, and population density raster data.

# In[3]:


# This path should point to your cider installation, where configs and data for this demo are located.
from pathlib import Path
cider_installation_directory = Path('../../cider')

datastore = DataStore(config_file_path_string= cider_installation_directory / 'configs' / 'config_quickstart.yml')
satellite = Satellite(datastore=datastore)


# The module can aggregate the RWI - which provides an asset index measure at a resolution of 2.4km x 2.4km - at one of the geographic levels provided by the antennas/towers, in which case their voronoi tessellation will be used - or one of the loaded shapefiles. <br><br>
# In this case, we have loaded (synthetic) data for the country of Togo, and for aggregations at the tower level we will run:

# In[8]:


satellite.aggregate_scores(dataset='rwi', geo='tower_id')


# while for cantons, admin level 3 in Togo, we will run:

# In[5]:


satellite.aggregate_scores(dataset='rwi', geo='cantons')


# The table is also saved as a geojson, storing the identifier of each region, its score - in this case its Relative Wealth Index - its population, and its geometry.

# In[7]:


import geopandas as gpd
gpd.read_file('../../cider/outputs/satellite/maps/cantons_rwi.geojson').head()

