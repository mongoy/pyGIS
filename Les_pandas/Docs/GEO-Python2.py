#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# ПРИМЕР СОЗДАНИЯ СЕРИИ И ДАТАФРЕЙМА

# In[23]:


# Create Pandas Series from a list
number_series = pd.Series([4, 5, 6, 7.0], index=['a', 'b', 'c', 'd'])
print(number_series)

# Station names
stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi', 'Helsinki Malmi airfield']

# Latitude coordinates of Weather stations
lats = [59.77, 61.2, 60.18, 60.25]

# Longitude coordinates of Weather stations
lons = [22.95, 26.05, 24.94, 25.05]

# Create Pandas DataFrame from a 3-list
new_df = pd.DataFrame(data={"station_name": stations, "lat": lats, "lon": lons})
print(new_df)


# In[77]:


# считаем данные в датафрейм без заголовка (8 строк) с 9-й строки
df = pd.read_csv('Kumpula-June-2016-w-metadata.txt', sep=',', skiprows=8)


# In[6]:


df.head() # 5 сверху, df - все, df.tail() - 5 снизу


# In[7]:


df.shape # (30, 4) строки колонки


# In[8]:


df.columns # Index(['YEARMODA', 'TEMP', 'MAX', 'MIN'], dtype='object')


# In[9]:


df.columns.values # array(['YEARMODA', 'TEMP', 'MAX', 'MIN'], dtype=object)


# In[10]:


df.columns.value_counts()


# In[11]:


df.index # RangeIndex(start=0, stop=30, step=1)


# Создание новых колонок

# In[81]:


# Define a new column "DIFF"
df = df
df['DIFF'] = 0.0
# Print the dataframe
print(df.head())


# In[82]:


# Calculate difference between temp and min column values
df['DIFF_MIN'] = df['TEMP'] - df['MIN']
# Print the dataframe
print(df.head())


# In[83]:


# Create a new column and convert temp fahrenheit to celsius:
df['TEMP_CELSIUS'] = (df['TEMP'] - 32) / (9/5)
#Check output
print(df.head())


# Выбор данных из ДатаФрейма

# In[47]:


# Select first five rows of dataframe using index values
selection = df[0:5]
print(selection)


# In[56]:


# Select one row using index
selection = df.loc[4]
#Print all attributes from the selected row
print(selection)
print(' ')
#Print one attribute from the selected row
print(selection['TEMP'])
print(' ')
# Select first five rows of dataframe using index values
selection = df[0:5]
print(selection)
print(' ')
# Select temp column values on rows 0-5
selection = df.loc[0:5, 'TEMP']
print(selection)
print(' ')
# Select columns temp and temp_celsius on rows 0-5
selection = df.loc[0:5, ['TEMP', 'TEMP_CELSIUS']]
print(selection)
print(' ')
# Select the temprerature (column TEMP) on the first fow (index 0) of our DataFrame 
print(df.at[0, "TEMP"])


# In[44]:


print(df.iloc[0: 5, 0 : 2])
print(' ')
print(df.iloc[0, 1])
print(' ')
print(df.iloc[-1])


# Фильтрация и обновление данных

# In[84]:


# Select rows with temp celsius higher than 15 degrees
warm_temps = df.loc[df['TEMP_CELSIUS'] > 15]
print(warm_temps.head())


# In[85]:


# Select rows with temp celsius higher than 15 degrees from late June 2016
warm_temps = df.loc[(df['TEMP_CELSIUS'] > 15) & (df['YEARMODA'] >= 20160615)]
print(warm_temps)


# In[64]:


# Reset index
warm_temps1 = warm_temps.reset_index()
print(warm_temps1)
print(' ')
# отказ от создания колонки INDEX
warm_temps2 = warm_temps.reset_index(drop=True)
print(warm_temps2)


# In[86]:


selections = df[['YEARMODA', 'TEMP']]
selections.head()


# In[87]:


df.mean()


# In[88]:


# Среднее значение
print(df['TEMP'].mean()) # 59.730000000000004


# In[89]:


print(df[['TEMP', 'MIN', 'MAX']].head())
df[['TEMP', 'MIN', 'MAX']].plot()


# Работа с недостающими данными

# In[90]:


# Drop no data values based on the MIN column
warm_temps[['TEMP', 'MIN', 'MAX']].plot()
warm_temps3 = warm_temps.dropna(subset=['MIN'])
print(warm_temps3)
warm_temps3[['TEMP', 'MIN', 'MAX']].plot()


# In[91]:


## Fill Nan values
warm_temps4 = warm_temps.fillna(-9999)
print(warm_temps4)
warm_temps4[['TEMP', 'MIN', 'MAX']].plot()


# Преобразование типов данных

# In[92]:


df_tranc = df
print("Original values:")
print(df_tranc['TEMP'].head())


# In[93]:


# Преобразование с простым отсечением дробной части
df_tranc = df
print("Truncated integer values:")
print(df_tranc['TEMP'].astype(int).head())


# In[94]:


# Преобразование с округлением
df_tranc = df
print("Rounded integer values:")
print(df_tranc['TEMP'].round(0).astype(int).head())


# Уникальное значение

# In[99]:


# Get unique celsius values
unique = df['TEMP'].unique()
print(unique)
print(' ')
# unique values as list
print(list(unique))


# In[102]:


# Number of unique values
unique_temps = len(unique)
print("В июне 2016г., с уникальной температурой было -", unique_temps, " дней")


# Сортировка данных

# In[103]:


# По возрастающей
df.sort_values(by='TEMP').head()


# In[104]:


# По убывающей
df.sort_values(by='TEMP', ascending=False).head()


# Запись данных в файл

# In[105]:


# define output filename
output_fp = "Kumpula_temps_June_2016.csv"

# Save dataframe to csv
df.to_csv(output_fp, sep=',')


# In[106]:


# Cохраним значения температуры из warm_tempsфрейма данных без индекса 
# и только с 1 десятичной дробью в числах с плавающей запятой
output_fp2  =  "Kumpula_temps_above15_June_2016.csv" 
warm_temps .to_csv ( output_fp2,  sep =',',  index = False,  float_format ="%.1f")


# In[ ]:




