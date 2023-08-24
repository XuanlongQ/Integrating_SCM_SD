import sys
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
            
def search_antonyms(val):
    Antomymsl_class_1_2 = "word_antonyms/AntonymsLexicon-OppCats-Affixes"
    antonym = []
    antonym.append(val)
    with open(Antomymsl_class_1_2,'r',encoding='utf-8') as f:
        for line in f:
            newline = line.strip().split(" ")
            if val == newline[0]:
                antonym.append(newline[1])
                #return val, newline[1]
            elif val == newline[1]:
                antonym.append(newline[0])
                #return val, newline[0]
            else:
                continue
    return antonym

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

def determine_pairs(antonymlist):
    antonymlist_arr = []
    for val in antonymlist:
        if val:
            vec_vector = word2vec_mce(val)
            antonymlist_arr.append(vec_vector)
        else:
            continue
    return antonymlist_arr

    

if __name__ == "__main__":
    original_file = "word_antonyms/scm_warm_low"
    with open(original_file,'r',encoding= 'utf-8') as f:
        for line in f:
            line = line.strip()
            try:
                antonymlist =  search_antonyms(line)
                print(antonymlist)
                determine_pairs(antonymlist)
            except Exception as err:
                print(" the err is: {} ".format(err))
            sys.exit(0)
    # 
    # val,val_antonym = search_antonyms()
    # if val and val_antonym:
    #     print(val, val_antonym)
    # else:
    #     print("Can not find {} !".format(val))