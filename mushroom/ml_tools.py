from math import log
import numpy as np

def entropy(labels):
    """ computes entropy of label distribution """
    n_labels = len(labels)
    if n_labels <= 1:
        return 0
    counts = np.bincount(labels).astype(float)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)
    
    print "counts: %s \nprobs: %s \nn_classes: %s" % (counts, probs, n_classes)
    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute standard entropy.
    for i in probs:
        ent -= i * log(i, n_classes)
    return ent
    
ex1 = [1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1]
ex2 = [1,1,1,1,1]
ex3 = [0,0,0,0,0]

print entropy(ex1)
print entropy(ex2)
print entropy(ex3)
