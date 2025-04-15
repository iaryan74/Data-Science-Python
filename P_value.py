import math
from scipy.stats import norm

#Sample Data
sample_mean=169.5
population_mean=168
population_std_dev= 3.9
sample_size= 36
alpha=0.05
tail='two'
#standard error
standard_error= population_std_dev/ math.sqrt(sample_size)
#Z-score
z_score=(sample_mean- population_mean)/ standard_error

#p-value based on the type of test
if tail =='two':
    p_value = 2*(1-norm.cdf(abs(z_score)))
elif tail=='left':
    p_value == norm.cdf(z_score)
elif tail =='right':
    p_value == 1 - norm.cdf(z_score)
else:
    raise ValueError("tail must be 'two', 'left', or 'right'" )
#output

if p_value < alpha:
    conclusion = "Reject null hypothesis"
    