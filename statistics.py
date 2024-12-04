import pandas as pd

df = pd.read_csv('reviews')
print(df.head())
print(df.tail())

print("Mean:", df['column'].mean())
print("Median:", df['column'].median())
print("Mode:", df['column'].mode()[0])
print("Variance:", df['column'].var())
print("Standard Deviation:", df['column'].std())

missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

df['column'].fillna(df['column'].mean(), inplace=True)

Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['column'] < (Q1 - 1.5 * IQR)) | (df['column'] > (Q3 + 1.5 * IQR))]
print("Outliers:\n", outliers)

df.to_csv('cleaned_dataset.csv', index=False)

print("EDA complete and cleaned data saved as 'cleaned_dataset.csv'")
