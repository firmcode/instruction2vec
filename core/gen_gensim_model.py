import gensim
import re
from gensim.models import Word2Vec
import instruction2vec as inst2vec


def read_asmcode_corpus(asmcode_corpus):
	asmcode_corpus = inst2vec.refine_asmcode(asmcode_corpus)
	list_instruction = []
	
	asmcode_corpus_list_split = asmcode_corpus.split('\n')

	for one_instruction in asmcode_corpus_list_split:

		one_instruction=one_instruction.replace(',',' ') # for split
		one_instruction=one_instruction.split()
		list_instruction.append(one_instruction)

	return list_instruction


def gen_instruction2vec_model(asmcode_corpus,vectorsize,save_filename):

	word_list = read_asmcode_corpus(asmcode_corpus)

	model = Word2Vec(word_list, size=vectorsize, window=128, min_count=1, workers=4, iter = 10)

	filename=save_filename
	model.save(filename)
	return model


