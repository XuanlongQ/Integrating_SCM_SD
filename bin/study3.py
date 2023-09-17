# Study3 Assessing the Semantic Significance of Opposition Dimensions in Word Embeddings

import re
import numpy as np
import matplotlib.pyplot as plt
# SCM
SCM_HW_HC = ['reliable','reserved','artistic', 'meditative','practical', 'important','industrious',  'cautious', 'serious','discriminating','intelligent', 'skillful', 'imaginative','scientific', 'determined'  ]
SCM_HW_LC = ['shrewd','honest','modest','tolerant','helpful','sincere','sentimental','humorous','good natured','happy','popular','sociable','warm','naive','submissive']
SCM_LW_HC = ['stern','critical','dominating','cold','unsociable','humorless','unpopular','pessimistic','irritable','moody','daring','persistent','unhappy','scientific','determined']                        
SCM_LW_LC = ['unhappy','vain','finicky', 'boring','unimaginative', 'dishonest', 'insignificant','superficial','squeamish','unintelligent', 'clumsy', 'impulsive','unreliable', 'foolish','frivolous', 'wasteful','wavering', 'irresponsible', 'submissive','naive']

# SD
SD_HW_HC = ['daring','reserved','discriminating','cautious','meditative','artistic','practical','serious','important','imaginative','persistent','scientific','determined','skillful','industrious','intelligent']
SD_HW_LC = ['shrewd','honest','modest','tolerant','helpful','sincere','sentimental','humorous','good natured','happy','popular','sociable','warm']
SD_LW_HC = ['stern','critical','dominating','cold','unsociable','humorless','unpopular','pessimistic','irritable','moody','unhappy','vain','finicky']                        
SD_LW_LC = ['unintelligent', 'clumsy', 'impulsive', 'unimaginative', 'unreliable', 'dishonest', 'insignificant', 'wavering', 'foolish', 'frivolous', 'submissive', 'irresponsible', 'naive', 'squeamish', 'superficial', 'wasteful', 'boring']


def scm_semantic(search_val,model_name):
    """search word and return its vector

    Args:
        search_val (str): the word you want to search

    Returns:
        array: np.array
    """
    if model_name == 'sd':
        model_embeddings = '/Users/xuanlong/Documents/program/python/src/xuanlong/alg/word_embeddings/SD_embedding_final.bin'
    elif model_name == 'scm':
        model_embeddings = '/Users/xuanlong/Documents/program/python/src/xuanlong/alg/word_embeddings/SCM_embedding_final.bin'
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
            
def find_groups():
    filePath = 'Integrating_SCM_SD/bin/doc/personality_traits.txt'
    groups = []
    with open(filePath,'r',encoding='utf-8') as fr:
        for line in fr:
            newline = line.rstrip().split(".")
            groups.append(newline[-1])
    return groups

def get_dimensions(groups,model_name):
    SCM_MAP = dict()
    for group in groups:
        val = scm_semantic(group,model_name)
        if val is None:
            print(group)
        else:
            try:
                if val[1][0] > 0 and val[1][1]> 0 :
                    if 'HW-HC' in SCM_MAP.keys():
                        SCM_MAP['HW-HC'].append(group)
                    else:
                        SCM_MAP['HW-HC'] = [group]
                        
                elif val[1][0] > 0 and val[1][1] < 0:
                    if 'HW-LC' in SCM_MAP.keys():
                        SCM_MAP['HW-LC'].append(group)
                    else:
                        SCM_MAP['HW-LC'] = [group]
                        
                elif val[1][0] < 0 and val[1][1] < 0:
                    if 'LW-LC' in SCM_MAP.keys():
                        SCM_MAP['LW-LC'].append(group)
                    else:
                        SCM_MAP['LW-LC'] = [group]
                        
                else:
                    if 'LW-HC' in SCM_MAP.keys():
                        SCM_MAP['LW-HC'].append(group)
                    else:
                        SCM_MAP['LW-HC'] = [group]
            except Exception as e:
                print(e)
        #print(SCM_MAP)
    return SCM_MAP
                      
