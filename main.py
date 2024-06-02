from salesAnalyzer import SalesAnalyzer

data = 'data\\retail_sales.csv'
analyzer = SalesAnalyzer(data)

#calculate
print('Total Sales Per Product \n', analyzer.total_sales_per_product())
print('Best Selling Product \n', analyzer.best_selling_product())
print('Average Daily Sales \n', analyzer.average_daily_sales())

#plot
analyzer.plot_sales_per_product()
analyzer.plot_sales_trend()