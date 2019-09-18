import sys
import core.gen_gensim_model as gen

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

model = gen.gen_instruction2vec_model(fun_list,10,"test")