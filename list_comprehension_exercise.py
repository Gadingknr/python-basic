"""Carly's Clippers: Data Analyst's Tasks

As the Data Analyst at Carly’s Clippers, your role involves analyzing data from the past weeks to help plan business operations. This includes calculating metrics and making pricing adjustments.
"""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate the total price of all hairstyles.
total_price = 0
for price in prices:
    total_price += price

# Calculate the average price of hairstyles.
average_price = total_price / len(prices)
print(average_price)

# Reduce all prices by $5.
new_prices = [price - 5 for price in prices]
print(new_prices)

# Calculate the total revenue generated last week.
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print(total_revenue)

# Calculate the average daily revenue.
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Identify hairstyles priced under $30.
cuts_under_30 = [prices[i] for i in range(len(prices)) if prices[i] < 30]
print(cuts_under_30)
