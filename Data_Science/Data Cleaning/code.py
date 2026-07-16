#Impute missing values
data['SepalWidthCm'] = data['SepalWidthCm'].fillna(data['SepalWidthCm'].median())
data['PetalLengthCm'] = data['PetalLengthCm'].fillna(data['PetalLengthCm'].median())

#Drop any remaining nulls
data = data.dropna() 

print("Null values after cleaning:")
display(data.isnull().sum())
