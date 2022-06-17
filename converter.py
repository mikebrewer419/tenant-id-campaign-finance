import pandas as pd
import sqlite3
conn = sqlite3.connect('tenant__id__campaign_finance.db')

data = pd.read_csv('tenant__id__campaign_finance_dl__fC__all__1f6464ed220783f3cdc0ddc8d65d9f94.csv')
data.to_sql('id_campaign_finance_contribution', conn, if_exists='append', index = False)

data = pd.read_csv('tenant__id__campaign_finance_dl__fC__all__dda97a2bd63e1d051bd99f97ee6bfc39.csv')
data.to_sql('id_campaign_finance_expenditure', conn, if_exists='append', index = False)
