def get_seed_words():
    import pandas as pd
    seedWords_path = '/Users/xuanlong/Documents/program/python/src/xuanlong/alg/css_word_embedding/stereotype/data/dictionary/osfstorage-archive/Dictionaries/Full Dictionaries.csv'

    df = pd.read_csv(seedWords_path,delimiter=',')
    print(df.shape)
    # reglion
    df['Belief'] = df.apply(lambda x: 0 if x['Religion dictionary'] + x['beliefs_other dictionary'] + x['Politics dictionary'] == 0 else 1,axis = 1)
    df['Geograpgy'] = df.apply(lambda x: 0 if x['inhabitant dictionary'] + x['country dictionary'] == 0 else 1,axis = 1)
    df['Appearance'] = df.apply(lambda x: 0 if x['clothing dictionary'] + x['body_property dictionary'] + x['body_part dictionary'] + x['skin dictionary'] + x['body_covering dictionary'] + x['beauty dictionary'] == 0 else 1,axis = 1) 
    df.to_csv('/Users/xuanlong/Documents/program/python/src/xuanlong/alg/Integrating_SCM_SD/bin/doc/external_study4/all.csv')

# get_seed_words()

import nltk
from nltk import word_tokenize
with open('/Users/xuanlong/Documents/program/python/src/xuanlong/alg/Integrating_SCM_SD/bin/doc/external_study4/geography.csv','r',encoding='utf-8') as f:
    for line in f:
        
        tokens = word_tokenize(line)
        tags = nltk.pos_tag(tokens)
        if tags[0][1] == 'JJ':
            with open('/Users/xuanlong/Documents/program/python/src/xuanlong/alg/Integrating_SCM_SD/bin/doc/external_study4/extra_pairs/geography.csv','a+',encoding='utf-8') as f:
                f.write(tags[0][0] + '\n')
                f.close()
            print (tags[0][0])
        else:
            continue
       