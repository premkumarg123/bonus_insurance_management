import pandas as pd

# Load CSVs
insurance = pd.read_csv('Data Files/Insurance.csv')
claims = pd.read_csv('Data Files/Claims.csv')
payments = pd.read_csv('Data Files/Payments.csv')

# Check foreign key relationships
missing_policies_in_claims = claims[~claims['policy_id'].isin(insurance['policy_id'])]
missing_policies_in_payments = payments[~payments['policy_id'].isin(insurance['policy_id'])]

print("Missing policies in Claims:")
print(missing_policies_in_claims)

print("Missing policies in Payments:")
print(missing_policies_in_payments)
