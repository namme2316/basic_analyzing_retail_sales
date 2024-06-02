import pandas as pd
import matplotlib.pyplot as plt

class SalesAnalyzer:
    def __init__(self,data):
        self.data = pd.read_csv(data)
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        
    def clean(self):
        self.data.dropna(inplace=True)
    
    def total_sales_per_product(self):
        return self.data.groupby('Product')['Sales'].sum()
    
    def best_selling_product(self):
        return self.total_sales_per_product().sort_values(ascending=False).index[0]
    
    def average_daily_sales(self):
        return self.data['Sales'].mean()
    
    def plot_sales_trend(self):
        self.data.groupby('Date')['Sales'].sum().plot(kind='line')

        plt.title('Sale Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total sales')
        plt.show()

    def plot_sales_per_product(self):
        self.total_sales_per_product().plot(kind = 'bar')
        plt.title('Sales Per Product')
        plt.xlabel('Product')
        plt.ylabel('Total sales')
        plt.show()