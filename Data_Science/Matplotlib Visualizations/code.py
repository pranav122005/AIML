# 1. Line Plot
plt.plot(data['SepalLengthCm'])
plt.title('Line Plot - Sepal Length')
plt.show()

# 2. Histogram
plt.hist(data['PetalLengthCm'], bins=20)
plt.title('Histogram - Petal Length')
plt.show()

# 3. Pie Chart
species_counts = data['Species'].value_counts()
species_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Species Distribution')
plt.ylabel('')
plt.show()

# 4. Multi-Dimensional Box Plot
data.iloc[:, 0:4].plot(kind='box')
plt.title('Multi-dimensional Box Plot')
plt.show()
