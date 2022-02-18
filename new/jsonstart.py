import json
import pandas as pd
from pprint import pprint

cuisins = pd.read_json('https://lms.skillfactory.ru/assets/courseware/v1/92fd198fd3eccc09a8c3498e9dd25588/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/recipes.json')

ml = list(cuisins['ingredients'].apply(lambda x: x))
all_ingredients = set()
for i in ml:
  for x in i:
      all_ingredients.add(x)
len(all_ingredients)

def contains(ingredients):
  if ing_name in ingredients:
    return 1
  else:
    return 0
    

for ing_name in check_list:
  cuisins[ing_name] = cuisins['ingredients'].apply(contains)
