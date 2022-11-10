import gensim.models.keyedvectors as word2vec


class FindSimilarOpinions:
    extracted_opinions = {}
    word2VecObject = []
    cosine_sim = 0

    def __init__(self, input_cosine_sim, input_extracted_ops):
        self.cosine_sim = input_cosine_sim
        self.extracted_opinions = input_extracted_ops
        word2vec_add = "assign4_word2vec_for_python.bin"
        self.word2VecObject = word2vec.KeyedVectors.load_word2vec_format(word2vec_add, binary=True)
        return

    def get_word_sim(self, word_1, word_2):
        return self.word2VecObject.similarity(word_1, word_2)

    def findSimilarOpinions(self, query_opinion):
        similar_opinions = {}
        query = query_opinion.split(", ")
        query_atr = query[0]
        query_qlty = query[1]
        for opinion in self.extracted_opinions:
            op = opinion.split(", ")
            opinion_atr = op[0]
            opinion_qlty = op[1]
            if op_atr in self.word2VecObject and op_qlty in self.word2VecObject:
                atr_similarity = self.get_word_sim(query_atr, opinion_atr)
                qlty_similarity = self.get_word_sim(query_qlty, opinion_qlty)
                if (atr_similarity >= self.cosine_sim and qlty_similarity >= self.cosine_sim):
                    similar_opinions[opinion] = self.extracted_opinions[opinion]
        return similar_opinions
