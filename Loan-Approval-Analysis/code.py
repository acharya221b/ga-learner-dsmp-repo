# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var)
# code starts here






# code ends here


# --------------
# code starts here
banks=bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
print(type(bank_mode))
print(bank_mode)
banks.fillna(bank_mode, inplace=True)

print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here





loan_approved_se=len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
loan_approved_nse=len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
percentage_se=loan_approved_se*100/614
percentage_nse=loan_approved_nse*100/614
# code ends here


# --------------
# code starts here
loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=len(banks[loan_term>=25])
print(big_loan_term)
print(banks[loan_term>=25])



# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()




# code ends here


