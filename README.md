# Branch-and-Bound-Feature-Selection-Python
Implementation of Feature Selection using Branch and Bound (Backward Elimination)

        Finding the indices of the k best dimensions using the backward
        elimination approach "Branch and Bound". (Narendra and Fukunaga, 1977)
        It is guaranteed to find the optimal feature subset under the monoticity
        assumption.
        The subspace quality measure used is Subspace Inconsistency:
            Idea:   A Subspace has an inconsistent labeling if identical vectors
                    in the subspace have different class labels
                    
            + efficient search for optimal solutions due to monotonicity
            + well suited for discrete data
            
            - useless for real-valued vectors
            - worst case runtime is still exponential in the number of features


## Install via pip:
```
pip install branch-and-bound-feature-selection
```


## Example
```python
from branch_and_bound import BranchAndBound
import numpy as np
import pandas as pd
test_data = pd.DataFrame([[1, 'a', 3, 4, 5, 1],
                      [1, 'a', 3, 4, 5, 1],
                      [1, 'a', 3, 4, 6, 0],
                      [2, 'c', 3, 4, 6, 0],
                      [2, 'a', 3, 4, 6, 0],
                      [1, 'a', 4, 3, 5, 1]])
test_data.columns = ['exampleInts', 'exampleStrings', 'exampleInts2',
                     'exampleInts3', 'exampleInts4', 'class']
                     
#NOTE: an integer represents a label of a categorical variable

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
test_data['exampleStrings'] = le.fit_transform(test_data['exampleStrings'])

X = test_data.values[:,:-1]
y = test_data.values[:, -1:].ravel()
bab = BranchAndBound(X, y)     
best_features = bab.best_subspace(1)
print(best_features)
```
