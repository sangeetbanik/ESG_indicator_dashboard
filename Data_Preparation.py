-- Importing all neccessary libraries
#importing necessery libraries
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import seaborn as sns  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

print("import successul")

-- load the dataset
df = pd.read_csv(r"C:\Users\Pratik Banik\Downloads\UM_Projects\Project_1\new\ESGData.csv")
df.head()

-- Renaming the columns and replace the null values with 0, for ease in SQL operations 
df.fillna(0,inplace= True)
df.columns = ['country_name', 'country_code','description','series_code','yr_1960','yr_1961','yr_1962','yr_1963','yr_1964', 'yr_1965','yr_1966','yr_1967','yr_1968','yr_1969','yr_1970','yr_1971','yr_1972', 'yr_1973','yr_1974','yr_1975','yr_1976','yr_1977','yr_1978','yr_1979', 'yr_1980', 'yr_1981','yr_1982', 'yr_1983','yr_1984', 'yr_1985','yr_1986', 'yr_1987','yr_1988', 'yr_1989', 'yr_1990','yr_1991','yr_1992','yr_1993','yr_1994','yr_1995','yr_1996','yr_1997','yr_1998','yr_1999', 'yr_2000', 'yr_2001','yr_2002','yr_2003','yr_2004','yr_2005','yr_2006','yr_2007','yr_2008','yr_2009', 'yr_2010', 'yr_2011','yr_2012','yr_2013','yr_2014','yr_2015','yr_2016','yr_2017','yr_2018','yr_2019','yr_2020','yr_2050' ,'Unnamed: 66' ]
df.head()

-- load the SQL pocessed data
df_filtered = pd.read_csv(r"C:\Users\Pratik Banik\Downloads\UM_Projects\Project_1\new\SQL_filtered_data.csv")
df_filtered.head()


-- Drop the unwanted year columns
list = ['yr_1960','yr_1961','yr_1962','yr_1963','yr_1964', 'yr_1965','yr_1966','yr_1967','yr_1968','yr_1969','yr_1970','yr_1971','yr_1972', 'yr_1973','yr_1974','yr_1975','yr_1976','yr_1977','yr_1978','yr_1979', 'yr_1980', 'yr_1981','yr_1982', 'yr_1983','yr_1984', 'yr_1985','yr_1986', 'yr_1987','yr_1988', 'yr_1989','yr_2050' ,'Unnamed: 66']
new_df_filtered = df_filtered.drop(list,axis=1)
new_df_filtered.head()

-- Concatenating the indicator measurement values from 1990 to 2020 in a new column
new_df_filtered['yr_1990_to_2020'] = new_df_filtered.iloc[:, 4:].apply(lambda row: ', '.join(row.astype(str)), axis=1)

-- Drop the rest of the year columns
list_u = ['yr_1990','yr_1991', 'yr_1992','yr_1993','yr_1994','yr_1995','yr_1996','yr_1997', 'yr_1998','yr_1999', 'yr_2000', 'yr_2001','yr_2002','yr_2003','yr_2004','yr_2005','yr_2006','yr_2007','yr_2008','yr_2009','yr_2010', 'yr_2011','yr_2012','yr_2013','yr_2014','yr_2015','yr_2016','yr_2017','yr_2018','yr_2019','yr_2020']
df_exploded_1 = new_df_filtered.drop(list_u, axis=1)
df_exploded_1.head()

-- Explode the "yr_1990_to_2020" column
df_exploded = df_exploded_1.copy()
df_exploded['yr_1990_to_2020'] = df_exploded['yr_1990_to_2020'].str.split(', ').apply(lambda x: [yr_1990_to_2020.strip() for yr_1990_to_2020 in x])
df_exploded = df_exploded.explode('yr_1990_to_2020')
df_exploded

-- Save the new exploded dataset
df_exploded.to_csv("exploded.csv" , index=False)
