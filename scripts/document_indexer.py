from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()

def create_script_index(series_name, episode, url, order, original_sentence, lem_sentence):
    doc = {
        'series': series_name,
        'episode': episode,
        'url': url,
        'order': order,
        'phase': original_sentence,
        'lemme': lem_sentence,
        'timestamp': datetime.now(),
    }
    
    es.index(index="cali-mix", doc_type='document', body=doc)
    