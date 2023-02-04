import pandas as pd

titanic_df = pd.read_csv('https://stepik.org/media/attachments/course/4852/titanic.csv')
print(titanic_df.shape)
print(titanic_df.dtypes.value_counts())

dota_heroes_pd = pd.read_csv('https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv')
print(dota_heroes_pd[['legs', 'name']].groupby('legs').nunique())
loopa_pupa_pd = pd.read_csv('https://stepik.org/media/attachments/course/4852/accountancy.csv')
print(loopa_pupa_pd.groupby(['Executor', 'Type'], as_index=False).aggregate({'Salary': 'mean'}))
print(dota_heroes_pd.groupby(['attack_type', 'primary_attr']).count())
seaweed_pd = pd.read_csv('http://stepik.org/media/attachments/course/4852/algae.csv')
print(seaweed_pd)
mean_concentration = seaweed_pd.groupby('genus').aggregate({'sucrose': 'mean', 'alanin': 'mean',
                                                            'citrate': 'mean', 'glucose': 'mean', 'oleic_acid': 'mean'})
print(mean_concentration)
pd.options.display.float_format = '{:.2f}'.format
print(seaweed_pd.groupby('genus').aggregate({'alanin': ['min', 'mean', 'max']}).loc[['Fucus']])
group_groupby = seaweed_pd.groupby('group').aggregate({
    'sucrose': ['max', 'min'],
    'citrate': 'var'
})
group_groupby[('sucrose', 'sucrose_amplitude')] = group_groupby['sucrose']['max'] - group_groupby['sucrose']['min']
print(group_groupby.applymap('{:.2f}'.format))
print(group_groupby.columns)
dota2_df = pd.read_csv('https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv')
dota2_df['count_roles'] = [str(x).count(',') + 1 for x in dota2_df.roles]
dota2_df.drop(index=116, inplace=True)
print(dota2_df)