def draw_pic(groups):
    warmth = []
    competent = []
    text =[]

    for g in groups:
        val = scm_semantic(g)
        print(val)
        if val == None:
            continue
        else:
            text.append(val[0])
            warmth.append(val[1][0])
            competent.append(val[1][1])


    plt.xlim((-1, 1))
    plt.ylim((-1, 1))
    plt.scatter(warmth, competent)
    for i in range(len(text)):
        plt.annotate(text[i], xy = (warmth[i], competent[i]), xytext = (warmth[i]-0.1, competent[i]+0.2))
    plt.grid()
    plt.show()

def test_scm_robustness(SCM_MAP):
    for item in SCM_MAP.keys():
        # print(item)
        if item == 'LW-LC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SCM_LW_LC:
                    T += 1
                else:
                    # print('lw-lc:',val)
                    continue
            print("LW-LC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        elif item == 'LW-HC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SCM_LW_HC:
                    T += 1
            print("LW-HC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        elif item == 'HW-LC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SCM_HW_LC:
                    T += 1
            print("HW-LC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        else:
            item == 'HW-HC'
            T = 0
            for val in SCM_MAP[item]:
                if val in SCM_HW_HC:
                    T += 1
                else:
                    continue
                    #print("hw-hc:",val)
            print("HW-HC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))

def test_sd_robustness(SCM_MAP):
    for item in SCM_MAP.keys():
        # print(item)
        if item == 'LW-LC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SD_LW_LC:
                    T += 1
                else:
                    # print('lw-lc:',val)
                    continue
            print("LW-LC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        elif item == 'LW-HC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SD_LW_HC:
                    T += 1
            print("LW-HC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        elif item == 'HW-LC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SD_HW_LC:
                    T += 1
            print("HW-LC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        else:
            item == 'HW-HC'
            T = 0
            for val in SCM_MAP[item]:
                if val in SD_HW_HC:
                    T += 1
                else:
                    continue
                    #print("hw-hc:",val)
            print("HW-HC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
           
if __name__ == '__main__':
    # groups = find_groups()   
    # 'high-strung','good natured' had lost 
    # all 64 personality traits.(actual 59)
    groups = ['determined', 'practical', 'industrious', 'intelligent', 'unintelligent', 'skillful', 'clumsy', 'cautious', 
              'impulsive', 'warm', 'cold', 'irritable',  'humorous', 'humorless', 'sociable', 'unsociable',
              'popular', 'unpopular', 'happy', 'unhappy', 'imaginative', 'unimaginative', 'reliable', 'unreliable', 'honest',
              'dishonest', 'important', 'insignificant', 'persistent', 'wavering', 'foolish', 'shrewd', 'critical', 'tolerant', 
              'serious', 'frivolous', 'vain', 'modest', 'submissive', 'irresponsible', 'sincere', 'helpful', 'sentimental',
              'naive', 'scientific', 'discriminating', 'squeamish', 'daring', 'superficial', 'moody', 'pessimistic', 'wasteful', 
              'stern', 'finicky', 'artistic', 'meditative', 'dominating', 'boring', 'reserved']
    
    #'inventive','liar','egotistical'
    # all 64 personality traits excluding ambiguous stereotype.(actual 39)
    groups_boarder = ['practical', 'industrious', 'intelligent', 'unintelligent', 'skillful', 'clumsy', 'cautious', 
              'impulsive', 'warm', 'cold',  'humorous', 'humorless', 'sociable', 'unsociable',
              'popular', 'happy',  'imaginative', 'unimaginative', 'reliable', 'unreliable', 
              'dishonest', 'important', 'insignificant',  'wavering',  'tolerant', 
              'serious',  'modest', 'irresponsible', 'sincere', 'helpful', 'sentimental',
              'squeamish',  'superficial',  'wasteful', 
               'artistic', 'meditative', 'dominating', 'boring', 'unpopular']
    # draw_pic(groups)
    print(len(groups),len(groups_boarder))
    
    # study3 scm
    scm_map = get_dimensions(groups_boarder,'scm')
    print(scm_map)
    test_scm_robustness(scm_map)
    
    # study3 sd
    sd_map = get_dimensions(groups_boarder,'sd')
    print(sd_map)
    test_sd_robustness(sd_map)
            

    


    




