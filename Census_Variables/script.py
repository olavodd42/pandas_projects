import codecademylib3

# Import pandas with alias
import pandas as pd
import numpy as np

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())
print(census.dtypes)
print(census.birth_year.unique())
census.birth_year.replace('missing', '1967', inplace=True)
print(census.birth_year.unique())

census.birth_year = census.birth_year.astype('int')
print(census.dtypes)

print(census.birth_year.mean())

census.higher_tax = pd.Categorical(census.higher_tax, ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

print(census.higher_tax.unique())

encoded_higher_tax = census.higher_tax.cat.codes
print(encoded_higher_tax.median())

census['marital_codes'] = census['marital_status'].astype('category').cat.codes
census = pd.get_dummies(data=census, columns=['marital_status'])
print(census.head())

census['age'] = 2025 - census['birth_year']
max_age = census.age.max()
min_age = census.age.min()
bins = np.arange(min_age // 5 * 5, max_age // 5 * 5 + 5, 5)

# ... existing code ...

# Create age groups in 5-year increments
census['age_group'] = pd.cut(
    census['age'],
    bins=bins,
    right=False,  # Left-closed interval [start, end)
    include_lowest=True
)


print(census.head())

age_group = census.groupby('age_group').size().reset_index()
print(age_group)
age_group['age_group'] = pd.Categorical(age_group['age_group'],
['[15, 20)', '[20, 25)', '[25, 30)', '[30, 35)', '[35, 40)', '[40, 45)', '[45, 50)', '[50, 55)', '[55, 60)', '[60, 65)', '[65, 70)', '[70, 75)', '[75, 80)', '[80, 85)'], ordered=True)
age_group_encoded = age_group['age_group'].cat.codes
print(age_group_encoded)