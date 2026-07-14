# Univariate Analysis

## Epic 2: Data Collection and Analysis

## Overview

Univariate Analysis is performed to examine each feature in the
agricultural dataset individually. It helps understand the distribution,
central tendency, spread, and overall characteristics of variables
before building machine learning models.

------------------------------------------------------------------------

## Objective

The primary objective of univariate analysis is to study the behavior of
each agricultural parameter independently and identify patterns that may
influence crop recommendation.

------------------------------------------------------------------------

## Features Analyzed

The following features are analyzed:

-   Nitrogen (N)
-   Phosphorous (P)
-   Potassium (K)
-   Temperature
-   Humidity
-   Soil pH
-   Rainfall

------------------------------------------------------------------------

## Visualization Techniques

The following visualization methods are used:

-   Distribution Plot (Distplot / Histogram with KDE)
-   Count Plot (where applicable)

These plots help visualize the frequency distribution and density of
each feature.

------------------------------------------------------------------------

## Sample Python Code

``` python
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("fivethirtyeight")

features = ["N","P","K","temperature","humidity","ph","rainfall"]

for feature in features:
    plt.figure(figsize=(6,4))
    sns.histplot(data[feature], kde=True)
    plt.title(f"Distribution of {feature}")
    plt.show()
```

------------------------------------------------------------------------

## Observations

-   Soil nutrients show varying distributions across the dataset.
-   Temperature and pH values are concentrated within suitable
    agricultural ranges.
-   Humidity and rainfall exhibit wider variation depending on crop
    requirements.
-   The visualizations provide insights into the spread and density of
    each feature.

------------------------------------------------------------------------

## Importance

Univariate analysis helps to:

-   Understand individual feature distributions.
-   Detect unusual values or outliers.
-   Validate data quality.
-   Support feature engineering.
-   Prepare the dataset for machine learning.

------------------------------------------------------------------------

## Conclusion

The univariate analysis provides a clear understanding of each
agricultural parameter and forms the foundation for further bivariate
analysis, multivariate analysis, and crop recommendation model
development.
