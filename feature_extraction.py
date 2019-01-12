#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 23:50:18 2019

@author: abhijithneilabraham
"""

from sklearn.feature_extraction import DictVectorizer #vectorizing dictionaries .Dictionaries have {} symbols.
onehot_encoder=DictVectorizer()
instances=[{'city':'Trivandrum'},{'city':'Aluva'},{'city':'Eranakulam'}]
print(onehot_encoder.fit_transform(instances).toarray())
'''
corpus

A collection of documents is called a corpus
'''
corpus={'I am programming right now','I love my life'}
from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
print(vectorizer.fit_transform(corpus).todense())