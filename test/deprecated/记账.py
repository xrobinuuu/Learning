# import copy
# from functools import reduce
# import pandas as pd
# import numpy as np
# from scipy.stats import pearsonr
#
# con = {
#     'name': ['xm', 'xh', 'xz', 'xx'],
#     'sex': ['woman', 'male', 'woman', 'male'],
#     'english': [20, 10, 17, 31],
#     'math': [44, 33, 22, 11],
# }
#
# df = pd.DataFrame(data=con)
#
#
# # da = ['xa', 'woman', 20, 55]
# # df.loc[4] = da
# # df.iloc[2:5], df.iloc[1] = df.iloc[1:4], df.iloc[4]
# # df = df.groupby('sex').agg(english_mean=('english', 'mean'), math_var=('math', 'var')).reset_index()
# # df = df.groupby('sex')['english'].agg(mean='mean', var='var').reset_index()
# df = df.groupby('sex')['english', 'math'].apply
#
#
#
# print(df, type(df))

x = 2 ** (4 * 8)
print(x / 2 / 60 / 60 / 24 / 365)


