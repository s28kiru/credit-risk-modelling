# CREDIT RISK MODELLING

## Dataset

UCI repository data: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients

- Credit risk modelling is to understand the credit worthiness of the burrower and check how likely the burrower is going to default a loan

### Exploratory data analysis

- `ID` - set as index
- `LIMIT_BAL` - Amount of given credit in NT dollars (includes individual and family/supplementary credit) - not normal but no possible outliers
- `SEX` - Gender (1 = male, 2 = female) - more female burrowers
- `EDUCATION` -  (1 = graduate school, 2 = university, 3 = high school, 0,4,5,6 = others)
- `MARRIAGE` -  Marital status (0 = others, 1 = married, 2 = single, 3 = divorce)
- `AGE` -  Age in years
- `PAY_0` - Repayment status in September, 2005
(-2 = No consumption, -1 = paid in full, 0 = use of revolving credit (paid minimum only), 1 = payment delay for one month, 2 = payment delay for two months, ... 8 = payment delay for eight months, 9 = payment delay for nine months and above)
- `PAY_2` - Repayment status in August, 2005 (scale same as above)
- `PAY_3` - Repayment status in July, 2005 (scale same as above)
- `PAY_4` - Repayment status in June, 2005 (scale same as above)
- `PAY_5` - Repayment status in May, 2005 (scale same as above)
- `PAY_6` - Repayment status in April, 2005 (scale same as above)
- `BILL_AMT1` -  Amount of bill statement in September, 2005 (NT dollar)
- `BILL_AMT2` -  Amount of bill statement in August, 2005 (NT dollar)
- `BILL_AMT3` -  Amount of bill statement in July, 2005 (NT dollar)
- `BILL_AMT4` -  Amount of bill statement in June, 2005 (NT dollar)
- `BILL_AMT5` -  Amount of bill statement in May, 2005 (NT dollar)
- `BILL_AMT6` -  Amount of bill statement in April, 2005 (NT dollar)
- `PAY_AMT1` -  Amount of previous payment in September, 2005 (NT dollar)
- `PAY_AMT2` - Amount of previous payment in August, 2005 (NT dollar)
- `PAY_AMT3` -  Amount of previous payment in July, 2005 (NT dollar)
- `PAY_AMT4` - Amount of previous payment in June, 2005 (NT dollar)
- `PAY_AMT5` - Amount of previous payment in May, 2005 (NT dollar)
- `PAY_AMT6` -  Amount of previous payment in April, 2005 (NT dollar)
- `default.payment.next.month` -  Default payment (1=yes, 0=no)

### Baseline model

- numerical variables - LIMIT_BAL, AGE
- categorical variables - SEX, EDUCATION, MARRIAGE, PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
