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

# print(data)

import pandas as pd

df = pd.json_normalize(data)



def no_sizes(x):

    if (x ==np.NaN) | (x==None):

        return 0

    elif str(str(x).find(',')) == '-1':

        return 1

    else:

        return len(x.split(','))



df['no._of_sizes'] = df['product.sizes'].apply(no_sizes)


df['product.sizes']
product_with_max_sizes = df.loc[df['no._of_sizes'].idxmax()]

product_with_max_sizes[['product.product_name']]
product_with_max_sizes[['product.product_name']]




