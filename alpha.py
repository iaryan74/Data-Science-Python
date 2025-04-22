from statsmodels.stats.proportion import proportions_ztest
from scipy import stats

#Group 1: 50 conversion out of 200 visits
#Group 2: 65 conversion out of 200 visits

conv_rate =[50,65]
samples =[200,200]
z_stat, p_value = proportions_ztest(conv_rate, samples) 
alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")