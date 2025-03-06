import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

print(ad_clicks.groupby('utm_source').user_id.count().reset_index())
ad_clicks['is_click'] = ~(ad_clicks.ad_click_timestamp.isnull())
print(ad_clicks.head())
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = ad_clicks.pivot_table(
  columns='is_click',
  index='utm_source',
  values='user_id',
  aggfunc='count'
).reset_index()
clicks_pivot.columns = ['utm_source', 'not_click', 'click']
#print(clicks_pivot)

clicks_pivot['percent_clicked'] = round(clicks_pivot['click'] / (clicks_pivot['click'] + clicks_pivot['not_click']), 2)

print(clicks_pivot)

clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

group_pivot = clicks_by_group.pivot(
  columns='is_click',
  index='experimental_group',
  values='user_id'
)
group_pivot.columns = ['not_click', 'click']
group_pivot['percent_clicked'] = round(group_pivot['click']/(group_pivot['click'] + group_pivot['not_click']), 2)
print(group_pivot)

a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A'].reset_index()
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B'].reset_index()
a_clicks = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_clicks = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
print(a_clicks)
print(b_clicks)