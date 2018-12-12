import numpy as np
import pandas as pd
import random

women_path = "datasets/women_complete_coding.csv"
men_path = "datasets/men_complete_coding.csv"

women = pd.read_csv(women_path)
men = pd.read_csv(men_path)

################################################################## Categories

top_jacket = ["jackets-coats", "jacket", 'peacoat', 'vest', 'cardigan', 'parka', 'raincoat', 'bomber', 
             'harrington', 'puffer', 'coat', 'coatshirt', 'overshirt', 'poncho', 'trenchcoat',
             'overcoat']

top_casual = ['pullover', 'shirts', 'sweaters', 'shirt', 'sweatershirt', 'hoodie', 'turtleneck', 'sweatshirt',
             'sweater', 'top', 'crewneck', 'tops']

bottom_casual = ['tights', 'pant', 'pants', 'shorts', 'sweatpants', 'denim', 'leggings', 'jeans', 'skirt',
                'miniskirt', 'skort', 'skirts', 'minskirt']

full_body = ['jumpsuit', 'overalls', 'dress', 'bodysuit', 'dresses', 'jumpsuits']

top_formal = ['blazer', 'suits-blazers', 'suit', 'blazer', 'dickie', 'polo', 'blouse']

bottom_formal = ['trousers', 'trouser', 'kilt']

category_type = [("top_jacket", top_jacket), ("top_casual", top_casual), 
                 ("bottom_casual", bottom_casual), ("full_body", full_body), 
                 ("top_formal", top_formal), ("bottom_formal", bottom_formal)]


compatible_category = {'top_casual':bottom_casual + top_jacket, 'top_formal':bottom_formal, 'bottom_formal':top_formal,
              'bottom_casual':top_casual + top_jacket, 'top_jacket':top_casual + bottom_casual + full_body,
              'bottom_formal':top_formal + top_jacket, 'full_body':top_jacket}

men_classes = ['jackets-coats', 'jeans', 'pants', 'shirts', 'shorts', 'suits-blazers', 'sweaters']
women_classes = ['dresses', 'jackets-coats', 'jeans', 'jumpsuits', 'pants', 'shorts', 'skirts', 'sweaters', 'tops']


# filter same category 
def filter_same_category(df, cat):
    
    for cati in category_type: 
        if cat in cati[1]:
            return df[df['category'].isin(cati[1])]



################################################################## Colors
def hex_to_rgb(hexi):
    
    if not hexi:
        return (0, 0, 0)
    
    if type(hexi) != str:
        return (0, 0, 0)
    
    h = hexi.lstrip('#')
    (r,g,b) = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    return (r,g,b)

def convert_hex_column(df):
    
    for i in range(len(df)):
        
        df['color1'][i] = hex_to_rgb(df['color1'][i])
        df['color2'][i] = hex_to_rgb(df['color2'][i])
        df['color3'][i] = hex_to_rgb(df['color3'][i])
            
    return df


'''
@param are hex colors and the df I want to compare to 
returns index of article of clothing with most similar color 
'''


def similar_color(color1, color2, color3, df):
    
    input1 = hex_to_rgb(color1)
    input2 = hex_to_rgb(color2)
    input3 = hex_to_rgb(color3)
    user_color = [input1, input2, input3]
    
    global_min = 765 
    most_similar = 0 
    
    for i, row in df.iterrows():
    
        row_index = df.loc[i]['id']
        total_closeness = 0
        
        for color in user_color: 
#             print("this is color: ", color)

                     
            # compare reds for each color 
            diff_red = [abs(color[0] - df.loc[i]['color1'][0])
                        , abs(color[0] - df.loc[i]['color2'][0]), abs(color[0] - df.loc[i]['color3'][0])]
            diff_blue = [abs(color[1] - df.loc[i]['color1'][1]), abs(color[1] - df.loc[i]['color2'][1])
                         , abs(color[1] - df.loc[i]['color3'][1])]
            diff_green = [abs(color[2] - df.loc[i]['color1'][2]), 
                          abs(color[2] - df.loc[i]['color2'][2]), abs(color[2] - df.loc[i]['color3'][2])]
            
            # sum of differences, where each index corresponds with a color 
            total_diff = [sum(i) for i in zip(diff_red, diff_blue, diff_green)]
            
            # index of closest color
            # closest_color = total_diff.index(min(total_diff))
            
            # add difference of closest color to total_closeness
            total_closeness += min(total_diff)
            
        if total_closeness < global_min:
            global_min = total_closeness
            most_similar = row_index 
    
    
    return most_similar 


################################################################## Fin

'''
@gender is either Female or Male
'''

def recommendation_similar(gender, user_category, color1, color2, color3):
    
    df = pd.read_csv('men_complete_coding.csv')
    
    if gender == 'Female':
        df = pd.read_csv("women_complete_coding.csv")
    
    # all clothes of similar broad category  
    compatible_cat_df = filter_same_category(df, user_category)
    
    index_similar = similar_color(color1, color2, color3, compatible_cat_df)
    
    return (df.loc[index_similar]['comp1'], df.loc[index_similar]['comp2'], df.loc[index_similar]['comp3'])






if __name__ == '__main__':
	recommendation_similar(men, "pants", '#C0C0C0', '#903B29', '#38211D')






