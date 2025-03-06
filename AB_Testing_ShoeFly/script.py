import codecademylib3
import pandas as pd

import codecademylib3
import pandas as pd

try:
    ad_clicks = pd.read_csv('ad_clicks.csv')
    print(ad_clicks.head())
except FileNotFoundError:
    print("The file 'ad_clicks.csv' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(ad_clicks.groupby('utm_source').user_id.count().reset_index())
ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].notnull()
print(ad_clicks.head())
clicksBySource = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicksBySource)

# Pivot the data to show the number of clicks and non-clicks for each utm_source
clicks_pivot = clicksBySource.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id',
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
a_clicks_pivot = a_clicks.pivot(
  columns='is_click',
  index='day',
  values='user_id'
).reset_index()
a_clicks_pivot['percent_clicked'] = round(a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False]), 2)

b_clicks_pivot = b_clicks.pivot(
  columns='is_click',
  index='day',
  values='user_id'
).reset_index()
b_clicks_pivot['percent_clicked'] = round(b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False]), 2)

print(a_clicks_pivot)
print(b_clicks_pivot)

# Compare the results and make a recommendation based on the percent_clicked values.
print(f'Based on the results, I would recommend experimental group A.')