import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import itertools
from sklearn.preprocessing import MultiLabelBinarizer
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


def get_repo_lang(repo_with_lang):
  for repo in repo_with_lang:
    for lang in repo['languages']:
      if len(lang.keys()) != 2:
        repo['languages'].remove(lang)
    if len(repo['languages']) == 0:
      repo_with_lang.remove(repo)
  return repo_with_lang

def extra_point(repo, extra_keys):
  temp_val = []
  for key in extra_keys:
    if key in repo.keys():
      temp_val.append(repo.get(key))
  extra = max(temp_val)
  return extra

def get_language(data):
  user_data = {}
  for user in data:
    id = user['_id']
    id = id['$oid']
    language_used = set()
    repo_list = user['repos']
    for repo in repo_list:
      if 'languages' in repo.keys():
        langs = repo['languages']
        for langs_indiv in langs:
          if 'name' in langs_indiv.keys(): #some of the repos don't have name
            langs_name = langs_indiv['name']
            language_used.add(langs_name)
    language_split = list(language_used)
    user_data[id] = language_split
  return user_data

def countable_lang(data_dict):
  dict_val = list(data_dict.values()) #results in list of lists
  all_language = list(itertools.chain(*dict_val)) #flatten the list
  return all_language

def most_used_language(data, highest_num):
  counted = Counter(data)
  return counted.most_common(highest_num) #return list of highest_num tuples(language, language_count) 

def calculate_language_percentage(data, user_data_dict):
  language_percentage = []
  for i, j in data:
    percent = round(j/len(user_data_dict)*100, 2)
    language_percentage.append((i,percent))
  return language_percentage

def visualize_language_percentage(data):
  data = data
  data.sort(key=lambda x: x[1])

  language = list(zip(*data))[0]
  percentage = list(zip(*data))[1]
  y_pos = np.arange(len(language))

  plt.barh(y_pos, percentage)
  plt.yticks(y_pos, language)
  plt.title('{} Most used language'.format(len(y_pos)))

  plt.show()

def percentage_use(lang, countable_lang, user_data_dict):
  lang_count = countable_lang.count(lang)/len(user_data_dict)*100
  return round(lang_count,2)

def to_user_lang_df(data):
  mlb = MultiLabelBinarizer()
  idx = pd.Series(data)
  df = pd.DataFrame(mlb.fit_transform(idx), columns= mlb.classes_, index = idx.index)
  return df

def get_redundant_pairs(df):
  '''Get diagonal and lower triangular pairs of correlation matrix'''
  pairs_to_drop = set()
  cols = df.columns
  for i in range(0, df.shape[1]):
      for j in range(0, i+1):
          pairs_to_drop.add((cols[i], cols[j]))
  return pairs_to_drop

def get_top_abs_correlations(df, n=15):
  au_corr = df.corr().abs().unstack()
  labels_to_drop = get_redundant_pairs(df)
  au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
  return au_corr[0:n]

def visualize_correlated_pair(df, lang_pair):
  set_index = list(set([element for pair in lang_pair.index for element in pair])) #take the set of languages
  new_user_df = df.filter(set_index, axis=1)
  plt.figure(figsize=(8,6))
  ax = sns.heatmap(new_user_df.corr())