## Study 1: Constructing contrasting pairs in word embeddings
import numpy as np
import yaml

# Global configration
config_file = "Integrating_SCM_SD/bin/conf/config.yaml" # the path of the config file
Antomymsl_file = "word_antonyms/AntonymsLexicon-OppCats-Affixes" # antonyms database
mce_model = "word_embeddings/mce_vectors.txt" # mce models


def word2vec_mce(mce_model,search_val):
    """search word and return its vector

    Args:
        search_val (str): the word you want to search

    Returns:
        array: np.array
    """

    with open(mce_model,'r') as f:
        next(f) # skip the first line
        try:
            for line in f:
                newline = line.split(" ")
                key = newline[0]           
                if key == search_val:
                    dimension = np.array(newline[1:-1]).astype('float64')
                    return dimension
                else:
                    continue
        except IOError:
            print("Input errot check the line {}".format(line))
        
        except Exception as e:
            print('err is :',e )
            print(line + "can not found")
            
def search_antonyms(Antomymsl_file,target_word):
    """search antonyms from the antonyms list

    Args:
        Antomymsl_list (str): the file of antonyms file
        target_word (str): seed word

    Returns:
        str: seed word
        list: antonyms list
    """
    antonyms = []
    with open(Antomymsl_file,'r',encoding='utf-8') as f:
        for line in f:
            newline = line.strip().split(" ")
            if target_word == newline[0]:
                antonyms.append(newline[1])
                
            elif target_word == newline[1]:
                antonyms.append(newline[0])
                
            else:
                continue
    print("there are {} antonyms for the word {}".format(len(antonyms),target_word))
    return target_word, antonyms

def social_dis(a,b):
    """return max distance

    Args:
        a (dataframe): _description_
        b (dataframe): _description_

    Returns:
        float64: 1- cosine_similarity
    """
    nominator = np.dot(a,b)

    a_norm = np.linalg.norm(a) 
    b_norm = np.linalg.norm(b)
    
    denominator = a_norm * b_norm
    
    cosine_similarity = nominator / denominator
    social_dis = 1- cosine_similarity
    return social_dis

def determine_degree(target_word,antonymlist):
    """Find the most contrusting meaning's pairs

    Args:
        target_word (string): the target word of pairs
        antonymlist (Array list): the antonym list of the target word.

    Returns:
        tuple: target word and the most contrusting word.
    """
   
    antonymlist_dic = {}
    target_word_vec = word2vec_mce(mce_model,target_word)
    
    for antonym in antonymlist:
        antonym_vec = word2vec_mce(mce_model,antonym)
        if antonym_vec is None:
            continue
        else:
            antonymlist_dic[antonym] = antonym_vec
            
    antonymlist_dic[target_word] = target_word_vec
    
    
    max_sim = 0
    min_sim = 2
    max_pair = None
    min_pair = None
    for item in antonymlist_dic.keys():
        if item is target_word:
            # remove the target word per se.
            continue
        else:
            sim = social_dis(antonymlist_dic[target_word],antonymlist_dic[item])
            # print(f"Cosine distance between '{target_word}' and '{item}': {sim:.2f}")
            if sim > max_sim:
                max_sim = sim
                max_pair = (target_word,item)
            if sim < min_sim:
                min_sim = sim 
                min_pair = (target_word,item)
    print(f"\nPair with highest Cosine distance: {max_pair[0]} and {max_pair[1]} with distance {max_sim:.2f}")
    print(f"Pair with lowest Cosine distance: {min_pair[0]} and {min_pair[1]} with distance {min_sim:.2f}")
    
    return max_pair
    
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
        with open(path_file,'r',encoding='utf-8') as f:
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

def writeToFile(contrasting_pair,task):
    """writing contrasting pairs to file

    Args:
        contrasting_pair (tuple): tuple of contrasting pairs
        task (str): the task of the contrasting pairs
    """
    contrasting_pair_path = get_file_path(config_file, ['contrasting_pairs',task])
    
    with open(contrasting_pair_path,'a+',encoding='utf-8') as file:
        file.write(contrasting_pair[0]+','+ contrasting_pair[1]+'\n')
        file.close()
    

if __name__ == "__main__":
    
    task_list = ['warmth_pairs','competent_pairs','communion_pairs','agency_pairs']
    
    for task in task_list:
        print(task)
        seed_path = get_file_path(config_file, ['word_pairs',task])
        contrasting_pair_path = get_file_path(config_file, ['contrasting_pairs',task])
        seed_words = get_seed_word(seed_path)
        print("this task is {} has {} seed words".format(task, len(seed_words)))   
        
        for seed_word in seed_words:
            target_word, antonymlist =  search_antonyms(Antomymsl_file,seed_word)
            contrasting_pair = determine_degree(target_word, antonymlist)
            writeToFile(contrasting_pair,task)
    