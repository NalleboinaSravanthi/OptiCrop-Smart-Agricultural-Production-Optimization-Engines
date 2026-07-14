# Bivariate Analysis

## Epic 2: Data Collection and Analysis

## Overview

Bivariate analysis is performed to study the relationship between two
variables in the agricultural dataset. In the OptiCrop project, the
relationship between **humidity** and **crop labels** is analyzed to
understand how environmental conditions influence crop recommendations.

------------------------------------------------------------------------

## Objective

The objective of this analysis is to identify patterns and relationships
between humidity levels and different crop types, helping improve the
accuracy of the crop recommendation model.

------------------------------------------------------------------------

## Features Analyzed

-   **Humidity** (Independent Variable)
-   **Crop Label** (Target Variable)

------------------------------------------------------------------------

## Visualization Technique

A **Scatter Plot** is used to visualize the relationship between
humidity and crop labels.

### Sample Python Code

``` python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.scatterplot(x=data["humidity"], y=data["label"])

plt.title("Humidity vs Crop Label")
plt.xlabel("Humidity")
plt.ylabel("Crop Label")
plt.show()
```

------------------------------------------------------------------------

## Observations

-   Different crops grow under different humidity conditions.
-   Crops such as Rice, Banana, and Coconut generally require higher
    humidity levels.
-   Crops like Chickpea and Kidney Beans are associated with
    comparatively lower humidity.
-   Some crops share overlapping humidity ranges, indicating that
    humidity should be combined with other environmental parameters for
    accurate prediction.

------------------------------------------------------------------------

## Importance

-   Understand relationships between environmental conditions and crop
    types.
-   Improve feature selection.
-   Support intelligent crop recommendation.
-   Enhance machine learning model performance.

------------------------------------------------------------------------

## Expected Outcome

The scatter plot provides insights into crop-specific humidity
requirements and demonstrates that humidity is an important feature for
crop recommendation.

------------------------------------------------------------------------

## Conclusion

Bivariate analysis helps identify meaningful relationships between
humidity and crop labels, improving feature engineering and supporting
accurate crop prediction in the OptiCrop system.
