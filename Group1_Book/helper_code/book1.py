import re
import spacy
import urllib
import numpy as np
import pandas as pd

import cufflinks as cf
import IPython
from plotly.offline import init_notebook_mode
cf.go_offline()

colors20 = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', 
          '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', 
          '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

#to enable plotting in colab
def enable_plotly_in_cell():
    display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
  '''))
    init_notebook_mode(connected=False)
    
get_ipython().events.register('pre_run_cell', enable_plotly_in_cell)
    

nlp = spacy.load('en')



def get_book_df(chapters):
    book_df = pd.DataFrame(columns=["text", "part-of-speech","lemma","chapter"])
    for i in range(len(chapters)):
        chapter_tokens = nlp(chapters[i])
        for token in chapter_tokens:
             if ((token.pos_=="VERB") | (token.pos_=="NOUN") | (token.pos_=="ADJ") | (token.pos_== "PROPN")):
                    book_df = book_df.append({"text": token.text,
                             "part-of-speech":  token.pos_,
                             "lemma" : token.lemma_.strip().lower(),
                             "chapter": i+1
                              }, ignore_index=True)
    return book_df


def get_speechparts_by_chapter(book_df):
    result = book_df.groupby(["chapter", "part-of-speech"]).size().reset_index(name="count").\
                          pivot(index="chapter", columns='part-of-speech',values="count").reset_index().\
                          rename_axis(None,axis="columns").set_index("chapter")
    return result 

def get_counts(book_df, value):
    result = book_df.groupby(value).size().reset_index(name='count').set_index(value).sort_values(['count'], ascending=False)
    
    return result


def get_counts_by_chapters(book_df):
    result = book_df.groupby(["chapter", "lemma"]).size().reset_index(name="count").\
                                     pivot(index="chapter", columns='lemma',values="count").reset_index().\
                                    rename_axis(None,axis="columns").set_index("chapter")
    return result