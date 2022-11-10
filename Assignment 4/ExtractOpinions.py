# import StringDouble
# import ExtractGraph
from pycorenlp import StanfordCoreNLP
import json

class ExtractOpinions:
    # Extracted opinions and corresponding review id is saved in extracted_pairs, where KEY is the opinion and VALUE
    # is the set of review_ids where the opinion is extracted from.
    # Opinion should in form of "attribute, assessment", such as "service, good".
    extracted_opinions = {}
    
    def __init__(self):
        return

    def extract_pairs(self, review_id, review_content):
        nlp = StanfordCoreNLP('http://localhost:9000')
        output = nlp.annotate(review_content,properties={
        'annotators': ' tokenize, ssplit, lemma, depparse, sentiment, ner, pos',
        'outputFormat': 'json',
        'openie.triple.strict':'true',
        'timeout': 50000,
        })
        
        pos_dict = {}
 
        for sentence in output['sentences']:            
            for term in sentence["tokens"]:
                pos_dict[term["word"] ]= term["pos"]

            #Extracting enhancedDependencies
            result = [sentence["enhancedDependencies"] for item in output]
            for i in result:
                opinion = ""
                for rel in i:
                    if rel['dep'] == 'amod':
                        opinion = rel['governorGloss'].lower() + ", " + rel['dependentGloss'].lower()                        
                    if rel['dep'] == 'nsubj' and pos_dict[rel['governorGloss']] == 'JJ' and pos_dict[rel['dependentGloss']] == 'NN':
                        opinion = rel['dependentGloss'].lower() + ", " + rel['governorGloss'].lower()
                if opinion != "":
                    if opinion not in self.extracted_opinions.keys():
                        self.extracted_opinions[opinion] = [review_id]
                    else:
                        id_list = self.extracted_opinions[opinion]
                        if review_id not in id_list:
                            id_list.append(review_id)
                            self.extracted_opinions[opinion] = id_list
                
        return(self.extracted_opinions)
        