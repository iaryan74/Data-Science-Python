import numpy as np
from scipy import stats
data=[12.1, 13.4, 13.8, 14.0, 13.9, 13.3, 12.9, 13.7, 13.5, 14.1]
statistic, p_value = stats.shapiro(data)
print("Shapiro-Wilk test statistic:", statistic)
print("p-value:", p_value)
alpha = 0.05
if p_value < alpha:
    print("The data looks Gaussian (normal distsribution) -fail to reject HO")
else:   
    print("The data does not look Gaussian (normal distsribution) -reject HO")
