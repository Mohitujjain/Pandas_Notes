#!/usr/bin/env python
# coding: utf-8

# <div style="text-align: center;"><div  style="color:#7f0000; font-size:30px; font-weight:bold; line-height:40px;">Pandas Notes</div></div>
# <div style="text-align: center; color:#006666"><strong>Owner: </strong>Mohit Kumar</div>
# <div style="text-align: center; color:#006666"><strong>Mail ID: </strong>mohitujjain71195@gmail.com</div>
# <div style="text-align: center; color:#006666"><strong>Linkedin ID: </strong>https://www.linkedin.com/in/mohit-kumar-61bb20198/</div>
# <div style="text-align: center; color:#006666"><strong>githublink: </strong><div style="text-align: center; color:#006666"><strong>githublink: </strong>https://github.com/Mohitujjain/</div>   
# 
# 

# What is Pandas?
# Pandas is a Python library used for working with data sets.
# 
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# 
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

# Why Use Pandas?
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# 
# Pandas can clean messy data sets, and make them readable and relevant.
# 
# Relevant data is very important in data science.

# What Can Pandas Do?
# Pandas gives you answers about the data. Like:
# 
# * Is there a correlation between two or more columns?
# * What is average value?
# * Max value?
# * Min value?
# * Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or     NULL values. This is called cleaning the data.

# What is a Series?
# A Pandas Series is like a column in a table.
# 
# It is a one-dimensional array holding data of any type.

# # Pandas
# ###### Pandas module works with the tabular data.
# ###### Pandas has poowerful tools like Series,DataFrame etc.
# ###### Pd is used in popular organizations like Instacart,SendGrid,and Sighten.
# ###### Pd has a better performance for 500k rows or more.
# ###### Pd consume large memory as compared to numpy.
# ###### Pd is mentioned in 73 company stacks and 46 developer stacks.
# ###### Pd provides 2d table object called DataFrame.

# # Exploring Data
# ######  df.head()       ###  first five rows
# ###### df.tail()       ### last five rows
# ###### df.sample(5)    ### random sample of rows
# ###### df.shape        ### number of rows/columns 
# ###### df.describe()   ### calculates measures of central tendency
# ###### df.info()       ### memory footprint and datatypes

# In[ ]:





# # Statistics
# ###### df.describe() # Summary statistics for numerical columns
# ###### df.mean() # Returns the mean of all columns
# ###### df.corr() # Returns the correlation between columns in a DataFrame
# ###### df.count() # Returns the number of non-null values in each DataFrame column
# ###### df.max()  # Returns the highest value in each column
# ###### df.min() # Returns the lowest value in each column
# ###### df.median() # Returns the median of each column
# ###### df.std() # Returns the standard deviation of each column

# # Import Data from Files
#  ## Import csv
# ###### df = pd.read_csv('Data/my-data.csv' ,sep=",") 
# ###### df

# # Import xls
# ###### df = pd.read_excel('Data/my-data.xlsx')
# ###### df = pd.read_excel('Data/my-data.xlsx',
# ######     sheetname='sheet1',
# ######    skiprows=[1] # header data
# )

# # Export Data to files
# #####  Export xls
# ###### df.to_excel('Data/my-data.xlsx')
# # Export csv
# ######  df.to_csv ('Data/my-data.csv' , index = False, header=True) 

# In[1]:


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)


# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# 
# This label can be used to access a specified value.

# In[2]:


print(myvar[0])


# In[3]:


# Create labels 
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


# In[4]:


print(myvar["y"])


# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

# In[5]:


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


# # We are going to learn about 
# ## 1. Pandas Dataframe.
# ## 2.Pandas Series.
# ## 3.Pandas Basic Operations

# In[6]:


import pandas as pd ##KN
import numpy as np


# In[7]:


np.arange(0,20).reshape(5,4)


# In[8]:


