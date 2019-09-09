# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
print(df.head(10))
p_a=len(df[df['fico']>700])/len(df)
p_b=len(df[df['purpose']=='debt_consolidation'])/len(df)
df1=df[df['purpose']=='debt_consolidation']
print(df1)
p_a_b=len(df1[df1['fico']>700])/len(df1)
if p_a_b==p_a:
    result=True
else:
    result=False
print(result)    
# code ends here


# --------------
# code starts here
prob_lp=len(df[df['paid.back.loan']=='Yes'])/len(df)
prob_cs=len(df[df['credit.policy']=='Yes'])/len(df)
new_df=df[df['paid.back.loan'] == 'Yes']
prob_pd_cs=len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)
bayes=prob_pd_cs*prob_lp/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
#print(df['purpose'].value_counts())
plt.bar(df['purpose'].value_counts(),height='10') 
df1=df[df['paid.back.loan'] == 'No']


# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
plt.hist(df['installment'],bins=10)
plt.hist(df['log.annual.inc'],bins=10)

# code ends here


