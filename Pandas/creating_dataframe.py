# creating dataframe
# read_csv(), read_json(), read_excel()
# using dictionary
# using tuple of values

import pandas as pd

d = pd.read_csv("C:\\Users\\Pradeep Rangisetti\\Downloads\\diabetes.csv")
df = pd.DataFrame(d)
print(df)