# 1. Violin Plot
sns.violinplot(x='Species', y='SepalLengthCm', data=data)
plt.title('Seaborn Violin Plot')
plt.show()

# 2. Scatterplot with Hue
sns.scatterplot(x='SepalLengthCm', y='PetalLengthCm', hue='Species', data=data)
plt.title('Seaborn Scatter Plot')
plt.show()

# 3. Correlation Heatmap
correlation_matrix = data.iloc[:, 0:4].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
