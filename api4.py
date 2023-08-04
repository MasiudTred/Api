import requests
import numpy as np
access_key = 'fe66583bfe5185048c66571293e0d358'
header = {'access_token': access_key}
baseurl = 'https://globalmart-api.onrender.com'
endpoint = '/mentorskool/v1/sales?offset=1&limit=100'

data=[]

for i in range(5):
    response = requests.get(baseurl+endpoint, headers=header)
    response_data = response.json()
    endpoint = response_data['next']
    data.extend(response.json()['data'])

import pandas as pd

df = pd.json_normalize(data)

# Convert 'order_purchase_date' column to datetime data type
df['order.order_purchase_date'] = pd.to_datetime(df['order.order_purchase_date'])

# Extract the month name and create a new column 'month_name'
df['month_name'] = df['order.order_purchase_date'].dt.strftime('%B')


print(df.groupby('month_name')['sales_amt'].sum().sort_values())

profit_margin = df.groupby('month_name')['profit_amt'].sum().sort_values(ascending=False)
profit_margin_df= pd.DataFrame(profit_margin).reset_index()
print(profit_margin_df)


total_profit_margin = profit_margin_df['profit_amt'].sum()
req_pm_df = profit_margin_df[profit_margin_df['profit_amt'] > total_profit_margin*0.20]
print(req_pm_df)



# Convert 'order_estimated_date' and 'order_delivered_date' columns to datetime data type
df['order.order_estimated_delivery_date'] = pd.to_datetime(df['order.order_estimated_delivery_date'], errors='coerce')
df['order.order_delivered_customer_date'] = pd.to_datetime(df['order.order_delivered_customer_date'], errors='coerce')

# Calculate the delay duration by subtracting 'order_estimated_date' from 'order_delivered_date'
df['delay'] = (df['order.order_delivered_customer_date'] - df['order.order_estimated_delivery_date']).dt.days

# Create the 'delay_status' column based on the delay duration
df['delay_status'] = df['delay'].apply(lambda x: 'Late' if x >= 0 else 'Early')

# Display the DataFrame with the delay information
print(df)


late_deliveries = df[df['delay_status'] == 'Late']
print(late_deliveries.shape[0])


print(late_deliveries['order.vendor.VendorID'].value_counts().idxmax())


l = [x for x in df['order.customer.customer_name'] if x.startswith('Alan')]
print(l)


