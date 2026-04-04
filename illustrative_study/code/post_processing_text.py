import ijson
import jsonlines
import re
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from langdetect import detect, LangDetectException

# Download the required nltk resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Get a set of English stop words
stop_words = set(stopwords.words('english'))

def process_file(jpath, output_path):
    """
    Process a single JSON file, filter and preprocess data, and write to a new JSON file.
    :param jpath: The input JSON file path
    :param output_path: The output JSON file path
    """
    count = 0  # To count the number of entries processed

    with jsonlines.open(jpath, 'r') as file:
        print(f"Processing file: {jpath}")

        with jsonlines.open(output_path, 'a') as writer:
            for o in file:
                if process_object(o, writer):
                    count += 1

        print(f"Finished processing {jpath}")
    
    print(f"Total processed entries: {count}")

def process_object(obj, writer):
    created_at = obj.get('author_id', {}).get('created_at', '')
    text = obj.get('author_id', {}).get('text', '')

    if not filter_by_date(created_at, "2019-12-01", "2021-01-01"):
        return False

    if not is_english(text):
        return False

    processed_text = preprocess_text(text)



    adjectives = extract_adjectives(processed_text)
    verbs = extract_verbs(processed_text)

    info = {
        'created_at': created_at,
        'text': processed_text,
        'extracted_text': adjectives + verbs  # Merging adjectives and verbs into one key
    }

    writer.write({'author_id': info})
    
    return True

def is_english(text):
    try:
        return detect(text) == 'en' 
    except LangDetectException:
        return False

def filter_by_date(date_str, start_date, end_date):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        return start <= date_obj <= end
    except ValueError:
        return False

def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def extract_adjectives(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    adjectives = [word for word, tag in pos_tags if tag in ('JJ', 'JJR', 'JJS') and word != "scientist"]
    return adjectives

def extract_verbs(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    verbs = [word for word, tag in pos_tags if tag.startswith('VB')]
    return verbs

def contains_keywords(text, keywords):
    for keyword in keywords:
        if keyword in text:
            return True
    return False

file_paths = ['stereotype_scenario/restart_0920/results/pre_processing/jap_sscr.json']
output_file = 'stereotype_scenario/restart_0920/results/post_precessing/jap_sscr_output.json'

for file_path in file_paths:
    process_file(file_path, output_file)

print("All files processed.")