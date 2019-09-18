# -*- coding: utf-8 -*-
 
import re
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
 
def make_gensim_model_fun(vec_size):
	window_size=10

	# ------------------------------
	# -- 파일 읽기
	# ------------------------------
	file = open("all_function.txt", "r")
	moby_dick = file.read()
	#print(moby_dick)

	moby_dick = moby_dick.replace("rep ","rep")
	moby_dick = moby_dick.replace(".byte","")
	moby_dick = moby_dick.replace('DWORD DPTR ', '')
	moby_dick = moby_dick.replace('DWORD PTR ', '')
	moby_dick = moby_dick.replace('BYTE PTR ', '')
	moby_dick = moby_dick.replace('WORD PTR ', '')
	moby_dick = moby_dick.replace('ds:', '')
	moby_dick = moby_dick.replace("es:","")
	moby_dick = moby_dick.replace('stoses:', '')
	moby_dick = moby_dick.replace('[', '')
	moby_dick = moby_dick.replace(']', '')
	moby_dick = moby_dick.replace("- ","-")
	moby_dick = moby_dick.replace("+"," ")
	moby_dick = moby_dick.replace("-"," -")
	moby_dick = moby_dick.replace("*"," ")	

	 
	# ------------------------------
	# -- 문장별로 Split 처리
	# ------------------------------
	moby_dick = re.split("[\n]", moby_dick)
	#print(moby_dick)
	  
	# ------------------------------
	# -- 공백/빈 리스트 제거
	# ------------------------------
	while ' ' in moby_dick:
	#    moby_dick.remove(' ')
	    moby_dick.remove('')
	 
	    print(moby_dick)
	 
	print("<remove_blank_doc", "_" * 100)
	 
	# ------------------------------
	# -- 데이터프레임에 저장
	# ------------------------------
	df_Mobydic = pd.DataFrame()
	df_Mobydic['sentences'] = np.asarray(moby_dick)
	 
	print (df_Mobydic)
	 
	print("<df_doc", "_" * 100)
	 
	# ------------------------------
	# -- 데이터프레임 문장별 Split
	# ------------------------------
	df_Mobydic["separates"] = df_Mobydic["sentences"].apply(lambda x: x.replace(","," "))
	df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.replace(";",""))
	df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.replace("\"",""))
	#df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.replace("-", " - "))
	#df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.replace("+", " + "))
	#df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.replace("*", " * "))
	df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.split())
	buf=df_Mobydic["separates"]
	#print (buf)

	print("<df_sep_doc", "_" * 100)
	 
	# ------------------------------
	# -- 문장별 Word2Vec 처리
	# ------------------------------
	#min_count 1회 이하 나오는 단어 무시!!!
	model = Word2Vec(buf,size=vec_size, window=window_size, min_count=0, workers=4)
	 
	print(model)
	#print model.wv.vocab
	#print model[" "]

	model.save("./gensim_model"+str(vec_size))


#for vector_size in range(1,16):
vector_size=22
print(vector_size)
make_gensim_model_fun(vector_size)



