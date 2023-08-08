import numpy as np
import csv
from lib import utils_fun,middleware,remain
from lib.middleware import word2vec_fun
import gensim

model_path = 'css_word_embedding/stereotype/GoogleNews-vectors-negative300.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(model_path,binary=True)


def normalize_vector(x):
    """Normalize vector

    Args:
        x (array): _description_

    Returns:
        array: _description_
    """
    return x/np.linalg.norm(x) 


Yamlcon = utils_fun.YamlConfig()
data_yaml = Yamlcon.get_yaml()

trustworthy_pairs_path = data_yaml["Trust"]["20_paris"]

anti_pairs = utils_fun.get_antonym_pairs(trustworthy_pairs_path)


word_dims = np.full((anti_pairs.shape[0], 300), np.nan) # create matrix
for _ in range(anti_pairs.shape[0]):
    print(_)
    rp_word_0 = anti_pairs[_,0]
    rp_word_1 = anti_pairs[_,1]
    try:
        rp_word_vec_0, rp_word_vec_1 = word2vec_fun(str(rp_word_0),str(rp_word_1))
        dimension = rp_word_vec_0 - rp_word_vec_1
        word_dims[_,] = normalize_vector(dimension)
    except Exception as err:
        print("something wrong, the err is{}".format(err))

new_dims= word_dims[~np.isnan(word_dims).any(axis=1), :]

curr_antonmy_vector = np.linalg.pinv(np.transpose(new_dims))
print(curr_antonmy_vector)   

vocab_list = model.index_to_key

for each_word in vocab_list:
    new_vector = np.matmul(curr_antonmy_vector,model[each_word])
    new_vector = new_vector/np.linalg.norm(new_vector)
    # with open('stereotype_scenario/trust_17.csv','a+',encoding='utf-8') as f:
    #     f.write(each_word + ',' + str(new_vector) + '\n')
    #     f.close()
    new_vector = [str(elem) for elem in new_vector]
    with open("output.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        row = [each_word] + new_vector
        writer.writerow(row)


