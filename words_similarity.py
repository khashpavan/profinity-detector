# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:01:02 2021

@author: Khasha Pavan Kalyan
"""

# =============================================================================
# Task:
#     Write a program that can indicate the degree of profanity for each sentence in the file.
#     
#     Changes: profanity -->relativity ex:food related.
# =============================================================================

#***************Approach 1******************************
#Using a built library
from profanity_check import  predict_prob


predict_prob(['predict_prob() takes an array and returns the probability each string is offensive'])
# [0.08686173]

predict_prob(['go to hell, you scum'])
# [0.7618861]



#***************Approach 2******************************
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
#Using nltk for words and stop words

#importing files
with open("bad_words.txt") as bad_words_file,open("tweets.txt") as tweets_file:
    bad_words=bad_words_file.read().split('\n')
    tweets=tweets_file.readlines()
    for tweet in tweets:
        # split into words
        
        tokens = word_tokenize(tweet)
        # convert to lower case
        tokens = [w.lower() for w in tokens]
        # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        c=0
        for word in words:
            if word in bad_words:
                c+=1
        #Using traditional percentage method
        print(str(c*100/len(words))+ " %")