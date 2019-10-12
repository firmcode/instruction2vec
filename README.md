# Instruction2vec
Yongjun Lee, Hyun Kwon, Sang-Hoon Choi, Seung-Ho Lim, Sung Hoon Baek, Ki-Woong Park* - Instruction2vec:Efficient Preprocessor of Assembly Code to Detect Software Weakness with CNN
(https://www.mdpi.com/2076-3417/9/19/4086)

# What?
Instruction2vec is a preprocessor that vectorizes the instructions of the assembly code. The output of Instruction2vec is a vector value that can be trained on various models. Instruction2vec has the following characteristics:
* Gives a vector value of fixed length.
* Considers the syntax of the assembly code.
* Works based on Word2vec.

# Example
```python
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
	print one_instruction
	vector_of_intruction = inst2vec.instruction2vec(one_instruction,model,vectorsize)
	print vector_of_intruction
```
