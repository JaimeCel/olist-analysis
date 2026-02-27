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

fig,ax=plt.subplots(figsize=(10,6))
sns.barplot(data=product_revenue,y='product_category_name',x='revenue_percent',order=product_revenue.sort_values('revenue_percent', ascending=False)['product_category_name'],
            color='steelblue',ax=ax)


ax.set_ylabel('Product category name ')
ax.set_xlabel('Revenue (%)')
ax.tick_params(labelsize=11)
sns.despine()
plt.tight_layout()
plt.savefig("revenue percetn vs product category name")



