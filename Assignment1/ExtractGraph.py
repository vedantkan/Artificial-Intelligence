class ExtractGraph:

    # key is head word; value stores next word and corresponding probability.
    graph = {}

    sentences_add = "assign1_sentences.txt"

    def __init__(self):
        pWord = '<s>'
        self.graph['<s>'] = {}
        no = 0
        # Extract the directed weighted graph, and save to {pWord, {tail_word, probability}}
        with open(self.sentences_add) as f:            
            for sentence in f:                                                          # Reading each sentence

                for cWord in sentence.split():                                   # Reading each word in sentence  

                    if cWord != '<s>' and pWord != '</s>':                   # Checking if the cWord is not <s> and pWord is not </s> 

                        if pWord not in self.graph.keys():                          # Checking if pWord is in the graph keys                            
                            
                            self.graph[pWord] = {}                                  # If not present, add it
                        
                        if cWord not in self.graph[pWord].keys():            # Checking if current word is in graph keys where key is pWord
                            
                            self.graph[pWord][cWord] = 1                     # If it is not present, add it as {pWord, {cWord, instances}}

                        else:
                           
                            self.graph[pWord][cWord] += 1                    # If it is present, add 1 to the instances
                    
                    pWord = cWord                                            # Set the pWord as the cWord
       
        for i in self.graph.keys():                                                     # For loop is used to iterate over all graph keys
           
            for j in self.graph[i].keys():                                              # Second for loop is used to iterate over the graph's keys with value i
                
                no += self.graph[i][j]                                              # Add number of times it appears
            
            for j in self.graph[i].keys():                                              # Iterating again over the graph's keys with value i
                
                self.graph[i][j] = self.graph[i][j]/no                              # Calculating the probability of pair            
            no = 0
        return

    def getProb(self, head_word, tail_word):
       
        if head_word not in self.graph.keys() or tail_word not in self.graph[head_word].keys():   #if head_word or tail_word isn't present in the graph, return 0
            return 0
        
        return self.graph[head_word][tail_word]                                 #else return graph with values [head_word][tail_word] to get the probability of the pair