## Create Dataframe
df=pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["R1","R2","R3","R4","R5"],columns=["C1","C2","C3","C4"])


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


type(df)


# In[12]:


df.info()


# In[13]:


df.describe()


# ## Index
# ####  Columnname,rowindex[.loc],  rowindex columnindex number [.iloc

# In[14]:


df.head()


# In[15]:


df['C1']


# In[16]:


type(df['C1'])


# In[17]:


df[['C1','C2','C3']]


# In[18]:


type(df[['C1','C2','C3']])


# In[19]:


df.loc['R3']


# In[20]:


type(df.loc['R3'])


# In[21]:


### using  row index name loc
df.loc[['R3','R4']]


# In[22]:


df.head()


# In[23]:


df.iloc[2:4,0:2]


# In[24]:


df.iloc[2:,1:]


# In[25]:


df.iloc[[1,2,3,4],[0, 3]]


# In[26]:


df.iloc[:,[0,3]]


# ## convert dataframe into arrays
# df.iloc[:,1:].values

# In[27]:


df.iloc[:,1:].values


# ##  Basic operations

# In[28]:


df.isnull().sum()


# In[29]:


df1=pd.DataFrame(data=[[1,np.nan,2],[1,3,4]],index=["R1","R2"],columns=["C1","C2","C3"])


# In[30]:


df1


# In[31]:


df1.isnull().sum()


# In[32]:


df1.isnull()


# In[33]:


df1.isnull().sum()==0


# In[34]:


df1['C2'].value_counts()


# In[35]:


df1


# In[36]:


df['C3'].unique()


# In[37]:


df1>2


# ## In this part we are learn about
#   ### 1. StringIO
#   ### 2. Pandas read_csv

# In[38]:


### Reading Different Data sources with the help of pandas
from io import StringIO  #in memory file format object


# In[39]:


import pandas as pd
df=pd.read_csv('mercedesbenz.csv')


# In[40]:


df.head()


# In[41]:


type(df)


# In[42]:


data=('c1,c2,c3\n'
     'x,y,1\n'
     'a,b,2\n'
     'c,d,3')


# In[43]:


type(data)


# In[44]:


## in memory file format object
StringIO(data)


# In[45]:


pd.read_csv(StringIO(data))


# In[46]:


pd.read_csv(StringIO(data),usecols=['c1','c2'])


# In[47]:


import pandas as pd
df=pd.read_csv('mercedesbenz.csv',usecols=['X0','X1','X2','X3','X4','X5'])
df.head()


# In[48]:


##first try with only df.to_csv and go back and check the data next add index=false and again 
##execute the data and check data again u see the index value is not their
df.to_csv('test.csv', index=False)


# In[49]:


## datatypes in csv
data = ('a,b,c,d\n'
       '1,2,3,4\n'
       '5,6,7,8\n'
        '9,10,11'
       )


# In[50]:


df3=pd.read_csv(StringIO(data))


# In[51]:


df3.info()


# In[52]:


df3=pd.read_csv(StringIO(data),dtype='object')


# In[53]:


df3.info()


# In[54]:


df3=pd.read_csv(StringIO(data),dtype='float')


# In[55]:


df3.info()


# In[56]:


df3.head()


# In[57]:


df3.isnull().sum()


# In[58]:


df3['a']


# In[59]:


df3['a'][0]


# In[60]:


## datatypes in csv
data = ('a,b,c,d\n'
       '1,2,3,4\n'
       '5,6,7,8\n'
        '9,10,11'
       )


# In[61]:


###now lets see if we need to add col with different datatypes using dictionary we 
#create dataframe with above cell data
df4=pd.read_csv(StringIO(data),dtype={'a':int,'b':float,'c':int})


# In[62]:


df4.head()


# In[63]:


df4.info()


# In[64]:


data = ('index,a,b,c\n'
       '4,apple,bat,5.7\n'
       '8,orange,cow,10')


# In[65]:


