df = df[df['status'].str.lower() != 'failed'].copy()

print("Rows left:", len(df))

df['category'] = df['category'].str.strip().str.title()

df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.strftime('%Y%m')
2026-01-15  →  202601
2026-02-20  →  202602
cust_summary = df.groupby('customer_name').agg(
    net_amount=('net_amount', 'sum'),
    txns=('transaction_id', 'count'),
    refunds=('refund', 'sum')
).reset_index()

print(cust_summary)

  customer_name  net_amount  txns  refunds
0         Anita       12500     4      500
1         Divya        9800     3      200
2        Gaurav       15200     5      800
pivot = df.pivot_table(
    index='month',
    columns='category',
    values='amount',
    aggfunc='sum',
    fill_value=0
)

print(pivot)

import seaborn as sns
import matplotlib.pyplot as plt

monthly_net = (
    df.groupby('month', as_index=False)['net_amount']
      .sum()
)

sns.lineplot(data=monthly_net, x='month', y='net_amount', marker='o')

plt.title('Total Net Amount by Month')
plt.xlabel('Month')
plt.ylabel('Total Net Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()