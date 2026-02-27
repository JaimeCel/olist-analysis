import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os
import seaborn as sns
import matplotlib.dates as mdates
import matplotlib.cm as cm

load_dotenv()
engine=create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}"
                     )

deliveries=pd.read_sql('SELECT * FROM deliveries',engine)
new_customers=pd.read_sql('SELECT * FROM new_customers',engine)
customer_repeat=pd.read_sql('SELECT * FROM customer_repeat',engine)
product_orders=pd.read_sql('SELECT * FROM product_orders',engine)

product_revenue=pd.read_sql('SELECT * FROM product_revenue',engine)

reviews=pd.read_sql('SELECT * FROM score',engine)
new_customers['cohort_month'] = pd.to_datetime(new_customers['cohort_month'],unit='ms')
print(new_customers.info())
print(new_customers)
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(new_customers['cohort_month'][5:-2], new_customers['new_customers'][5:-2], color='steelblue', width=20)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.set_ylabel('New customers')
ax.set_xlabel('month')
ax.tick_params(labelsize=11)
plt.xticks(rotation=45)
sns.despine()
plt.tight_layout()
plt.savefig("new customers vs month")

