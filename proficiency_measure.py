import json
import pandas as pd
import numpy as np
from task_func import *
import zipfile
import warnings
warnings.filterwarnings("ignore")

archive = zipfile.ZipFile('data/github_profiles_samples.zip','r')
data = [json.loads(line) for line in archive.open('data/github_profiles_samples.jsonl')]
extra_keys = ('stars', 'forks') #assumes to be comparably important (stars and forks because they're assessed by other people.)

#Input User
user_id = str(input("Enter user id: "))
user = next((item for item in data if item['_id']['$oid'] == user_id), None)

#Data cleaning & preprocessing
repo_not_fork = list(filter(lambda x: 'isFork' in x.keys() and not x['isFork'], user['repos'])) #as an assumption that the repo is not forked from other's
repo_with_lang = list(filter(lambda x: 'name' and 'languages' in x.keys(), repo_not_fork)) #make sure  have language
repo_valid_lang = get_repo_lang(repo_with_lang) #get repo languages which have complete information : name of language and percentage

all_repo = []
for repo in repo_valid_lang:
  extra = extra_point(repo, extra_keys)
  for lang in repo['languages']:
    temp_repo = repo['name'], lang['name'], lang['percentage'], extra    
    all_repo.append(temp_repo)

df = pd.DataFrame(all_repo, columns=['name', 'language', 'percentage', 'extra_point'])
df

#Feature Engineering
df['freq'] = df.groupby('language')['language'].transform('count') #count languages frequency
df['final_point'] = df['percentage'] #initial point
df['final_point'][(df['extra_point'] > 20) & (df['extra_point'] < 50)  & (df['percentage']> 20 )] = df['percentage']*(1+(df['extra_point']/100)) #point for some people like it and language not very minor
df['final_point'][(df['extra_point'] >50) & (df['percentage']> 50 )] = 100 #many people like the work with the language as majority
df['final_point'][(df['freq'] < 5) & (df['extra_point'] < 10)] = 10 #not convincing since only 
df['final_point'][df['final_point']>100] = 100  #cap to 100
df['final_point'][(df['freq'] > 10) & (df['final_point'] < 75)] = 75 #compensation for being active
df['final_point'][df['freq'] > 20] = 100 #compensation for being having big portfolio

#Final calculation by averaging the final point
final_df = df.groupby('language').mean()
print_df = final_df.filter(['final_point'])
print_df = print_df.rename(columns={"final_point": "Proficiency (%)"})
print(print_df)





# #print all languages used by the user
# print("Available languages:")
# for i in final_df.index:
#     print(i)

# #print result
# input_language = str(input("Enter desired language: "))
# if input_language in final_df.index:
#   print("User ID: {}, Proficiency Level of {}: {}%".format(user_id, input_language, round(final_df.loc[input_language]['final_point']),1))
# else:
#   print("User {} does not have any portfolio in {}".format(user_id, input_language))