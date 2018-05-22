######### Python Code block extracted from non_equi_joins.Rmd ##############

import numpy as np
import pandas as pd
import feather



############# Python Code block extracted from non_equi_joins.Rmd ##############

# A data set with interesting cases identified by id numbers
df_cases       = feather.read_dataframe("data/df_cases.feather")
# Background data from a data base that we want to add to the cases
df_op          = feather.read_dataframe("data/df_op.feather")
df_prom_before = feather.read_dataframe("data/df_prom_before.feather")
df_prom_after  = feather.read_dataframe("data/df_prom_after.feather")



############# Python Code block extracted from non_equi_joins.Rmd ##############

for n in df_cases.columns.values:
  print(n)



############# Python Code block extracted from non_equi_joins.Rmd ##############

def relevant_columns(x):
    """
    Function to find columns names from x also found in 'df_cases' 
    """
    return np.intersect1d(df_cases.columns.values, x.columns.values)
# Relevant columns from each background data set
cols_in_df_op          = relevant_columns(df_op)
cols_in_df_prom_before = relevant_columns(df_prom_before)
cols_in_df_prom_after  = relevant_columns(df_prom_after)
# Find which columns in df_cases can be found only in this data set
cols_in_df_cases = (
    np.concatenate([['fake_id'],
        np.setdiff1d(
            df_cases.columns.values,
            np.concatenate([
                df_op.columns.values,
                df_prom_before.columns.values,
                df_prom_after.columns.values
            ])
        )
    ])
)



############# Python Code block extracted from non_equi_joins.Rmd ##############

print([len(x) for x in [
  cols_in_df_op, cols_in_df_prom_before, cols_in_df_prom_after, cols_in_df_cases]
])



############# Python Code block extracted from non_equi_joins.Rmd ##############

df_cases       = df_cases[cols_in_df_cases]
df_op          = df_op[cols_in_df_op]
df_prom_before = df_prom_before[cols_in_df_prom_before]
df_prom_after  = df_prom_after[cols_in_df_prom_after]



############# Python Code block extracted from non_equi_joins.Rmd ##############

df_op['P_SurgDate']         = pd.to_datetime(df_op['P_SurgDate'])
df_prom_before['PREP_Date'] = pd.to_datetime(df_prom_before['PREP_Date'])
df_prom_after['POSTP_Date'] = pd.to_datetime(df_prom_after['POSTP_Date'])



############# Python Code block extracted from non_equi_joins.Rmd ##############

df_prom_before = (
    df_prom_before.assign(
        # The lower bound is actually just "PREP_Date" itself but we prepare the
        # code if we would like to modify this later
        PREP_Date_min = lambda x: x.PREP_Date - pd.to_timedelta(0  , unit = 'd'),
        PREP_Date_max = lambda x: x.PREP_Date + pd.to_timedelta(180, unit = 'd')
    )
)
df_prom_after = (
    df_prom_after.assign(
        POSTP_Date_min = lambda x: x.POSTP_Date - pd.to_timedelta(365 - 180, unit = 'd'),
        POSTP_Date_max = lambda x: x.POSTP_Date - pd.to_timedelta(356 + 180, unit = 'd')
    )
)



############# Python Code block extracted from non_equi_joins.Rmd ##############

df = df_cases
def print_dims():
    print("Rows and columns of df:", end = " ")
    for d in df.shape:
        print(d, end = " ")
print_dims()



############# Python Code block extracted from non_equi_joins.Rmd ##############

df = pd.merge(df_cases, df_op, how = 'left')
print_dims()



############# Python Code block extracted from non_equi_joins.Rmd ##############

print(df.head())



############# Python Code block extracted from non_equi_joins.Rmd ##############

df_tmp = (
    pd.merge(df, df_prom_before)
    .query('PREP_Date_min <= P_SurgDate <= PREP_Date_max')
    .drop_duplicates()
)



############# Python Code block extracted from non_equi_joins.Rmd ##############

print(df_tmp.loc[:, ['fake_id', 'P_SurgDate', 'PREP_Date_min', 'PREP_Date_max']])



############# Python Code block extracted from non_equi_joins.Rmd ##############

df = pd.merge(df, df_tmp, "left")
print_dims()



############# Python Code block extracted from non_equi_joins.Rmd ##############

print(df.loc[:, ['fake_id', 'HipRegStartHere', 'P_SurgDate', 'PREP_Date']].count())