## But I dont want index value like this I want index col in the place of 0,1 index ,
# 1st shift enter and check index col and go through all
pd.read_csv(StringIO(data))


# In[66]:


pd.read_csv(StringIO(data),index_col=0)  ## see index 


# In[67]:


# use index cols and usecols
data = ('a,b,c\n'
       '4,apple,bat\n'
       '8,orange,cow')


# In[68]:


pd.read_csv(StringIO(data),usecols=['a','b','c'],index_col=0)


# ### Now lets try to read tab seperated url with the help of "sep='\t' ,'\n'.\c
# pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',  sep='\t')

# In[69]:


pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item', sep='\t')


# In[70]:


pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item', sep='\t').to_csv('urldata.csv')


# ## In this part we are going to learn about 
# ### 1.read Json(read_json)
# ### 2.To Json(to_json)
# ### 3.Json Normalize

# In[71]:


data='{"employee_name":"Pitbull", "email": "pitbull@gmail.com", "job_profile": [{  "title1": "Team Lead","title2": "Sr.Developer"}]}'


# In[72]:


type(data)


# In[73]:


###first we need to check data is in json or not with this link JSONLint-The JSON Validator and drop your
# ddata in this and run you get the result your data is json or not.
{
    "employee_name":"Pitbull",
    "email": "pitbull@gmail.com",
    "job_profile": [{
        "title1": "Team Lead",
        "title2": "Sr.Developer"
    }]
}


# In[74]:


import pandas as pd


# In[75]:


pd.read_json(data,orient='index')


# In[76]:


pd.read_json(data,orient='records') ##records and columns are same almost


# In[77]:


pd.read_json(data,orient='columns')


# In[78]:


import pandas as pd
df5 = pd.DataFrame([['a','b'],['c','d']],
                  index=['row 1','row 2'],
                  columns=['cl 1','cl 2'])


# In[79]:


df5


# In[80]:


df5.to_json()


# In[81]:


df5.to_json(orient='index')  ###here row is taken as index


# In[82]:


df5.to_json(orient='columns')  ##here columns wise taken 


# In[83]:


df5.to_json(orient='records')


# In[84]:


df5.to_json(orient='split')


# In[85]:


df5.to_json(orient='table')  ##schema format


# In[86]:


schema='{"schema":{"fields":[{"name":"index","type":"string"},{"name":"cl 1","type":"string"},{"name":"cl 2","type":"string"}],"primaryKey":["index"],"pandas_version":"1.4.0"},"data":[{"index":"row 1","cl 1":"a","cl 2":"b"},{"index":"row 2","cl 1":"c","cl 2":"d"}]}'


# In[87]:


pd.read_json(schema,orient='table')


# In[88]:


df6 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)


# In[89]:


df6.head(2)


# In[90]:


df6.to_json(orient='index')  ###we convert our data into json format


# In[91]:


data = [{"employee_name": "Pitbull","email": "pitbull@gmail.com", "job_profile": {"title1": "Team Lead","title2": "Sr.Developer"}}]


# In[92]:


type(data)


# In[93]:


#pd.read_json(data) #here we seein job profile data he's unableto splitthat datasowehaveone one function called normalize 


# In[94]:


pd.json_normalize(data)  ##when you add this data then u get err through this then u need to change data
            ## format into list we simply add one square bracket in this data only and chk in jsonlint.com


# In[97]:


data = [
    {
        "id": 1,
        "name": "Cole Volk",
        "fitness": {"height": 130, "weight": 60},
    },
    {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}},
    {
        "id": 2,
        "name": "Faye Raker",
        "fitness": {"height": 130, "weight": 60},
    },
]                                


# In[98]:


pd.json_normalize(data)


# In[99]:


pd.json_normalize(data,max_level=0)


# In[100]:


pd.json_normalize(data,max_level=1)


# In[101]:


