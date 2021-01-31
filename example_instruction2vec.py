import sys
import core.gen_gensim_model as gen
import core.instruction2vec as inst2vec


test_asmcode = """
push   ebp
mov    ebp,esp
sub    esp,0x18
mov      ebp -0xc ,eax
call wmemset
mov      ebp -0x34 ,0x41414141
mov      ebp + eax * 4 -0x38 ,0x1"""


fd = open("./sample/asmcode_corpus", "r")
asmcode_corpus = fd.read()

vectorsize = 5

model = gen.gen_instruction2vec_model(asmcode_corpus,vectorsize,"test_model")

for one_instruction in test_asmcode.split('\n'):
	print(one_instruction)
	vector_of_intruction = inst2vec.instruction2vec(one_instruction,model,vectorsize)
	print (vector_of_intruction)