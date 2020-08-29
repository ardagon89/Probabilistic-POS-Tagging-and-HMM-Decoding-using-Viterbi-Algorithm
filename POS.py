#!/usr/bin/env python
# coding: utf-8

# In[12]:


def get_uni_bi_grams(filename):
    file1 = open(filename,"r")
    tagslist = []
    wordslist = []
    word_has_tags = {}
    for line in file1.readlines():
        token_arr = line.split()
        tagslist.append(['<s>']+[token.split('_')[1] for token in token_arr]+['</s>'])
        wordslist.append([token.split('_')[0] for token in token_arr])
        for token in token_arr:
            word_tag = token.split('_')
            if word_tag[0] in word_has_tags:
                if word_tag[1] not in word_has_tags[word_tag[0]]:
                    word_has_tags[word_tag[0]].append(word_tag[1])
            else:
                word_has_tags[word_tag[0]] = [word_tag[1]]

    return wordslist, tagslist, word_has_tags

def get_unigram_count(wordslist):
    unigram_count = {}
    total_tokens = 0
    for line in wordslist:
        for word in line:
            if word not in unigram_count:
                unigram_count[word] = 1
            else:
                unigram_count[word] += 1
        total_tokens += len(line)
        
    return unigram_count, total_tokens

def get_WT_bigram_count(wordslist, tagslist):
    tags_bigram = {}
    word_tag_bigram = {}
    for line in tagslist:
        for i in range(1, len(line)):
            if (line[i-1], line[i]) not in tags_bigram:
                tags_bigram[(line[i-1], line[i])] = 1
            else:
                tags_bigram[(line[i-1], line[i])] += 1
                
    for line in range(len(wordslist)):
        for i in range(len(wordslist[line])):
            if (wordslist[line][i], tagslist[line][i+1]) not in word_tag_bigram:
                word_tag_bigram[(wordslist[line][i], tagslist[line][i+1])] = 1
            else:
                word_tag_bigram[(wordslist[line][i], tagslist[line][i+1])] += 1
    
    return tags_bigram, word_tag_bigram

def get_WT_bigram_prob(tags_bigram, word_tag_bigram, unigram_count):
    tags_prob = {}
    word_tag_prob = {}
    
    for key in tags_bigram:
        tags_prob[key] = tags_bigram[key]/unigram_count[key[0]]
        
    for key in word_tag_bigram:
        word_tag_prob[key] = word_tag_bigram[key]/unigram_count[key[1]]
        
    return tags_prob, word_tag_prob

def find_sentence_prob(sentence, tags_prob, word_tag_prob, word_has_tags, probs, prev_tag, result):
    while len(sentence)>0 and len(word_has_tags[sentence[0]]) == 1:
        result.append(sentence[0]+'_'+word_has_tags[sentence[0]][0])
        if (sentence[0],word_has_tags[sentence[0]][0]) in word_tag_prob and (prev_tag, word_has_tags[sentence[0]][0]) in tags_prob:
            probs *= word_tag_prob[(sentence[0],word_has_tags[sentence[0]][0])]
            probs *= tags_prob[(prev_tag, word_has_tags[sentence[0]][0])]
        else:
            probs = 0
        prev_tag = word_has_tags[sentence[0]][0]
        sentence = sentence[1:]
    if len(sentence)==0:
        if (prev_tag, '</s>') in tags_prob:
            probs *= tags_prob[(prev_tag, '</s>')]
        else:
            probs = 0
        return probs, result
    else:
        max_prob = -1
        for cur_tag in word_has_tags[sentence[0]]:
            if (sentence[0],cur_tag) in word_tag_prob and (prev_tag, cur_tag) in tags_prob:
                temp_prob, temp_result = find_sentence_prob(sentence[1:], tags_prob, word_tag_prob, word_has_tags, 
                                               probs*word_tag_prob[(sentence[0],cur_tag)]*tags_prob[(prev_tag, cur_tag)],
                                               cur_tag, result+[sentence[0]+'_'+cur_tag])
                if temp_prob > max_prob:
                    max_prob = temp_prob
                    new_result  = temp_result
        return max_prob, new_result
        
def get_prob_table(filename):
    result = {}
    file1 = open(filename,"r")
    for i, line in enumerate(file1.readlines()):
        if i==0:
            tags = line.rstrip().split(',')
        else:
            for j, word in enumerate(line.rstrip().split(',')):
                if j==0:
                    prev = word
                else:
                    result[(prev,tags[j])] = float(word)
    return result, tags[1:]

def get_sentence_prob(sentence, tags, trans_tab, obser_tab):
    calc_tab = []
    for word in sentence:
        col = []
        for tag in tags:
            if len(calc_tab)==0:
                col.append([1*trans_tab[('<s>',tag)]*obser_tab[(tag,word)], -1, '<s>', tag, word])
            else:
                max_prob = -1
                cell = []
                for x, item in enumerate(calc_tab[-1]):
                    temp_prob = item[0]*trans_tab[(tags[x],tag)]*obser_tab[(tag,word)]
                    if temp_prob > max_prob:
                        max_prob = temp_prob
                        cell = [temp_prob, x, tags[x], tag, word]
                col.append(cell)
        calc_tab.append(col)
    
    print(''.rjust(3), end='')
    for y in sentence:
        print(y.rjust(24), end='')
    print()
    for x,tag in enumerate(tags):
        print(tag.rjust(3), end='')
        for row in calc_tab:
            print(str(row[x][0]).rjust(24), end='')
        print()
        
    max_index = np.argmax([subrow[0] for subrow in calc_tab[-1]])
    print('The probability of the below POS sequence is :', calc_tab[-1][max_index][0])
    result = []
    print_arr = []
    for row in reversed(calc_tab):
        result.append(row[max_index][4]+'_'+row[max_index][3])
        max_index = row[max_index][1]
    return result[::-1]

