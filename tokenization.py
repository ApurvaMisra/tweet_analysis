import numpy as np 
import pandas as pd
import seaborn as sns
import re
import nltk
from nltk.tokenize.casual import casual_tokenize
from nltk.util import ngrams
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sen="I know he gets knocked on a lot.But I like being un-sober and watching robots beat each other up. :)"
tokens=casual_tokenize(sen, reduce_len=True, strip_handles=True)
print(list(ngrams(tokens,2))) #Creates a generator
analyzer=SentimentIntensityAnalyzer()
#print(analyzer.lexicon)
print(analyzer.polarity_scores(text=sen))