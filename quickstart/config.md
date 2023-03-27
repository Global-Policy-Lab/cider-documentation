
# Configuration file

The configuration file - example at `configs/config.yml` - is used to store all relevant configurations, like paths to the datasets and spark parameters. It should be appropriately edited before executing the code. It is written in [YAML](https://yaml.org/).<br>

## Spark parameters
Spark parameters are set under the `spark` heading. Syntax for specifying Spark parameters derives from [Spark\'s own property names](https://spark.apache.org/docs/latest/configuration.html#available-properties). For example, to conigure the parameter `spark.app.name` in Cider config, we'd use
```
spark:
  app:
    name: "my_first_cider_app"
```

Here is a more complete example config. It's not meant as an endorsement of these specific config values; optimal choices vary greatly based on your environment and use case. 

```
spark:
  app:
    name: "my_first_cider_app"
  master: "local[*]"
  sql:
    shuffle:
      partitions: 144
  driver:
    memory: "8G"
    maxResultSize: "2G"
    supervise: true
  executor:
    memory: "8G"
  rpc:
    askTimeout: "600s"
  loglevel: "WARN"
  logConf: true
```

## File and folder locations

Under the `path` heading, we specify folder and file locations. File subpaths are given relative to a "parent" directory: Either the `input_data` directory or the `working` directory (if you'd rather specify an absolute path, use a leading slash). The locations of the parent directories must be specified with absolute paths (with leading slashes). Cider will not modify files under the `input_data` directory. It will use the `working` directory for program outputs, some of which may act as inputs for later steps. For example, the featurizer writes features to the `working` directory, and then the ml module reads features back in (from that same directory, unless a different one is specified as input). At present, file names/sub-paths written programmatically under the `working` directory are hard-coded and can't be specified in config.

```
path:
  input_data: 
    directory_path: "/Users/example/Documents/GD/cider/synthetic_data/"
    file_paths:
      antennas: "antennas.csv"
      cdr: "cdr.csv"
      home_ground_truth: "home_locations.csv"
      labels: "labels.csv"
      mobiledata: "mobiledata.csv"
      mobilemoney: "mobilemoney.csv"
      population: "population_tgo_2019-07-01.tif"
      poverty_scores: null
      recharges: "recharges.csv"
      rwi: "TGO_relative_wealth_index.csv"
      shapefiles:
        regions: "regions.geojson"
        cantons: "cantons.geojson"
        prefectures: "prefectures.geojson"
      user_consent: null
  working: 
    directory_path: "/Users/example/Documents/GD/cider/working_directory/"
```

## Column names

Cider expects certain columns to be present, and we can specify their names under the `col_names` heading (this is not a complete list):

```
col_names:
  cdr:
    txn_type: "txn_type"
    caller_id: "caller_id"
    recipient_id: "recipient_id"
    timestamp: "timestamp"
    duration: "duration"
    caller_antenna: "caller_antenna"
    recipient_antenna: "recipient_antenna"
    international: "international"
  antennas:
    antenna_id: "antenna_id"
    tower_id: "tower_id"
    latitude: "latitude"
    longitude: "longitude"
  recharges:
    caller_id: "caller_id"
    amount: "amount"
    timestamp: "timestamp"
  mobiledata:
    caller_id: "caller_id"
    volume: "volume"
    timestamp: "timestamp"
  mobilemoney:
    txn_type: "txn_type"
    caller_id: "caller_id"
    recipient_id: "recipient_id"
    timestamp: "timestamp"
    amount: "amount"
    sender_balance_before: "sender_balance_before"
    sender_balance_after: "sender_balance_after"
    recipient_balance_before: "recipient_balance_before"
    recipient_balance_after: "recipient_balance_after"
  geo: "tower_id"
```

## Miscellaneous parameters

We also have to set a few parameters that will affect the behaviour of some modules, under the `params` heading:

```
params:
  cdr:
    weekend: [1, 7] // definition of weekend (Sun = 1 to Sat = 7)
    start_of_day: 7 // hour when day starts (used to define day/night)
    end_of_day: 19 // hour when night starts (used to define day/night)
  home_location:
    filter_hours: null // hours to filter out when inferring home locations
  automl: // params used by the autoML libraries
    autosklearn:
      time_left: 3600
      n_jobs: 1
      memory_limit: 3072
    autogluon:
      time_limit: 3600
      eval_metric: "r2"
      label: "label"
      sample_weight: "weight"
  opt_in_default: false // if true opt-in is set as default, i.e. all users give their consent unless they opt-out
```

## ML tuning parameters

Under the `hyperparams` heading, we set the hyper-parameters that will be tested during a grid-search performed by the ML module:

```
hyperparams:
  "linear":
    "dropmissing__threshold": [0.9, 1]
    "droplowvariance__threshold": [ 0, 0.01 ]
    "winsorizer__limits": [!!python/tuple [0., 1.], !!python/tuple [0.005, .995]]
  "lasso":
    "dropmissing__threshold": [ 0.9, 1 ]
    "droplowvariance__threshold": [ 0, 0.01 ]
    "winsorizer__limits": [!!python/tuple [0., 1.], !!python/tuple [0.005, .995]]
    "model__alpha": [ .001, .01, .05, .03, .1 ]
  "ridge":
    "dropmissing__threshold": [ 0.9, 1 ]
    "droplowvariance__threshold": [ 0, 0.01 ]
    "winsorizer__limits": [!!python/tuple [0., 1.], !!python/tuple [0.005, .995]]
    "model__alpha": [ .001, .01, .05, .03, .1 ]
  "randomforest":
    "dropmissing__threshold": [ 0.9, 1 ]
    "droplowvariance__threshold": [ 0, 0.01 ]
    "winsorizer__limits": [!!python/tuple [0., 1.], !!python/tuple [0.005, .995]]
    "model__max_depth": [ 2, 4, 6, 8, 10 ]
    "model__n_estimators": [ 50, 100, 200 ]
  "gradientboosting":
    "dropmissing__threshold": [ 0.99 ]
    "droplowvariance__threshold": [ 0.01 ]
    "winsorizer__limits": [!!python/tuple [0., 1.], !!python/tuple [0.005, .995]]
    "model__min_data_in_leaf": [ 10, 20, 50 ]
    "model__num_leaves": [ 5, 10, 20 ]
    "model__learning_rate": [ 0.05, 0.075, 0.1 ]
    "model__n_estimators": [ 50, 100, 200 ]
```
