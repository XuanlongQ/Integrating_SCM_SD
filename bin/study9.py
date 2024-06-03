# -*- encoding: utf-8 -*-
'''
@file: study9.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 

# Constructing indirect from direct antonyms
# Only for DPM pairs, because QIN and TAM pairs are already indirect. As we need to comapre with them,
# I did not create a new one.

# the way I contrust the indirect antonyms is to find the direct antonyms of the direct antonyms of the target word,
# when we meet the first word that is not in the antonyms list, we stop and return the list.

import yaml
import numpy as np


# Global configration
config_file = "Integrating_SCM_SD/bin/conf/config.yaml" # the path of the config file
Antomymsl_file = "word_antonyms/AntonymsLexicon-OppCats-Affixes" # antonyms database
mce_model = "word_embeddings/mce_vectors.txt" # mce models

def get_file_path(yaml_file, keys):
    """get file path from config file

    Args:
        yaml_file (str): the path of the yaml file
        keys (list): the keys of the file path

    Returns:
        str: the file path
    """
    try:
        with open(yaml_file, 'r') as f:
            config = yaml.safe_load(f)
            file_path = config[keys[0]][keys[1]]
            return file_path
    except yaml.YAMLError as exc:
            print("YAML error:", exc)
    except KeyError as exc:
            print("Key error:", exc)
    except TypeError as exc:
            print("Type error, possibly due to incorrect keys:", exc)
    except Exception as exc:
            print("Error occurred:", exc)
            
def get_seed_word(path_file):
    """get seed word from file and delete the repeat word

    Args:
        path_file (str): the path of seed words

    Returns:
        list: seed word list
    """
    try:
        with open(path_file,'r',encoding='utf-8-sig') as f:
            antonym_list = []
            for line in f:
                line = line.strip()
                antonym_list.append(line)
            # remove the repeat word
            antonym_list = list(set(antonym_list))
            # sort these with alphabeta
            antonym_list.sort()
        return antonym_list
    except Exception as err:
        print(" the err is: {} ".format(err))
        return None


def search_antonyms(Antomymsl_file,target_word):
    """search antonyms from the antonyms list

    Args:
        Antomymsl_list (str): the file of antonyms file
        target_word (str): seed word

    Returns:
        str: seed word
    """
    with open(Antomymsl_file,'r',encoding='utf-8') as f:
        for line in f:
            newline = line.strip().split(" ")
            if target_word == newline[0]:
                return target_word, newline[1]
            elif target_word == newline[1]:
                return target_word, newline[0]        
            else:
                continue


def writeToFile(indirect_pair,task):
    """writing contrasting pairs to file

    Args:
        indirect_pair (tuple): tuple of contrasting pairs
        task (str): the task of the contrasting pairs
    """
    indirect_pair_path = get_file_path(config_file, ['indirect_pairs',task])
    
    with open(indirect_pair_path,'a+',encoding='utf-8') as file:
        file.write(indirect_pair[0]+','+ indirect_pair[1]+'\n')
        file.close()
        
if __name__ == "__main__":
    
    task_list = ['communion_pairs','agency_pairs']
    
    for task in task_list:
        print(task)
        seed_path = get_file_path(config_file, ['word_pairs',task])
        indirect_pair_path = get_file_path(config_file, ['indirect_pairs',task])
        
        seed_words = get_seed_word(seed_path)
        print("this task is {} has {} seed words".format(task, len(seed_words)))   
        seed_words.sort()
        print(seed_words,len(seed_words))
        
        for seed_word in seed_words[1:]:
            try:
                target_word, antonym =  search_antonyms(Antomymsl_file,seed_word)
                print(target_word, antonym)

                
                indirect_antonyms = (seed_word, antonym)
                if indirect_antonyms is not None:
                    writeToFile(indirect_antonyms,task)
                else:
                    print("indirect_pair is None")
            except Exception as err:
                print(" the err is: {} ".format(err))
                print("This word {} has no antonyms".format(seed_word))
                continue
        print("task {} is done".format(task))
    print("All tasks are done")
