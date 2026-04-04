import jsonlines
import re
import numpy as np
import json

def scm_semantic(search_val):
    """search word and return its vector

    Args:
        search_val (str): the word you want to search

    Returns:
        tuple: (word, np.array of dimensions) or None if not found
    """
    model_embeddings = 'word_embeddings/New2_2D.bin'
    try:
        with open(model_embeddings, 'r') as f:
            for line in f:
                key = line.replace('"', '').split(',')[0]
                if key == search_val:
                    dimension = np.array(re.findall(r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)).astype('float64')
                    return (key, dimension)
    except IOError as e:
        print(f"Error reading the file: {e}")
    except Exception as e:
        print(f"Error processing line {line}: {e}")

    return None  # Return None if not found or on error

def process_and_save_data(input_path, output_path):
    """Process the jsonlines file and save the results to another jsonlines file

    Args:
        input_path (str): Path to the input jsonlines file.
        output_path (str): Path to the output jsonlines file.
    """
    with jsonlines.open(input_path, 'r') as file, jsonlines.open(output_path, mode='w') as outfile:
        print(f"Processing file: {input_path}")

        for o in file:
            extracted_text = o.get('author_id', {}).get('extracted_text', [])
            created_at = o.get('author_id', {}).get('created_at', '')
            
            wce_values = []
            ca_values = []

            for t in extracted_text:
                result = scm_semantic(t)
                if result is not None:
                    word, sem_vector = result
                    if sem_vector.size == 2:
                        wce_values.append(sem_vector[0])
                        ca_values.append(sem_vector[1])

            if wce_values and ca_values:
                avg_wce = np.nanmean(wce_values)
                avg_ca = np.nanmean(ca_values)
            else:
                avg_wce = None
                avg_ca = None

            # Construct the output JSON object
            result_data = {
                "created_at": created_at,
                "extract_text": extracted_text,
                "score": {
                    "average_wce": avg_wce,
                    "average_ca": avg_ca
                }
            }
            outfile.write(result_data)

        print(f"Results have been written to {output_path}")

# Example usage
input_json_path = 'stereotype_scenario/restart_0920/results/post_precessing/chn_sscr_output.json'
output_json_path = 'stereotype_scenario/restart_0920/results/score_processing/chn_sscr_score.jsonl'

process_and_save_data(input_json_path, output_json_path)