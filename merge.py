import pandas as pd


sic6l = pd.read_csv("C6L.SI.csv")
print(sic6l)
hk0293 = pd.read_csv("0293.HK.csv")
result = sic6l.join(hk0293,how='inner',rsuffix='_hk')

print(result['Close'].pct_change())

result = pd.concat((result, result['Close'].pct_change().rename('pct_change')), axis=1)
result = pd.concat((result, result['Close_hk'].pct_change().rename('pct_change_hk')), axis=1)
result.to_csv("merge.csv",index=False)
