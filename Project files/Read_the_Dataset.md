# Read the Dataset

## Epic 2: Data Collection and Analysis

## Overview

After downloading the **Crop_recommendation.csv** dataset, it is loaded
into the OptiCrop system using the **Pandas** library. Reading the
dataset is an essential step before preprocessing, visualization, and
machine learning model development.

------------------------------------------------------------------------

## Loading the Dataset

The dataset is imported using the `read_csv()` function.

``` python
import pandas as pd

data = pd.read_csv("dataset/Crop_recommendation.csv")
```

To verify that the dataset has been loaded correctly, the first five
records are displayed:

``` python
data.head()
```

------------------------------------------------------------------------

## Dataset Features

The dataset contains the following columns:

  Column        Description
  ------------- ------------------------------------
  N             Nitrogen content
  P             Phosphorous content
  K             Potassium content
  temperature   Average temperature
  humidity      Relative humidity
  ph            Soil pH value
  rainfall      Rainfall
  label         Recommended crop (target variable)

------------------------------------------------------------------------

## Purpose

Reading the dataset allows the project to:

-   Verify that the data is loaded correctly.
-   Understand the dataset structure.
-   Inspect feature names and target labels.
-   Prepare the data for preprocessing and analysis.
-   Enable machine learning model training.

------------------------------------------------------------------------

## Expected Output

Using `data.head()` displays the first five rows of the dataset,
providing a quick overview of the agricultural records and confirming
successful data loading.

------------------------------------------------------------------------

## Conclusion

Successfully reading the dataset is the foundation for the OptiCrop
workflow. It ensures that agricultural data is available for
preprocessing, visualization, feature analysis, and machine
learning-based crop recommendation.
