#STARTUP CASE STUDY AND ANALYSIS
#importing required libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize']=(16,7)
#importing the dataset for tha analysis
data = pd.read_csv("startup_funding.csv")
​
​
#creating a copy of original data
df=data.copy(deep=True)
​
#displaying the first 10 records in the dataset
df.head(10)

#changing column names of the given data
df.columns=["Sno","Date","StartupName","IndustryVertical","SubVertical","City","InvestorName","InvestmentType","AmountinUSD","Remarks"]
df.head()

#data cleaning
​
def clean_string(x):
    return str(x).replace("\\xc2\\xa0","").replace("\\\\xc2\\\\xa0","")
​
for col in ["Sno","Date","StartupName","IndustryVertical","SubVertical","City","InvestorName",
            "InvestmentType","AmountinUSD","Remarks"]:
    df[col]=df[col].apply(lambda x: clean_string(x))
    
    
print("Rows : ",df.shape[0])
print("Columns : ",df.shape[1])
Rows :  3044
Columns :  10
print("Columns Names ")
print(df.columns)
​
Columns Names 
Index(['Sno', 'Date', 'StartupName', 'IndustryVertical', 'SubVertical', 'City',
       'InvestorName', 'InvestmentType', 'AmountinUSD', 'Remarks'],
      dtype='object')
DATA CLEANING
df.isnull().sum()

#Since remarks has many NaN values we will remove the remark columns
​
df=df.drop(['Remarks'],axis=1)
print("Data Set after removing remarks ")
df.head()

