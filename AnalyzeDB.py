import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv("Data/all_engineers.csv", encoding="utf-8")
    # df.Links = "https://www.oea.org.lb/Arabic/"+df.Links
    # df.to_csv("Data/all_engineers.csv", index=False)
# Useful
# https://intellipaat.com/community/32844/insert-a-link-inside-a-pandas-table
# from IPython.display import HTML
# df['Links'] = df['Links'].apply(lambda x: '<a href="{0}">Details</a>'.format(x))
# HTML(df.to_html(escape=False))

# df.groupby(["Field",'SubField'])["Engineer_ID"].mean().nsmallest(10)


# df.groupby("Field")["Engineer_ID"].mean().nlargest(10)

# df.groupby("Field")["Engineer_ID"].median().nlargest(10)

# results=df.groupby("Field").agg({'Engineer_ID': ['min','median', 'max']})
# results.sort_values([('Engineer_ID', 'median')], ascending=False)


# To Drop a column
# df.drop(columns=['Links'],inplace=True)
# df.to_csv("Data/All_engineers_reduced.csv",index=False)