def print_probs(tags, tags_prob, word_tag_prob):
    prev = '<s>'
    for token in tags:
        word, tag = token.split('_')
        if (word, tag) in word_tag_prob:
            print(str((word, tag)).ljust(15), str(word_tag_prob[(word, tag)]).ljust(25))
        else:
            print(str((word, tag)).ljust(15), str(0).ljust(25))
        if (prev, tag) in tags_prob:
            print(str((tag, prev)).ljust(15), str(tags_prob[(prev, tag)]).ljust(25))
        else:
            print(str((tag, prev)).ljust(15), str(0).ljust(25))
        prev = tag
    if (prev, '</s>') in tags_prob:
        print(str((prev, '</s>')).ljust(15), str(tags_prob[(prev, '</s>')]).ljust(25))
    else:
        print(str((prev, '</s>')).ljust(15), str(0).ljust(25))
        
if __name__ == '__main__':
    import sys
    import numpy as np
    if len(sys.argv) == 1:
        print('Naive Bayes Classification:')
        wordslist, tagslist, word_has_tags = get_uni_bi_grams("NLP6320_POSTaggedTrainingSet-Windows.txt")
        unigram_count, total_tokens = get_unigram_count(tagslist)
        tags_bigram, word_tag_bigram = get_WT_bigram_count(wordslist, tagslist)
        tags_prob, word_tag_prob = get_WT_bigram_prob(tags_bigram, word_tag_bigram, unigram_count)
        sentence  = "John went to work .".split()
        prob, tags = find_sentence_prob(sentence, tags_prob, word_tag_prob, word_has_tags, 1, '<s>', [])
        print_probs(tags, tags_prob, word_tag_prob)
        print(' '.join(tags))
        print('The probability of the above sentence is :',prob)
        
        print('-'*100)
        
        print('HMM Viterbi Algorithm:')
        trans_tab, tags = get_prob_table('Transition_Table.csv')
        obser_tab, _ = get_prob_table('Observation_Table.csv')
        sentence = "Janet will back the bill".split()
        POS_tags = get_sentence_prob(sentence, tags, trans_tab, obser_tab)
        print(' '.join(POS_tags))
        print()
        sentence = "will Janet back the bill".split()
        POS_tags = get_sentence_prob(sentence, tags, trans_tab, obser_tab)
        print(' '.join(POS_tags))
        print()
        sentence = "back the bill Janet will".split()
        POS_tags = get_sentence_prob(sentence, tags, trans_tab, obser_tab)
        print(' '.join(POS_tags))
        
    elif len(sys.argv) == 2:
        print('Naive Bayes Classification:')
        wordslist, tagslist, word_has_tags = get_uni_bi_grams(sys.argv[1])
        unigram_count, total_tokens = get_unigram_count(tagslist)
        tags_bigram, word_tag_bigram = get_WT_bigram_count(wordslist, tagslist)
        tags_prob, word_tag_prob = get_WT_bigram_prob(tags_bigram, word_tag_bigram, unigram_count)
        sentence  = "John went to work .".split()
        prob, tags = find_sentence_prob(sentence, tags_prob, word_tag_prob, word_has_tags, 1, '<s>', [])
        print_probs(tags, tags_prob, word_tag_prob)
        print(' '.join(tags))
        print('The probability of the above sentence is :',prob)
        
        print('-'*100)
        
        print('HMM Viterbi Algorithm:')
        trans_tab, tags = get_prob_table('Transition_Table.csv')
        obser_tab, _ = get_prob_table('Observation_Table.csv')
        sentence = "Janet will back the bill".split()
        POS_tags = get_sentence_prob(sentence, tags, trans_tab, obser_tab)
        print(' '.join(POS_tags))
        print()
        sentence = "will Janet back the bill".split()
        POS_tags = get_sentence_prob(sentence, tags, trans_tab, obser_tab)
        print(' '.join(POS_tags))
        print()
        sentence = "back the bill Janet will".split()
        POS_tags = get_sentence_prob(sentence, tags, trans_tab, obser_tab)
        print(' '.join(POS_tags))
    elif len(sys.argv) == 3:
        print('Enter correct input')
    elif len(sys.argv) == 4:
        if sys.argv[2] == 'NB':
            wordslist, tagslist, word_has_tags = get_uni_bi_grams(sys.argv[1])
            unigram_count, total_tokens = get_unigram_count(tagslist)
            tags_bigram, word_tag_bigram = get_WT_bigram_count(wordslist, tagslist)
            tags_prob, word_tag_prob = get_WT_bigram_prob(tags_bigram, word_tag_bigram, unigram_count)
            sentence  = sys.argv[3].split()
            prob, tags = find_sentence_prob(sentence, tags_prob, word_tag_prob, word_has_tags, 1, '<s>', [])
            print_probs(tags, tags_prob, word_tag_prob)
            print(' '.join(tags))
            print('The probability of the above sentence is :',prob)
        elif sys.argv[2] == 'HMM':
            trans_tab, tags = get_prob_table('Transition_Table.csv')
            obser_tab, _ = get_prob_table('Observation_Table.csv')
            sentence = sys.argv[3].split()
            POS_tags = get_sentence_prob(sentence, tags, trans_tab, obser_tab)
            print(' '.join(POS_tags))
        else:
            print('Enter correct input')