data = [
    {
        "state": "Florida",
        "shortname": "FL",
        "info": {"governor": "Rick Scott"},
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
        ],
    },
    {
        "state": "Ohio",
        "shortname": "OH",
        "info": {"governor": "John Kasich"},
        "counties": [
            {"name": "Summit", "population": 1234},
            {"name": "Cuyahoga", "population": 1337},
        ],
    },
]


# In[102]:


pd.json_normalize(data)


# In[103]:


pd.json_normalize(data, "counties",["state", "shortname",["info",'governor']])


# #  Python Pandas Working With HTML
# ###### In this Part we are going to learn about
# 
# ###### read HTML(read_html)
# ###### To HTML(to_html)

# In[104]:


import pandas as pd


# In[105]:


html=pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code")


# In[106]:


type(html)


# In[107]:


html[1]


# In[108]:


html=pd.read_html("https://en.wikipedia.org/wiki/Economy_of_the_United_States",match="Government debt")


# In[110]:


html[0]


# In[111]:


html=pd.read_html("https://en.wikipedia.org/wiki/Minnesota",match="Average daily maximum and minimum temperatures for selected cities in Minnesota")


# In[112]:


html[0]


# In[113]:


type(html[0])


# In[114]:


html[0].to_html('demo.html')


# # Python Pandas Working With XML 
# ###### Read XML and get Dataframe
# ###### Convert Dataframe to XML
# #### What is XML?
# 
# ###### * XML stands for eXtensible Markup Language
# ###### * XML is a markup language much like HTML
# ###### * XML was designed to store and transport data
# ###### * XML was designed to be self-descriptive
# ###### * XML is a W3C Recommendation

# In[116]:


import pandas as pd

pd.read_xml('employee.xml.xml')


# In[119]:


xml = '''<?xml version='1.0' encoding='utf-8'?>
<data xmlns="http://example.com">
 <row>
   <shape>square</shape>
   <degrees>360</degrees>
   <sides>4.0</sides>
   <firstname>Mohit</firstname>
 </row>
 <row>
   <shape>circle</shape>
   <degrees>360</degrees>
   <sides/>
   <firstname/>
 </row>
 <row>
   <shape>triangle</shape>
   <degrees>180</degrees>
   <sides>3.0</sides>
   <firstname/>
 </row>
</data>'''


# In[120]:


pd.read_xml(xml)


# In[121]:


xml = '''<?xml version='1.0' encoding='utf-8'?>
<data>
  <row shape="square" degrees="360" sides="4.0" firstname="Mohit"/>
  <row shape="circle" degrees="360"/>
  <row shape="triangle" degrees="180" sides="3.0" lastname="Singh"/>
</data>'''


# In[122]:


pd.read_xml(xml,xpath=".//row")


# In[123]:


xml = '''<?xml version='1.0' encoding='utf-8'?>
<doc:data xmlns:doc="https://example.com">
  <doc:row>
    <doc:shape>square</doc:shape>
    <doc:degrees>360</doc:degrees>
    <doc:sides>4.0</doc:sides>
  </doc:row>
  <doc:row>
    <doc:shape>circle</doc:shape>
    <doc:degrees>360</doc:degrees>
    <doc:sides/>
  </doc:row>
  <doc:row>
    <doc:shape>triangle</doc:shape>
    <doc:degrees>180</doc:degrees>
    <doc:sides>3.0</doc:sides>
  </doc:row>
</doc:data>'''


# In[124]:


df=pd.read_xml(xml,xpath=".//doc:row",namespaces={"doc": "https://example.com"})


# In[125]:


df.to_xml('test1.xml')


# # Python Pickling And Unpickling
# ###### The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
# 
# ###### Pickle in Python is primarily used in serializing and deserializing a Python object structure. In other words, it's the process of converting a Python object into a byte stream to store it in a file/database, maintain program state across sessions, or transport data over the network

# In[126]:


import seaborn as sns


