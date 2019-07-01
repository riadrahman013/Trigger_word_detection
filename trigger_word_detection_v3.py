# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:03:33 2018

@author: some_random_user
"""

import csv

lr_intr = lambda l, r: list(set(l).intersection(r))

string = 'the absence of  Marshal Department Marshal virginbreaker is the kind of addicting shits that keeps the Department wreaked'
lwords = string.split()
print('\nInput: {}'.format(string))
print('\nTotal number of words: {}'.format(len(lwords)))

negative_words_list = []
with open('negative_words.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for words in csv_reader:
        negative_words_list += words

negative_words = lr_intr(lwords, negative_words_list)

negative_words_count = len(negative_words)
for word1 in negative_words:
    count = 0
    for word2 in lwords:
        if word1 == word2:
            count = count + 1
    negative_words_count = negative_words_count + (count - 1)
    print('\nNegative word: {one}, Number of instances: {two}'.format(one = word1, two = count))
    
print('\nNumber of negative words detected: {}'.format(negative_words_count))

threat_words_list = []
with open('threat_words.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for words in csv_reader:
        threat_words_list += words

threat_words = lr_intr(lwords, threat_words_list)

threat_words_count = len(threat_words)
for word1 in threat_words:
    count = 0
    for word2 in lwords:
        if word1 == word2:
            count = count + 1
    threat_words_count = threat_words_count + (count-1)
    print('\nThreat word: {one}, Number of instances: {two}'.format(one = word1, two = count))

print('\nNumber of threatening words detected: {}'.format(threat_words_count))

percentage = (threat_words_count/len(lwords))*100
alert = ''
if percentage <= 30:
    alert = 'NO THREAT'
elif percentage <= 40:
    alert = 'LOW THREAT'
elif percentage <= 50:
    alert = 'MILD THREAT'
else:
    alert = 'HIGH THREAT'
print('\nPercentage of threat: {one}% [{two}]'.format(one = percentage, two = alert))

profane_words_list = []
with open('profane_words.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for words in csv_reader:
        profane_words_list += words

profane_words = lr_intr(lwords, profane_words_list)

profane_words_count = len(profane_words)
for word1 in profane_words:
    count = 0
    for word2 in lwords:
        if word1 == word2:
            count = count + 1
    profane_words_count = profane_words_count + (count - 1)
    print('\nProfane word: {one}, Number of instances: {two}'.format(one = word1, two = count))    

print('\nNumber of profane words detected: {}'.format(profane_words_count))
percentage = (profane_words_count/len(lwords))*100
print('\nPercentage of profanity: {}%'.format(percentage))



