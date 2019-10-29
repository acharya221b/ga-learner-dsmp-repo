# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(path)
#plt.hist(data.Rating)
data=data[data.Rating<=5]


#Code starts here


#Code ends here


# --------------
# code starts here
total_null=data.isnull().sum()

percent_null=(total_null/data.isnull().count())


missing_data=pd.concat([total_null,percent_null],keys=['Total','Percent'],axis=1)
data.dropna(inplace=True)
total_null_1=data.isnull().sum()

percent_null_1=(total_null_1/data.isnull().count())

missing_data_1=pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis=1)
# code ends here


# --------------

#Code starts here
sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10) 
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
data.Installs.replace(r'[,+]','',regex=True,inplace=True)

data.Installs=data.Installs.astype(int)
le=LabelEncoder()
le.fit(data.Installs)
data.Installs=le.transform(data.Installs)

#Code ends here



# --------------
#Code starts here
import re
data.Price=data['Price'].map(lambda x: re.sub(r'\W+', '', x))
data.Price=data.Price.astype(float)

data.info()
sns.regplot(x='Price',y='Rating',data=data)
#Code ends here


# --------------

#Code starts here
data.Genres=data.Genres.str.split(';').map(lambda x: x[0])
gr_mean=data[['Genres','Rating']].groupby('Genres',as_index=False).mean()

gr_mean.describe()

gr_mean=gr_mean.sort_values(by='Rating')

gr_mean.head(1)
gr_mean.tail(1)


#Code ends here


# --------------

#Code starts here
data['Last Updated']=pd.to_datetime(data['Last Updated'])

data.info()

max_date=data['Last Updated'].max()

data['Last Updated Days']=data['Last Updated'].map(lambda x: max_date-x).dt.days

data.info()

sns.regplot(x='Last Updated Days',y='Rating',data=data)



#Code ends here


