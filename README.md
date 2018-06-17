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
test_data = np.array([[1, 2, 3, 4, 5, 1],
                      [1, 2, 3, 4, 5, 1],
                      [1, 2, 3, 4, 6, 0],
                      [2, 1, 3, 4, 6, 0],
                      [2, 2, 3, 4, 6, 0],
                      [1, 2, 4, 3, 5, 1]])
X = test_data[:,:-1]
y = test_data[:, -1:].ravel()
bab = BranchAndBound(X, y)     
best_features = bab.best_subspace(1)
print(best_features)
```
