import pandas as pd


data_orders = pd.read_csv('orders_pandas_practice.csv')
df_orders = pd.DataFrame(data_orders)


df_orders['order_date'] = pd.to_datetime(df_orders['order_date'], format='%Y-%m-%d')
# print(df_orders.info())

# nan_idx_orders = df_orders.dropna(how='any', axis=0).index
# nan_df_orders = df_orders.drop(index=nan_idx_orders)
# print(nan_df_orders)


# df_orders = df_orders.loc[df_orders['city'] == 'Yaroslavl']
# df_orders = df_orders.loc[(df_orders['category'] == 'Laptop') & (df_orders['price'] > 90000.0)]
# df_orders = df_orders.loc[('2026-08-01' <= df_orders['order_date']) & (df_orders['order_date'] < '2026-09-01')]
# print(df_orders)

df_orders['total'] = df_orders['price'] * df_orders['quantity']
# df_orders['month'] = df_orders['order_date'].dt.month
# df_orders['expensive'] = df_orders['price'].apply(lambda x: x > 50000)
# print(df_orders)

# print(round(df_orders.groupby(by='category')['price'].agg(['mean']).reset_index(), 1))
# print(round(df_orders.groupby(by='city')['total'].agg(['sum']), 1).reset_index())
# print(round(df_orders.groupby('category')['price'].agg(['min', 'max', 'mean']).reset_index(), 1))

# df_cost_orders = df_orders.sort_values(by='total', ascending=False, ignore_index=True).head(5)
# print(df_cost_orders)

print(df_orders.groupby(['category', 'city'])['price'].agg(['sum']))
#                            sum
# category   city               
# Headphones Moscow       9000.0
#            SPB          6500.0
# Laptop     Kazan       99000.0
#            Moscow      87000.0
#            SPB        183000.0
#            Yaroslavl  252000.0
# Phone      Kazan       45000.0
#            Moscow     121000.0
#            Yaroslavl   43000.0
# Tablet     Kazan       35000.0
#            SPB         66000.0
#            Yaroslavl   30000.0
