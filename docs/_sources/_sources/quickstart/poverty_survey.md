# Poverty Outcome Generation from Survey Data
Set up the configuration file and load some survey data (see {doc}`standardized data formats <../data_formats/survey_data>`) for file schema).

```
datastore = DataStore('/path/to/config/file')
outcomes_generator = SurveyOutcomesGenerator(datastore=datastore, clean_folders=True)
```

Calculate PCA asset index and proxy-means test (PMT). Only use binary and continuous columns in the asset index.

```
asset_index = outcomes_generator.asset_index(cols=['con1', 'con2', 'bin1', 'bin2'])
```

Select five components to be used in the proxy-means test using forward selection of predictors with a linear regression. Calculate a proxy-means test with these components and obtain out-of-sample PMT predictions for the training survey. 

```
selected_cols, scores = outcomes_generator\
                        .select_features('consumption',
                                         ['con1', 'con2', 'cat1', 'cat2', 'bin1', 'bin2'], 
                                         5, 
                                         method=LinearRegession())
pmt = outcomes_generator.fit_pmt('consumption', 
                                 selected_cols, 
                                 model_name='linear', 
                                 winsorize=False, 
                                 scale=True)
```

`[OUT] r2 score: 0.56`


Use the trained proxy-means test on another survey dataset. 

```
predictions = outcomes_generator.pretrained_pmt('/path/to/other/data.csv', selected_cols, 'linear')
```