# In[127]:


df=sns.load_dataset('tips')


# In[128]:


df.head()


# In[129]:


import pickle


# In[130]:


filename='file.pkl'


# In[131]:


##serialize process
pickle.dump(df,open(filename,'wb'))


# In[132]:


##unsereliaze
df=pickle.load(open(filename,'rb'))


# In[133]:


df.head()


# In[134]:


dic_example={'first_name':'Mohit','last_name':'kumar'}


# In[135]:


pickle.dump(dic_example,open('test.pkl','wb'))


# In[136]:


pickle.load(open('test.pkl','rb'))


# #                                            OR

# # Column manipulation
# ### Column Filter
# ###### df[['Title','Rating']]
# ###### df.filter(['Title','Rating'])
# ### Column Rename
# ###### df.rename(columns={'Title': 'a', 'Rating': 'c'},inplace=True)
# ###### df
# #### rename the columns back
# ###### df.rename(columns={'a': 'Title', 'c': 'Rating'},inplace=True)
# ###### df
# # Column Resorter/Reorder
# # show column values
# ######  df.columns.values
# # reorder Rating after Title
# ######  df[['Title', 'Rating','Genre', 'Description', 'Director', 'Actors', 'Year',
#        'Runtime (Minutes)',  'Votes', 'Revenue (Millions)',
#        'Metascore']]
# # Constant Value Column
# ######  df['new_column'] = 23
# ###### df.head()

# # Math Formula
# ###### df['Rating_Votes'] = df.Rating + df.Votes
# ###### df[['Rating_Votes','Rating','Votes']].head()

# # Number to String
# ###### df['Year_str'] =df['Year'].astype(str)
# ###### df.info()

# # String to Number
# ###### df['Year_int'] =df['Year_str'].astype(int)
# ###### df.info()

# # Double to Int
# ###### df['Rating_int'] = df['Rating'].round(0).astype(int)
# ###### df[['Rating_int','Rating']].head()
# 

# # String Replacer
# ###### df['Title'].replace('Prometheus', 'Alien') 
#  ###### df[df.Title == 'Prometheus']

# # String Manipulation
# ### lower cases
# ###### df['Title2'] = df['Title'].str.lower()
# ###### df[['Title2','Title']].head()
# 
# ### upper cases
# ###### df['Title2'] = df['Title'].str.upper() 
# ###### df[['Title2','Title']].head()
# 
# ### length of words
# ###### df['Title2'] = df['Title'].str.len() 
# ###### df[['Title2','Title']].head()
# 
# # first word
# ###### df['Title2'] = df['Title'].str.split(' ').str[0]
# ###### df[['Title2','Title']].head()
# 
# # find the word "Squad" in Title
# ###### df['Title2'] = df['Title'].str.find('Squad', 0) 
# ###### df[['Title2','Title']].head()

# # Date manipulation
# ###### pd.to_datetime('2010/11/12')
# ### Sort
# ###### df.sort_values(by='Title', ascending=True)
# ###### df.sort_values(by=['Director','Year'], ascending=True)
# 

# # Row manipulation
# ### Row Filter
# ####  select Title 'Prometheus' 
# ###### df[df.Title == 'Prometheus']
# #### select Rating greater or equal 8.5
#  ###### df[df.Rating >= 8.5]
# #### select Year equal 2016 and Rating greater or equal 8.5
# ###### df[(df.Year == 2016) & (df.Rating >= 8.5)]
# ####  select Title with 'Prometheus','Sing', 'Guardians of the Galaxy'
# ### titel = ['Prometheus','Sing', 'Guardians of the Galaxy']
# ###### df[df.Title.isin(titel)]
# ####  select years in 2010,2015,002
# ### years = [2010,2015,2002]
# ###### df[df.Year.isin(years)]
# #### Selects rows 1-to-3
# ###### df.iloc[0:3]
# #### First 4 rows and first 2 columns
# ###### df.iloc[0:4, 0:2]

