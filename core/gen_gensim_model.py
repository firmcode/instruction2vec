import gensim
import re
from gensim.models import Word2Vec

def refine_asmcode(raw_asmcode):
	raw_asmcode = raw_asmcode.replace("rep ","rep")
	raw_asmcode = raw_asmcode.replace(".byte","")
	raw_asmcode = raw_asmcode.replace('DWORD DPTR ', '')
	raw_asmcode = raw_asmcode.replace('DWORD PTR ', '')
	raw_asmcode = raw_asmcode.replace('BYTE PTR ', '')
	raw_asmcode = raw_asmcode.replace('WORD PTR ', '')
	raw_asmcode = raw_asmcode.replace('ds:', '')
	raw_asmcode = raw_asmcode.replace("es:","")
	raw_asmcode = raw_asmcode.replace('stoses:', '')
	raw_asmcode = raw_asmcode.replace('[', '')
	raw_asmcode = raw_asmcode.replace(']', '')
	raw_asmcode = raw_asmcode.replace("- ","-")
	raw_asmcode = raw_asmcode.replace("+"," ")
	raw_asmcode = raw_asmcode.replace("-"," -")
	raw_asmcode = raw_asmcode.replace("*"," ")

	return raw_asmcode

def read_asmcode_corpus(asmcode_corpus_list):
	asmcode_corpus_list = refine_asmcode(asmcode_corpus_list)
	list_instruction = []
	
	asmcode_corpus_list_split = asmcode_corpus_list.split('\n')

	for one_instruction in asmcode_corpus_list_split:

		one_instruction=one_instruction.replace(',',' ') # for split
		one_instruction=one_instruction.split()
		list_instruction.append(one_instruction)

	return list_instruction


def gen_instruction2vec_model(asmcode_corpus_list,vectorsize,save_filename):
	word_list = read_asmcode_corpus(asmcode_corpus_list)
	print word_list

	model = Word2Vec(word_list, size=vectorsize, window=128, min_count=1, workers=32, iter = 10)
	print model.wv['push'] # just test
	print model.wv['eax'] # just test

	filename=save_filename
	model.save(filename)
	return model


