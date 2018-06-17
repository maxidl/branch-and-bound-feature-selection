# Branch-and-Bound-Feature-Selection-Python
Implementation of Feature Selection using Branch and Bound (Backward Elimination)

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
test_data.columns = ['exampleInts', 'exampleStrings', 'exampleInts',
                     'exampleInts', 'exampleInts', 'class']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
test_data['exampleStrings'] = le.fit_transform(test_data['exampleStrings'])

X = test_data.values[:,:-1]
y = test_data.values[:, -1:].ravel()
bab = BranchAndBound(X, y)     
best_features = bab.best_subspace(1)
print(best_features)
```
