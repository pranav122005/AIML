# 1. Create a new mathematical column
data['PetalAreaCm'] = data['PetalLengthCm'] * data['PetalWidthCm']

# 2. Binning (Creating Categories)
bins = [0, 2.5, 5, 7]
labels = ['Small', 'Medium', 'Large']
data['PetalLengthCm_Group'] = pd.cut(data['PetalLengthCm'], bins=bins, labels=labels)

# 3. Label Encoding (Text to Numbers)
le = LabelEncoder()
data['Species_encoded'] = le.fit_transform(data['Species'])

print("Dataset with Engineered Features:")
display(data.head())
