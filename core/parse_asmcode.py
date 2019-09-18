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

def parse_asmcode(elf, addr, size):
	node_asmcode_block=[]

	plt_dic=elf.plt
	symbol_dic=elf.symbols

	#print addr, size
	if addr == 0:
		return ''
	asmcode_raw = elf.disasm(addr, size)
	asmcode_raw_lines=asmcode_raw.splitlines()
	
	for line in asmcode_raw_lines:
		instruction_list = line[40:] #remove address, bytecode
		instruction_list = refine_asmcode(instruction_list)
		instruction = instruction_list.split()

		if instruction==[]:
			continue

		#rename plt functions  ex)call 0x8048d14 => call wmemset
		opcode=instruction[0]
		if (opcode == 'call') and (instruction[1][:2]=='0x'):	
			addr=int(instruction[1],16)
			name=find_function_name(addr,symbol_dic)
			if is_plt(addr,plt_dic)==1: #plt function
				name=name.split('.')
				instruction[1]=name[-1]
		#print instruction

		node_asmcode_block.extend(instruction)


	return node_asmcode_block
