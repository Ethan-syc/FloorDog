# coding: utf-8

# In[202]:


import numpy as np
import pandas as pd
import random

# In[80]:


men = pd.read_excel("/Users/shunli/Downloads/men_fin.xlsx")

# ## Split into Categories

# In[81]:


categories = list(men['category'].unique())

# In[244]:


top_jacket = ["jackets-coats", "jacket", 'peacoat', 'vest', 'cardigan', 'parka', 'raincoat', 'bomber',
              'harrington', 'puffer', 'coat', 'coatshirt', 'overshirt']

top_casual = ['pullover', 'shirts', 'sweaters', 'shirt', 'sweatershirt', 'hoodie', 'turtleneck', 'sweatshirt',
              'sweater']

bottom_casual = ['tights', 'pant', 'pants', 'shorts', 'sweatpants', 'denim', 'leggings', 'jeans', 'skirt']

full_body = ['jumpsuit', 'overalls']

top_formal = ['blazer', 'suits-blazers', 'suit', 'blazer', 'dickie']

bottom_formal = ['trousers', 'trouser', 'kilt']

# In[245]:


category_type = [("top_jacket", top_jacket), ("top_casual", top_casual),
                 ("bottom_casual", bottom_casual), ("full_body", full_body),
                 ("top_formal", top_formal), ("bottom_formal", bottom_formal)]

# In[197]:


missing_cat = list(set(categories) - set(top_jacket) - set(top_formal) - set(top_casual) - set(bottom_casual) -
                   set(bottom_formal) - set(full_body))

compatible_category = {'top_casual': bottom_casual + top_jacket, 'top_formal': bottom_formal,
                       'bottom_casual': top_casual + top_jacket, 'top_jacket': top_casual + bottom_casual + full_body,
                       'bottom_formal': top_formal + top_jacket, 'full_body': top_jacket}

# In[213]:


'''
@df is the dataframe,
@cat is the given category,
returns df of all compatible clothes based on the category 
'''


def filter_compatible_category(df, cat):
    return df[df['category'].isin(compatible_category[cat])]


# ## Adding Colors

# In[104]:


# read colors
with open("list_colors.txt") as f:
    color_names = f.read().splitlines()

f.close()

# In[99]:


men['color_word'] = ''

# In[105]:


for i in range(len(men)):
    if type(men['title'][i]) == str:
        title = men['title'][i].lower().split()
        for word in title:
            if word in color_names:
                men['color_word'][i] = word
                break
            men['color_word'][i] = title[0]

# In[269]:


men.to_csv('men_fin.csv')

# ## Categorize by Color

# In[172]:


color_categories = list(men['color_word'].unique())

# In[173]:


# pd.set_option('display.max_colwidth', -1)

# hard editing

# men.loc[493, 'color_word'] = 'black'


# In[186]:


compatible_color = {'brown': ['orange', 'beige', 'white', 'off-white'],
                    'off-white': color_categories, 'red': ['off-white', 'white', 'silver', 'navy', 'blue'],
                    'navy': ['off-white', 'white', 'blue', 'gold', 'tan', 'ivory'],
                    'blue': list(set(color_categories) - {'red', 'pink', 'orange'}),
                    'white': color_categories, 'purple': ['off-white', 'white', 'black', 'beige', 'khaki'],
                    'green': ['off-white', 'white', 'black', 'beige', 'khaki', 'tan'],
                    'black': color_categories,
                    'grey': list(set(color_categories) - {'black', 'grey', 'brown', 'yellow', 'ivory'}),
                    'beige': list(set(color_categories) - {'white', 'off-white', 'khaki', 'tan', 'beige'}),
                    'khaki': list(set(color_categories) - {'white', 'off-white', 'beige', 'tan', 'khaki'}),
                    'pink': ['white', 'off-white', 'black', 'blue', 'navy'],
                    'indigo': ['off-white', 'white', 'gold', 'tan', 'ivory'],
                    'tan': list(set(color_categories) - {'white', 'off-white', 'beige', 'khaki', 'tan'}),
                    'orange': ['blue', 'purple', 'off-white', 'white', 'black', 'beige'],
                    'multicolor': ['white', 'off-white', 'grey', 'blue', 'navy'],
                    'silver': list(set(color_categories) - {'white', 'off-white', 'beige', 'khaki', 'silver'}),
                    'yellow': ['navy', 'blue', 'black', 'indigo', 'off-white'],
                    'burgundy': ['grey', 'black', 'navy', 'blue', 'white', 'off-white'],
                    'gold': ['navy', 'blue', 'black', 'indigo', 'off-white'],
                    'bronze': ['navy', 'blue', 'black', 'indigo', 'off-white'],
                    'taupe': ['navy', 'blue', 'black', 'indigo', 'off-white', 'white'],
                    'transparent': color_categories,
                    'camel': ['black', 'blue', 'navy'],
                    'ivory': list(set(color_categories) - {'white', 'off-white', 'beige', 'khaki', 'ivory'}),
                    'tricolor': ['black', 'blue', 'grey']}


# In[270]:


# get clothes with compatable colors

def filter_comp_colors(df, cat):
    return df[df['color_word'].isin(compatible_color[cat])]


# ## running code

# In[271]:


''' input - user_category & user_color
output - index for compatable clothes'''

print("All possible categories are: ", categories)
print()
print("All possible colors are: ", color_categories)

# In[267]:


'''
@df is the dataframe, 
@user_category is the category of user clothing
@user_color is the color of the user clothing
@num_return is the number of results to be returned 

'''


def compatible_clothes(df, user_category, user_color, num_return):
    # checks which type of category
    for cat in category_type:
        if user_category in cat[1]:
            # all clothes of compatible category
            compatible_cat_df = filter_compatible_category(df, cat[0])
            break

            # all clothes of compatible colors
    compatible_colors_df = filter_comp_colors(compatible_cat_df, user_color)
    print(type(compatible_cat_df))

    return [int(i) for i in compatible_colors_df.sample(num_return)['id']]


# In[268]:


if __name__ == "__main__":
    # SAMPLE RUN
    print(compatible_clothes(men, 'pants', 'brown', 10))

    # compatible_clothes(df, user_category, user_color, num_return)

