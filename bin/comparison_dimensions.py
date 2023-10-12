from lib.remain import cosine_similarity
from lib import utils_fun
import numpy as np
import matplotlib.pyplot as plt

Yamlcon = utils_fun.YamlConfig()
data_yaml = Yamlcon.get_yaml()


def calculate_each_two(vectors):
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            similarity = cosine_similarity(vectors[i], vectors[j])
            print(f"The cosine similarity between vector {i+1} and vector {j+1} is {similarity:.2f}")


def heat_map(vectors,METHOD):
    # Compute the cosine similarity matrix
    similarities = np.dot(vectors, vectors.T) / (np.linalg.norm(vectors, axis=1) * np.linalg.norm(vectors, axis=1)[:, np.newaxis])

    # Plot the heatmap
    fig, ax = plt.subplots()
    im = ax.imshow(similarities)

    # Set the tick labels
    ax.set_xticks(np.arange(len(vectors)))
    ax.set_yticks(np.arange(len(vectors)))
    ax.set_xticklabels(["warmth", "competent", "evaluation", "potency", "activity"])
    ax.set_yticklabels(["warmth", "competent", "evaluation", "potency", "activity"])

    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over the data and add text annotations
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            text = ax.text(j, i, "{:.2f}".format(similarities[i, j]), ha="center", va="center", color="w")

    # Set the title and show the plot
    ax.set_title(str(METHOD) + " " + "Cosine Similarity Matrix")
    fig.tight_layout()
    # Save picture
    # figureP = "Integrating_SCM_SD/bin/output/figure_cosine_simlarity/" + METHOD + ".png" 
    # plt.savefig(figureP)
    plt.show()

    
if __name__ == "__main__":
    # Path
    warmth_pairs_path = data_yaml["Reduction"]["SCM_warmth"]
    competent_pairs_path = data_yaml["Reduction"]["SCM_competent"]
    evaluation_pairs_path = data_yaml["Reduction"]["Osgood_evaluation"]
    potency_pairs_path = data_yaml["Reduction"]["Osgood_potency"]
    activity_pairs_path = data_yaml["Reduction"]["Osgood_activity"]
    trustworthy_pairs_path = data_yaml["Reduction"]["Trustworthy"]
    
    # Antonym pairs
    ant_pairs_warmth = utils_fun.get_antonym_pairs(warmth_pairs_path)
    ant_pairs_competent = utils_fun.get_antonym_pairs(competent_pairs_path)
    ant_pairs_evaluation = utils_fun.get_antonym_pairs(evaluation_pairs_path)
    ant_pairs_potency = utils_fun.get_antonym_pairs(potency_pairs_path)
    ant_pairs_activity = utils_fun.get_antonym_pairs(activity_pairs_path)
    ant_pairs_trustworthy = utils_fun.get_antonym_pairs(trustworthy_pairs_path)
    
    # dimensions
    dir_warmth = utils_fun.build_dimensions(ant_pairs_warmth) #v1
    dir_competent = utils_fun.build_dimensions(ant_pairs_competent)#v2
    dir_evaluation = utils_fun.build_dimensions(ant_pairs_evaluation)#v3
    dir_potency = utils_fun.build_dimensions(ant_pairs_potency)#v4
    dir_activity = utils_fun.build_dimensions(ant_pairs_activity)#v5
    dir_trustworthy = utils_fun.build_dimensions(ant_pairs_trustworthy)#v6
    
    # vectors = [dir_warmth,dir_competent,dir_evaluation,dir_potency,dir_activity,dir_trustworthy]
    # calculate_each_two(vectors)
    
    
    #  plot the result
    vectors = np.stack([dir_warmth,dir_competent,dir_evaluation,dir_potency,dir_activity,dir_trustworthy])
    heat_map(vectors)
