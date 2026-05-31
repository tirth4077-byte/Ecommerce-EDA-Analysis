import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_Dataset for Data Analytics.csv")

print("\ndataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\n Data Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

print("\nTotal revenue:")
print(df['TotalPrice'].sum())

print("\nTop Products:")
print(df['Product'].value_counts().head(10))

df["Product"].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Products")
plt.xlabel("Products")
plt.ylabel("Orders")

plt.savefig("charts/top_products.png")
plt.show()

print("\nPayment methods:")
print(df['PaymentMethod'].value_counts())

df['PaymentMethod'].value_counts().plot(kind='bar')

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Count")

plt.savefig("charts/payment_methods.png")

plt.show()

print("\nOrder Status:")
print(df['OrderStatus'].value_counts())

df['OrderStatus'].value_counts().plot(kind='pie', autopct='%1.1f%%')

plt.title("Order Status Distribution")

plt.ylabel("")

plt.savefig("charts/order_status.png")

plt.show()

plt.hist(df['TotalPrice'])

plt.title("Revenue Distribution")
plt.xlabel("Total Price")
plt.ylabel("Frequency")

plt.savefig("charts/revenue_distribution.png")

plt.show()

df.boxplot(column='TotalPrice')
plt.title("Total Price Outliers")
plt.savefig("charts/price_outliers.png")
plt.show()

print("\nReferral Sources:")
print(df['ReferralSource'].value_counts())
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

print("\nKey Observations:")

print("1. Some products are ordered significantly more than others.")
print("2. Certain payment methods are more popular.")
print("3. Most orders are successfully delivered.")
print("4. Some orders have extremely high total prices (outliers).")
print("5. Referral sources impact customer traffic.")
print("\nEDA Completed Successfully!")