# lets convert the amount column into numerical, so that we can analyze the values inside it
​
# function to clean the AmounInUsd Column
def clean_amount(x):
    x = ''.join([c for c in str(x) if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']])
    x = str(x).replace(",","").replace("+","")
    x = str(x).lower().replace("undisclosed","")
    x = str(x).lower().replace("n/a","")
    if x == '':
        x = '-999'
    return x
​
# lets apply the function on the column
df["AmountinUSD"] = df["AmountinUSD"].apply(lambda x: float(clean_amount(x)))
​
## Cleaning the dates
​
# doesn't show warnings
import warnings
warnings.filterwarnings('ignore')
​
df['Date'][df['Date']=='12/05.2015'] = '12/05/2015'
df['Date'][df['Date']=='13/04.2015'] = '13/04/2015'
df['Date'][df['Date']=='15/01.2015'] = '15/01/2015'
df['Date'][df['Date']=='22/01//2015'] = '22/01/2015'
df['Date'][df['Date']=='05/072018'] = '05/07/2018'
df['Date'][df['Date']=='01/07/015'] = '01/07/2015'
df['Date'][df['Date']=='\\\\xc2\\\\xa010/7/2015'] = '10/07/2015'
DATA ANALYSIS
1.How does funding of ecosystem changes w.r.t time?
#converting to specific format eg. 201702 represent 2nd feb in 2017
df["yearmonth"] = (pd.to_datetime(df['Date'],
         format='%d/%m/%Y').dt.year*100)+(pd.to_datetime(df['Date'],format='%d/%m/%Y').dt.month)
​
​
temp = df['yearmonth'].value_counts().sort_values(ascending = False).head(10)
print("Number of funding per month in decreasing order(Top 10)\n",temp)
year_month = df['yearmonth'].value_counts()

#barplot
sns.barplot(year_month.index, year_month.values,palette="copper")
plt.xticks(rotation=90)
plt.xlabel("Year-month transaction",fontsize=15)
plt.ylabel("Number of fundings",fontsize=15)
Text(0, 0.5, 'Number of fundings')

2.WHAT IS THE GENRAL AMOUNT THAT STARTUP GET IN INDIA
#Maximum, Minimum and average funding for a startup
print("Maximum funding for a startup : ",df['AmountinUSD'].dropna().max())
print("Minimum funding for a startup : ",df['AmountinUSD'].dropna().min())
print("Average funding for a startup : ",df['AmountinUSD'].dropna().mean())
Maximum funding for a startup :  3900000000.0
Minimum funding for a startup :  -999.0
Average funding for a startup :  13270058.261169514
#10 startups with least funding 
df[['AmountinUSD','StartupName']].sort_values(by='AmountinUSD', ascending=True).head(10)

# 10 startups with most funding
df[['AmountinUSD','StartupName']].sort_values(by='AmountinUSD', ascending=True).tail(10)

#Total Startups Funding
print("Total Startups funding : ",len(df['StartupName'].unique()))


#barplot
plt.rcParams['figure.figsize'] = (15, 5)
sns.barplot(y=startupname.index,x=startupname.values,palette='Dark2')
plt.ylabel("Startup Name",fontsize=15)
plt.xlabel("No of fundings",fontsize=15)
Text(0.5, 0, 'No of fundings')

3. WHAT KIND OF INDUSTRIES ARE PREFERRED MORE FOR STARTUPS
df['IndustryVertical']=df['IndustryVertical'].replace('nan','Consumer Technology')

df['IndustryVertical']=df['IndustryVertical'].replace('nan','Consumer Technology')
​
Industry=df['IndustryVertical'].value_counts().head(10)
print(Industry)

plt.xticks(rotation='90')
plt.title("Industries preferred for startups",fontsize=20)
plt.xlabel("Industry vertical for startups",fontsize=15)
plt.ylabel("Fundings for startups",fontsize=15)
plt.show()
#plotting for industry vertical
plt.rcParams['figure.figsize'] = (15, 5)
sns.barplot(x=Industry.index,y=Industry.values,palette='autumn')
plt.xticks(rotation='90')
plt.title("Industries preferred for startups",fontsize=20)
plt.xlabel("Industry vertical for startups",fontsize=15)
plt.ylabel("Fundings for startups",fontsize=15)
plt.show()

#plotting for Subvertiical
subind=df['SubVertical'].value_counts().head(10)
subvertical=subind[1:]
print(subvertical)

plt.rcParams['figure.figsize'] = (15, 5)
sns.lineplot(x=subvertical.index,y=subvertical.values,palette='winter')
plt.xticks(rotation='90')
plt.title("Sub Verical Industries preferred for startups",fontsize=20)
plt.xlabel("Sub vertical for startups",fontsize=15)
plt.ylabel("Fundings for startups",fontsize=15)
plt.show()

4.DOES LOCATION PLAY IMPORTNT ROLE ON INDIAN STARTUPS
f
df['City'] = df['City'].replace(('Bengaluru', 'nan'),('Bangalore', 'Bangalore'))
​
city = df['City'].value_counts().head(10)
print(city)
​

​
# plot
sns.barplot(city.index, city.values, palette = 'Wistia')
plt.xticks(rotation='vertical')
plt.xlabel('city location of startups', fontsize=12)
plt.ylabel('Number of fundings made', fontsize=12)
plt.title("city location of startups with number of funding", fontsize=16)
plt.show()

5.WHO PLAYS THE MAIN ROLE IN INDIAN STARTUPS
df['InvestorName'][df['InvestorName'] == 'Undisclosed investors'] = 'Undisclosed Investors'
df['InvestorName'][df['InvestorName'] == 'undisclosed Investors'] = 'Undisclosed Investors'
df['InvestorName'][df['InvestorName'] == 'undisclosed investors'] = 'Undisclosed Investors'
df['InvestorName'][df['InvestorName'] == 'Undisclosed investor'] = 'Undisclosed Investors'
df['InvestorName'][df['InvestorName'] == 'Undisclosed Investor'] = 'Undisclosed Investors'
df['InvestorName'][df['InvestorName'] == 'Undisclosed'] = 'Undisclosed Investors'
df['InvestorName'][df['InvestorName'] == 'nan'] = 'Undisclosed Investors'
​
​
# value counts
investors = df['InvestorName'].value_counts()[1:].head(10)
print(investors)
​
#  plot the data
sns.barplot(investors.index, investors.values, palette = 'cool')
plt.xticks(rotation='vertical')
plt.xlabel('Investors Names', fontsize=12)
plt.ylabel('Number of fundings made', fontsize=12)
plt.title("Investors Names with number of funding", fontsize=16)
plt.show()


6. WHAT ARE THE DIFFERENT TYPES PF FUNDING FOR STARTUPS
investment = df['InvestmentType'].value_counts().head(10)
print(investment)
investment = df['InvestmentType'].value_counts().head(10)
print(investment)
​
​

# lets clean the dataset
df['InvestmentType'][df['InvestmentType'] == 'SeedFunding'] = 'Seed Funding'
df['InvestmentType'][df['InvestmentType'] == 'Crowd funding'] = 'Crowd Funding'
df['InvestmentType'][df['InvestmentType'] == 'PrivateEquity'] = 'Private Equity'


investment = df['InvestmentType'].value_counts().head(10)
print(investment)

# lets clean the dataset
df['InvestmentType'][df['InvestmentType'] == 'SeedFunding'] = 'Seed Funding'
df['InvestmentType'][df['InvestmentType'] == 'Crowd funding'] = 'Crowd Funding'
df['InvestmentType'][df['InvestmentType'] == 'PrivateEquity'] = 'Private Equity'
​
​
investment = df['InvestmentType'].value_counts().head(10)
print(investment)
​

sns.barplot(investment.index, investment.values, palette = 'summer')
plt.xticks(rotation='vertical')
plt.xlabel('Investment Type', fontsize=12)
plt.ylabel('Number of fundings made', fontsize=12)
plt.title("Investment Type with number of funding", fontsize=16)
plt.show()

​
