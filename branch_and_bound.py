# -*- coding: utf-8 -*-
import numpy as np
import itertools
from sklearn.utils import check_X_y

class BranchAndBound:
    def __init__(self, X, y):
        """
        Class to find the indices of the k best dimensions using the backward
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
                
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Dataset vectors, where n_samples is the number of samples
            and n_features is the number of features
            
        y : array-like, shape (n_samples,)
            Target values.
        """
        X, y = check_X_y(X, y, accept_sparse=False)
        self.X = X
        self.y = y
        self.class_values = np.unique(y)
    
    def __num_of_identical(self, row, columns):
        return (self.X[:,columns] == row).all(axis=1).sum()
    
    def __num_of_identical_given_class(self, row, columns, class_value):
        return ((self.X[:,columns] == row).all(axis=1) & (self.y == class_value).T).sum()
    
    def __inconsistency_of_row(self, row, columns):
        return self.__num_of_identical(row, columns) - max([self.__num_of_identical_given_class(row, columns, c) for c in self.class_values])
    
    def __inconsistency_of_subspace(self, columns):
        return np.mean([self.__inconsistency_of_row(row, columns) for row in self.X[:,columns]])
    
    def __get_subspaces(self, space):
        return np.array(list(itertools.combinations(space, len(space)-1)))
    
    def best_subspace(self, target_dim):
        """
        Perform the feature selection for a given the target dimension
        
        Parameters
        ----------
        target_dim : int
            The targeted number of output dimensions (features)
        
        Returns
        -------
        X_subset_indices : array, shape (target_dim,)
            The indices of the best subspace given the target dimension
        """
        stack = []
        init_dim = np.array(range(self.X.shape[1]))
        stack.append((init_dim, self.__inconsistency_of_subspace(init_dim)))
        curr_bound = float('inf')
        while stack:
            curr_node = stack.pop()
            if curr_bound > curr_node[1]:
                children = []
                for subspace in self.__get_subspaces(curr_node[0]):
                    inconsistency = self.__inconsistency_of_subspace(subspace)
                    if len(subspace) == target_dim:
                        if inconsistency < curr_bound:
                            curr_bound = inconsistency
                            curr_best_subspace = subspace
                    children.append((subspace, inconsistency))
                if len(curr_node[0]) != target_dim + 1:
                    children = sorted(children, key=lambda x: x[1])
                    children.reverse() #push lowest inconsistency last
                    stack.extend(children)
        return curr_best_subspace
        
        
"""
test_data = np.array([[1, 2, 3, 4, 5, 1],
                      [1, 2, 3, 4, 5, 1],
                      [1, 2, 3, 4, 6, 0],
                      [2, 1, 3, 4, 6, 0],
                      [2, 2, 3, 4, 6, 0],
                      [1, 2, 4, 3, 5, 1]])
X = test_data[:,:-1]
y = test_data[:, -1:]   
bab = BranchAndBound(X, y)     
best_features = bab.best_subspace(1)
"""