# # Table Manipulation
# ## Group By
# #### number of titles per year
# ###### df.groupby("Year")["Title"].count().to_frame() 
# #### number of titles per year and per director
# ###### df.groupby(["Year","Director"])["Title"].count().to_frame().reset_index()
# ####  number of titles per director
# ###### df.groupby(["Director"])["Title"].count().to_frame(name = 'count').reset_index() 
# #### Total revenue per year and per director
# ###### df.groupby(["Year","Director"])["Revenue (Millions)"].sum().to_frame().reset_index()
# ####  Rating-Mean per director
# ###### df.groupby("Director")["Rating"].mean().to_frame().reset_index()
# #### combination of different group by functions
# ###### df.groupby(["Year","Director"]).agg(
#     {
#          'Title':"count",  # number of titles per year and director
#          'Rating':"mean",  # Rating-Mean per director
#          'Revenue (Millions)': "sum"  # Total revenue per year and director
#     }
# ).reset_index() 

# # Pivot / Unpivot
# #### Pivot over Director and mean over all other columns
# ###### pd.pivot_table(df,index=["Director"]).reset_index()
# #### Pivot with sum
# ######  df_rev_sum = pd.pivot_table(df,index=["Director","Year"],values=["Revenue (Millions)"],aggfunc=np.sum).reset_index()
# ###### df_rev_sum
# #### Unpivot over years
# ###### df_rating = pd.pivot_table(df,values=['Rating'], columns=['Year']).reset_index()
# ###### df_rating
#  ###### df4.melt(id_vars=['index'],var_name='Year',value_name='Title')

# # Join
# #### create new dataframe "df_dir_movies"
# ###### df_dir_movies = df.groupby(["Director"])["Title"].count().to_frame(name = 'number of movies').reset_index()
# ###### df_dir_movies
# #### create new dataframe "df_dir_rev"
# ###### df_dir_rev = df.groupby(["Director"])["Revenue (Millions)"].sum().to_frame(name = 'Revenue').reset_index()
# ###### df_dir_rev
# #### join the dataframe "df_dir_movies" with "df_dir_rev"
# #### how = rigtht, left, inner or outer
#  ###### pd.merge(df_dir_movies,df_dir_rev, left_on=['Director'], right_on=['Director'],how = 'left') 

# # Concatenate
# ###### df2 = df
# ###### df.append(df2) # Append df2 to df (The columns must be the same in both dataframes)
# ###### pd.concat([df, df2],axis=0) # concatenate two dataframes

# # Import Data from Databases
# #### Import from mysql
# ###### import pymysql
# 
# ###### conn = pymysql.connect(host='localhost',port=3306, db='database',user='root',password='pw')
# 
# ###### df = pd.read_sql_query(
# ###### "SELECT * FROM table LIMIT 3;",
#     conn)
# ###### df.tail(100)

# # Import Teradata
# ###### import teradata
#  
# ###### Make a connection
# ###### session = udaExec.connect(method="odbc",
#                           USEREGIONALSETTINGS="N",
#                           system= "dwh",
#                           username = "root",
#                           password = "pw");  
# ###### query = "SELECT * FROM DATABASEX.TABLENAMEX"
# ###### Reading query to df
#  ###### df = pd.read_sql(query,session)
# ###### do something with df,e.g.
# ###### print(df.head()) #to see the first 5 rows

# ### Import SAP-Hana
# ###### import pyhdb
#  
# ###### connection = pyhdb.connect(
#     host="localhost",
#     port=30015,
#     user="root,
#     password="pw"
# )
# ###### print(connection.isconnected())
# ###### query = "SELECT * FROM HDB_REPORT.\"Table\""
# ###### df = pd.read_sql(query,connection)
# ###### do something with df,e.g.
# ###### print(df.head()) #to see the first 5 rows

# #                      END
