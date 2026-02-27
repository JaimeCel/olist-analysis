import numpy as np 
import matplotlib.pyplot as plt
from sqlalchemy import create_engine 
import pandas as pd
from dotenv import load_dotenv
import os
import seaborn as sns
import matplotlib.dates as mdates


load_dotenv()


engine=create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}")
print("USER:", repr(os.getenv("DB_USER")))
print("PASS:", repr(os.getenv("DB_PASSWORD")))
                     

growth=pd.read_sql("SELECT * FROM growth_overall",engine)
deliveries=pd.read_sql('SELECT * FROM deliveries',engine)
new_customers=pd.read_sql('SELECT * FROM new_customers',engine)
customer_repeat=pd.read_sql('SELECT * FROM customer_repeat',engine)
product_orders=pd.read_sql('SELECT * FROM product_orders',engine)

product_revenue=pd.read_sql('SELECT * FROM product_revenue',engine)
     
reviews=pd.read_sql('SELECT * FROM score',engine)

growth=growth.rename(columns={'average':'average_per_order','round':'revenue_per_month'})
print(growth)
# print renevue vs month
fig,ax=plt.subplots(figsize=(10,6))
sns.lineplot(data=growth[:-2],x='month',y='revenue_per_month',ax=ax,color='red',linewidth=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Jan 2024
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))
ax.set_ylabel('revenue(millions)')
plt.xticks(rotation=45)  # rotate so they don't overlap
plt.tight_layout
plt.savefig("growth vs month")

# print orders vs month.2

fig,ax=plt.subplots(figsize=(10,6))
sns.lineplot(data=growth[:-2],x='month',y='num_orders',ax=ax,color='red',linewidth=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Jan 2024
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.set_ylabel('orders')
plt.xticks(rotation=45)  # rotate so they don't overlap
plt.tight_layout
plt.savefig("orders vs month")


# print average value per order vs month
fig,ax=plt.subplots(figsize=(10,6))
sns.lineplot(data=growth[5:-2],x='month',y='average_order_value',ax=ax,color='red',linewidth=2)
plt.ylim(0, 200)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Jan 2024
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.set_ylabel('average price per order')
plt.xticks(rotation=45)  # rotate so they don't overlap
plt.tight_layout()
plt.savefig("average price per order vs month.png")












