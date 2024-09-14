import pandas as pd

test, train = pd.read_csv("TEST_DF.csv"), pd.read_csv("TRAIN_DF.csv")

big = pd.concat([test, train])

sample = big.groupby('pose').sample(n=280, random_state=42)
df_250 = sample.groupby('pose').head(250)
sample.drop(df_250.index)
df_30 = sample.groupby('pose').head(30)
df_250.to_csv("TRAIN_DF_SAMPLE.csv", index=False)
df_30.to_csv("TEST_DF_SAMPLE.csv", index=False)