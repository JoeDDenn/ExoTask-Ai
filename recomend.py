import pandas as pd
import neattext.functions as nf
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recommeded(user_desc):
    df = pd.read_csv('data.csv')
    df

    df.loc[len(df.index)] = [999999, '', user_desc]

    df.drop_duplicates(inplace=True)
    df

    l = len(df.index)
    x = pd.Series(data=range(11604))
    df.sort_index()

    df.drop(df[df['description'].isna() == True].index, axis=0, inplace=True)
    df['clean_desc'] = df['description'].apply(nf.remove_stopwords)
    df['clean_desc'] = df['description'].apply(nf.remove_special_characters)
    cv = CountVectorizer()
    cv_m = cv.fit_transform(df['clean_desc'])
    cv_m.toarray()
    df_cv_m = pd.DataFrame(cv_m.toarray(), columns=cv.get_feature_names_out())
    df_cv_m
    cos_sim_m = cosine_similarity(cv_m)
    cos_sim_m
    desc_index = pd.Series(df.index, index=df['description']).drop_duplicates()
    desc_index

    index = len(desc_index) - 1
    index

    cos_sim_m[index]
    scores = list(enumerate(cos_sim_m[index]))
    scores
    sorted_score = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_score
    sorted_score[:5]

    sorted_indices = [i[0] for i in sorted_score[1:]]
    sorted_indices
    sorted_values = [i[1] for i in sorted_score[1:]]
    sorted_values
    recommeded = df.iloc[sorted_indices]
    recommeded

    import numpy as np
    recommeded['similarity_score'] = np.array(sorted_values)
    recommeded
    return (recommeded[['similarity_score', 'Url', 'description']][:5])


"""

# call the ipynb 

import os

# get the path of the current file
current_path = os.path.dirname(os.path.abspath(__file__))
# get the path of the ipynb file
ipynb_path = os.path.join(current_path, 'recommender_system.ipynb')
# call the ipynb file
os.system('jupyter nbconvert --to script ' + ipynb_path)
# get the path of the py file
py_path = os.path.join(current_path, 'recommender_system.py')
# call the py file
os.system('python ' + py_path + "web app to conbert link to qr code")


"""
