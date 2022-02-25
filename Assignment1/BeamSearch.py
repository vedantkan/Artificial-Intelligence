import math
import StringDouble
import heapq

class BeamSearch:

    graph = []

    def __init__(self, input_graph):
        self.graph = input_graph
        return

    def beamSearchV1(self, pre_words, beamK, maxToken):
    
        return self.beamSearchV2(pre_words, beamK, 0, maxToken)        # Calling beamSearchV2 with lambda = 0


    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):   
        # Initializing the variables     
        graph_of_words = self.graph.graph
        sentence = pre_words
        prob = 0.0
        p_heap = []
        p_word = "<s>"
        
        for word in pre_words.split():                      #Iterating over all the words present in the previous words by splitting the words
            if word != "<s>":
                
                prob = prob + math.log(graph_of_words[p_word][word])        # formula to calculate the log prob
                
                p_word = word                                   #Setting the next word as previous word

        self.heap_push(p_heap, beamK, prob, False, sentence)

        while True:
            cHeap = []
            
            for (prob, complete, sentence) in p_heap:               # iterating over the values in p_heap
                
                if complete == True:                                # if complete is true, push to heap
                    self.heap_push(cHeap, beamK, prob, True, sentence)

                else:                                               # if not, then set h_word as last word
                    h_word = sentence.split()[-1]
                    
                    for t_word in self.graph.graph[h_word].keys():  # Iterating over the keys of graph with value i for the t_word
                        
                        if t_word == "</s>":                        # if t_word is </s> means sentence is complete
                            length_norm = (len(sentence.split()) + 1) ** param_lambda
                            self.heap_push(cHeap, beamK, prob + math.log(graph_of_words[h_word][t_word])/length_norm, True, sentence + " " + t_word)
                        
                        else:                   # if not, then continue looping
                            self.heap_push(cHeap, beamK, prob + math.log(graph_of_words[h_word][t_word]), False, sentence + " " + t_word)
            
            (prob, complete, sentence) = max(cHeap)             # Maximum score from the current heap
            
            if complete == True and len(sentence.split()) <= maxToken:      # If sentence is complete, return the prob
                return StringDouble.StringDouble(sentence, math.exp(prob))
            
            p_heap = cHeap                          # Setting the previous heap as the current heap
    
    def heap_push(self, heap_q, beamK, sentence_probability, complete, sentence):
        heapq.heappush(heap_q, (sentence_probability, complete, sentence))
        if len(heap_q) > beamK:
            heapq.heappop(heap_q)