import requests

 

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

df['order_date'] = pd.to_datetime(df['order.order_purchase_date'])

# Extract the day of the week (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
df['day_of_week'] = df['order_date'].dt.dayofweek

# Filter the orders placed on weekends (Saturday or Sunday)
weekend_orders = df[(df['day_of_week'] == 5) | (df['day_of_week'] == 6)]

# Count the number of orders placed on weekends
num_weekend_orders = len(weekend_orders)

print(f"Number of orders placed on weekends: {num_weekend_orders}")

category_sales = df.groupby('product.category')['order.order_id'].count()
category_sales
