# -*- encoding: utf-8 -*-
'''
@file: study6.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 

# Supplementary- Measuring the accuracy of personality prediction
import numpy as np
import re

import matplotlib.pyplot as plt

good_intellectural = ['reliable','reserved','daring',
             'artistic', 'meditative', 'practical','cautious', 'serious','discriminating','intelligent','important',
             'imaginative','industrious','skillfull','determined','scientific','persistent','shrewd','critical','stern',
             'dominating','cold','unsociable','humorless','pessimistic','irritable','moody','unpopular','unsociable']
good_intellectural_stable = ["scientific","persistent","determined","skillful",
                             "industrious","intelligent","imaginative","discriminating","serious",
                             "important","cautious","daring","reserved","shrewd"]


good_social = ["warm","sociable","popular","happy","humorous","sentimental","sincere",
               "helpful","tolerant","modest","honest","reliable","naive",
               "reserved","artistic","meditative","cautious","practical","important","serious","intelligent","industrious",
               "skillful"]
good_social_stable = ["honest","modest","tolerant","helpful","sincere","reliable"]

bad_social = ["unsociable","shrewd","stern","critical","dominating","cold","humorless","pessimistic",
              "irritable","moody","unhappy","vain","finicky","boring",
              "unimaginative","dishonest","squeamish","insignificant",
              "superficial","wavering","irresponsible","wasteful","unintelligent",
              "foolish","impulsive","clumsy","frivolous"]
bad_social_stable = ["unhappy","vain","finicky","moody","unpopular",
                     "irritable","pessimistic","boring","unimaginative",
                     "humorless","unsociable","cold"]

bad_intellectural = ["unhappy","vain","finicky","boring",
              "unimaginative","dishonest","squeamish","insignificant",
              "superficial","wavering","irresponsible","wasteful","unintelligent",
              "foolish","impulsive","clumsy","frivolous","submissive","naive",
              "warm","sociable","popular","happy","humorous","sentimental","sincere",
               "helpful","tolerant","modest","honest"
              ]
bad_intellectural_stable = ["submissive","impulsive","naive",
                            "clumsy","frivolous","unintelligent","foolish",
                            "wasteful","insignificant","squeamish"]

def scm_semantic(search_val,model_name):
    """search word and return its vector

    Args:
        search_val (str): the word you want to search

    Returns:1
        array: np.array
    """
    if model_name == 'SD':
        model_embeddings = 'word_embeddings/SD_2D.bin'
    elif model_name == 'SCM':
        model_embeddings = 'word_embeddings/SCM_2D.bin'
    elif model_name == 'DPM':
        model_embeddings = 'word_embeddings/DPM_2D.bin'
    elif model_name == 'NEW':
        model_embeddings = 'word_embeddings/New2_2D.bin'
    elif model_name == 'DPM_indirect':
        model_embeddings = 'word_embeddings/DPM_2D_indirect.bin'
    else:
        print("Model is not exist! Please Check your path! ")
        
    with open(model_embeddings,'r') as f:
        try:
            for line in f:
                key = line.replace('"','').split(',')[0]
                if key == search_val:
                    dimension = np.array(re.findall(r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",line)).astype('float64')
                    return (key,dimension)
                else:
                    continue
        except IOError:
            print("Input errot check the line {}".format(line))
        
        except Exception as e:
            print('err is :',e )
            print(line + "can not found")



def plot_words(word_list):
    """
    Plots words with their corresponding 2D coordinates.
    
    Args:
    word_list (list of tuples): Each tuple contains a word (str) and its coordinates (tuple of two floats).
    """
    # Set up the plot
    plt.figure(figsize=(10, 6))
    
    # Loop through the list of words and coordinates
    for word, (x, y) in word_list:
        # Plot each point
        plt.scatter(x, y, marker='o', color='blue')
        # Annotate the point with the corresponding word
        plt.text(x + 0.1, y, word, fontsize=12, ha='left', va='center')

    # Set titles and labels
    plt.title('Word Vectors in 2D Space')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    
    # Show the plot
    plt.show()

def count_words_x_greater_than_zero(word_list):
    """
    Counts the number of words with an x-coordinate greater than 0.

    Args:
    word_list (list of tuples): Each tuple contains a word (str) and its coordinates (tuple of two floats).

    Returns:
    int: Number of words with x-coordinate greater than 0.
    """
    # Using a list comprehension to count
    count = sum(1 for _, (x, _) in word_list if x > 0)
    print("the number of words with x-coordinate greater than 0 is ",count)
    return count

def count_words_y_greater_than_zero(word_list):
    """
    Counts the number of words with a y-coordinate greater than 0.

    Args:
    word_list (list of tuples): Each tuple contains a word (str) and its coordinates (tuple of two floats).

    Returns:
    int: Number of words with y-coordinate greater than 0.
    """
    # Using a list comprehension to count
    count = sum(1 for _, (_, y) in word_list if y > 0)
    print("the number of words with y-coordinate greater than 0 is ",count)
    return count

def count_words_y_lower_than_zero(word_list):
    """
    Counts the number of words with a y-coordinate lower than 0.

    Args:
    word_list (list of tuples): Each tuple contains a word (str) and its coordinates (tuple of two floats).

    Returns:
    int: Number of words with y-coordinate lower than 0.
    """
    # Using a list comprehension to count
    count = sum(1 for _, (_, y) in word_list if y < 0)
    print("the number of words with y-coordinate lower than 0 is ",count)
    return count

def count_words_x_lower_than_zero(word_list):
    """
    Counts the number of words with an x-coordinate lower than 0.

    Args:
    word_list (list of tuples): Each tuple contains a word (str) and its coordinates (tuple of two floats).

    Returns:
    int: Number of words with x-coordinate lower than 0.
    """
    # Using a list comprehension to count
    count = sum(1 for _, (x, _) in word_list if x < 0)
    print("the number of words with x-coordinate lower than 0 is ",count)
    return count

if __name__ == '__main__':
    print("The length of good_intellectural is ",len(good_intellectural),len(good_intellectural_stable))
    print("The length of good_social is ",len(good_social),len(good_social_stable))
    print("The length of bad_social is ",len(bad_social),len(bad_social_stable))
    print("The length of bad_intellectural is ",len(bad_intellectural),len(bad_intellectural_stable))

    print("###################")
    
    model = 'DPM_indirect'
    print("the model is,",model)
    
    traits = [good_social,good_intellectural,bad_social,bad_intellectural]
    traits_stable = [good_social_stable,good_intellectural_stable,bad_social_stable,bad_intellectural_stable]
    
    for i in traits_stable:
        data = []
        for per in i:
            # print("the length of good_social is ",len(good_social))
            val = scm_semantic (per,model)
            if val is None:
                print(per)
            else:
                # print(val)
                data.append(val)
        if i == good_intellectural or i == good_intellectural_stable:
            print("The length of good_intellectural is ",len(data))
            count_words_y_greater_than_zero(data)
            
        elif i == good_social or i == good_social_stable:
            print("The length of good_social is ",len(data))
            count_words_x_greater_than_zero(data)
        elif i == bad_social or i == bad_social_stable:
            print("The length of bad_social is ",len(data))
            count_words_x_lower_than_zero(data)
        else:
            print("The length of bad_intellectural is ",len(data))
            count_words_y_lower_than_zero(data)
            
    # plot_words(data)