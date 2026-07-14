# Importing the Libraries

## Epic 2: Data Collection and Analysis

## Overview

The OptiCrop project requires several Python libraries to perform data
preprocessing, exploratory data analysis, visualization, machine
learning model development, and model evaluation. These libraries
provide efficient tools for handling agricultural datasets and
generating accurate crop recommendations.

------------------------------------------------------------------------

## Imported Libraries

### Pandas (`pandas`)

Used for loading, cleaning, manipulating, and analyzing the agricultural
dataset.

### NumPy (`numpy`)

Provides numerical computing functions and supports array-based
mathematical operations.

### Matplotlib (`matplotlib.pyplot`)

Used to create charts and plots for visualizing agricultural data.

### Seaborn (`seaborn`)

Built on Matplotlib and used for attractive statistical visualizations.

### Scikit-learn (`sklearn`)

Provides machine learning algorithms and utilities including:

-   KMeans Clustering
-   Logistic Regression
-   Train-Test Split
-   Confusion Matrix
-   Classification Report

### IPython & ipywidgets

Used to enhance the interactive notebook environment during data
exploration.

------------------------------------------------------------------------

## Imported Modules

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
```

------------------------------------------------------------------------

## Visualization Style

The project uses the **FiveThirtyEight (`fivethirtyeight`)**
visualization style to produce clean and professional graphs for
agricultural data analysis.

------------------------------------------------------------------------

## Purpose of the Libraries

  Library        Purpose
  -------------- ---------------------------------------
  Pandas         Dataset loading and manipulation
  NumPy          Numerical computations
  Matplotlib     Data visualization
  Seaborn        Statistical plotting
  Scikit-learn   Machine learning and model evaluation
  IPython        Interactive notebook support
  ipywidgets     Interactive controls

------------------------------------------------------------------------

## Outcome

After importing the required libraries, the project environment is ready
for data exploration, preprocessing, visualization, model training, and
evaluation. These tools form the foundation of the OptiCrop machine
learning workflow.

------------------------------------------------------------------------

## Conclusion

The selected Python libraries provide a complete ecosystem for
developing the OptiCrop application. They simplify data analysis,
improve model development, and support effective visualization, enabling
accurate and reliable crop recommendation.
