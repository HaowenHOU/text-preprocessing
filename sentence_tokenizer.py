# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 01:15:51 2018

@author: Administrator
"""


def tokenize_sentence(text, punctuation_list='!！?？.。', keep_token='"“'):
    """
    split sentence according to punctuation list
    """
    sentence_set = []
    inx_position = 0         #索引标点符号的位置
    char_position = 0        #移动字符指针位置
    for char in text:
        char_position += 1
        if char in punctuation_list:
            next_char = list(text[inx_position:char_position+1]).pop()
            if next_char not in punctuation_list:
                if next_char not in keep_token:
                    sentence_set.append(text[inx_position:char_position].strip())
                    inx_position = char_position
                else:
                    sentence_set.append(text[inx_position:char_position+1].strip())
                    inx_position = char_position+1
            
    if inx_position < len(text):
        sentence_set.append(text[inx_position:].strip())

    return sentence_set