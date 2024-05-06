import pandas as pd

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unik = data['whoAmI'].unique()
for new in unik:
    data[new] = (data['whoAmI'] == new).astype(int)
data.drop(columns=['whoAmI'], inplace=True)
data.head()