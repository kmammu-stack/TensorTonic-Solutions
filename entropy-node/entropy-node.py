import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    values, counts = np.unique(y, return_counts=True)
    print("Counts:", counts)       

    prob = counts / counts.sum()
    
    probs = np.array(prob)
    return np.abs(-np.sum(probs * np.log2(probs + 1e-9))) 

