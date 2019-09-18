import gensim
import re


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

def read_asmcode_corpus(asmcode_corpus_list):
	asmcode_corpus_list = refine_asmcode(asmcode_corpus_list)

	list_instruction = asmcode_corpus_list.split("\n")

	return list_instruction


def gen_instruction2vec_model(asmcode_corpus_list,vectorsize,save_filename):
	word_list = read_asmcode_corpus(asmcode_corpus_list)

	model = Word2Vec(word_list, size=vectorsize, window=128, min_count=1, workers=32, iter = 10)
	print model.wv['push'] # just test
	print model.wv['eax'] # just test

	filename=save_filename
	model.save(filename)
	return model

fun_list = """\
push   ebp
mov    ebp,esp
sub    esp,0x18
mov    eax,0x10
sub    eax,0x1
add    eax,0x19f
mov    ecx,0x10
mov    edx,0x0
div    ecx
imul   eax,eax,0x10
sub    esp,eax
mov    eax,esp
add    eax,0xf
shr    eax,0x4
shl    eax,0x4"""

gen_instruction2vec_model(fun_list,10,"test")