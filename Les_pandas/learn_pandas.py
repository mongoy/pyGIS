import os
import pandas as pd


ROOT_PATH = os.path.abspath(os.curdir)
file_path = os.path.join(ROOT_PATH, "Input\\Kumpula-June-2016-w-metadata.txt")
# считаем данные в датафрейм без заголовка - 8 строк
df = pd.read_csv(file_path, sep=',', skiprows=8)
"""
    df
    df.haed()
    df.tail()
    df.shape # (30, 4)
    df.columns # Index(['YEARMODA', 'TEMP', 'MAX', 'MIN'], dtype='object')
    df.columns.values # array(['YEARMODA', 'TEMP', 'MAX', 'MIN'], dtype=object)
    df.columns.value_counts()
    df.index # RangeIndex(start=0, stop=30, step=1)
    selections = df[['YEARMODA', 'TEMP']]
    df['TEMP'].mean() 59.730000000000004
    df.mean()
    df[['TEMP', 'MIN', 'MAX']].plot()
    
"""
print(df.shape)

# Create Pandas Series from a list
number_series = pd.Series([4, 5, 6, 7.0], index=['a', 'b', 'c', 'd'])
print(number_series)

# Station names
stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi', 'Helsinki Malmi airfield']

# Latitude coordinates of Weather stations
lats = [59.77, 61.2, 60.18, 60.25]

# Longitude coordinates of Weather stations
lons = [22.95, 26.05, 24.94, 25.05]

new_data = pd.DataFrame(data={"station_name": stations, "lat": lats, "lon": lons})
print(new_data)

"""
    # Define a new column "DIFF"
    data['DIFF'] = 0.0
    # Print the dataframe
    print(data)

    #Calculate max min difference
    data['DIFF'] = data['MAX'] - data['MIN']
    # Check the result
    print(data.head())    

    # Calculate difference between temp and min column values
    data['DIFF_MIN'] = data['TEMP'] - data['MIN']
    # Print the dataframe
    print(data)    

    # Create a new column and convert temp fahrenheit to celsius:
    data['TEMP_CELSIUS'] = (data['TEMP'] - 32) / (9/5)
    #Check output
    print(data.head())

    # Select first five rows of dataframe using index values
    selection = data[0:5]
    print(selection)

    # Select one row using index
    selection = data.loc[4]
        #Print one attribute from the selected row
        print(selection['TEMP'])    
    # Select first five rows of dataframe using index values
    selection = data[0:5]
    # Select temp column values on rows 0-5
    selection = data.loc[0:5, 'TEMP']
    # Select columns temp and temp_celsius on rows 0-5
    selection = data.loc[0:5, ['TEMP', 'TEMP_CELSIUS']]
    #
    print(selection)
    data.iloc[0: 5 :, 0 : 2]
    data.iloc[0, 1]
    data.iloc[-1]

    # Select rows with temp celsius higher than 15 degrees
    warm_temps = data.loc[data['TEMP_CELSIUS'] > 15]
    print(warm_temps)    

    # Select rows with temp celsius higher than 15 degrees from late June 2016
    warm_temps = data.loc[(data['TEMP_CELSIUS'] > 15) & (data['YEARMODA'] >= 20160615)]
    print(warm_temps)



"""

