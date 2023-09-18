## Study 1: Constructing contrasting pairs in word embeddings
import numpy as np

def word2vec_mce(search_val):
    """search word and return its vector

    Args:
        search_val (str): the word you want to search

    Returns:
        array: np.array
    """

    word2vec_model = "word_embeddings/mce_vectors.txt"
    with open(word2vec_model,'r') as f:
        next(f)
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
            
def search_antonyms(target_word):
    Antomymsl_class_1_2 = "word_antonyms/AntonymsLexicon-OppCats-Affixes"
    antonym = []
    with open(Antomymsl_class_1_2,'r',encoding='utf-8') as f:
        for line in f:
            newline = line.strip().split(" ")
            if target_word == newline[0]:
                antonym.append(newline[1])

            elif target_word == newline[1]:
                antonym.append(newline[0])
                
            else:
                continue
    print(len(antonym))
    return target_word, antonym

def social_dis(a,b):
    """return cosine similarity

    Args:
        a (dataframe): _description_
        b (dataframe): _description_

    Returns:
        float64: cosine similarity
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
    antonymlist = set(antonymlist)
    
    while target_word in antonymlist:
        antonymlist.remove(target_word)
            
    antonymlist_dic = {}
    target_word_vec = word2vec_mce(target_word)
    for antonym in antonymlist:
        antonym_vec = word2vec_mce(antonym)
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
    print(f"\nPair with highest Cosine distance: {max_pair[0]} and {max_pair[1]} with similarity {max_sim:.2f}")
    print(f"Pair with lowest Cosine distance: {min_pair[0]} and {min_pair[1]} with similarity {min_sim:.2f}")
    
    return max_pair
    

def writeToFile(maxdistance_pair,original_file):
    o_file = original_file.split('/')[1]
    writepath = 'Integrating_SCM_SD/bin/output/contrusting_pairs_mce/' + o_file
    with open(writepath,'a+',encoding='utf-8') as file:
        file.write(maxdistance_pair[0]+','+ maxdistance_pair[1]+'\n')
        file.close()

if __name__ == "__main__":
    original_file = "/Users/xuanlong/Documents/program/python/src/xuanlong/alg/Integrating_SCM_SD/bin/doc/external_study4/extra_pairs/status.csv"
    o_file = original_file.split('/')[1]
    with open(original_file,'r',encoding= 'utf-8') as f:
        for line in f:
            line = line.strip()
            try:
                target_word, antonymlist =  search_antonyms(line)
                maxdistance_pair = determine_degree(target_word, antonymlist)
                writeToFile(maxdistance_pair,original_file)
                
            except Exception as err:
                print(" the err is: {} ".format(err))
            
