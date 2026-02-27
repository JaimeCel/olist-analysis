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

print(deliveries)
norm = plt.Normalize(deliveries['late_delivery_percent'].min(), deliveries['late_delivery_percent'].max())
colors = cm.RdYlGn_r(norm(deliveries['late_delivery_percent']))
 
fig,ax=plt.subplots(figsize=(10,6))
bars = ax.barh(deliveries['customer_state'], deliveries['avg_delivery_days'], color=colors)
sm = plt.cm.ScalarMappable(cmap='RdYlGn_r', norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax, label='Late Delivery %')

ax.set_xlabel('Avg Delivery Days')
ax.set_title('Delivery Performance by State')
plt.tight_layout()
plt.savefig("late deliveries vs state")


