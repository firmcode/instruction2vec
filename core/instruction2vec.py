import re
import numpy as np


def refine_asmcode(raw_asmcode):
    raw_asmcode = raw_asmcode.replace("rep ", "rep")
    raw_asmcode = raw_asmcode.replace(".byte", "")
    raw_asmcode = raw_asmcode.replace('DWORD DPTR ', '')
    raw_asmcode = raw_asmcode.replace('DWORD PTR ', '')
    raw_asmcode = raw_asmcode.replace('BYTE PTR ', '')
    raw_asmcode = raw_asmcode.replace('WORD PTR ', '')
    raw_asmcode = raw_asmcode.replace('ds:', '')
    raw_asmcode = raw_asmcode.replace("es:", "")
    raw_asmcode = raw_asmcode.replace('stoses:', '')
    raw_asmcode = raw_asmcode.replace('[', '')
    raw_asmcode = raw_asmcode.replace(']', '')
    raw_asmcode = raw_asmcode.replace("- ", "-")
    raw_asmcode = raw_asmcode.replace("+", " ")
    raw_asmcode = raw_asmcode.replace("-", " -")
    raw_asmcode = raw_asmcode.replace("*", " ")

    return raw_asmcode


def instruction2vec(one_insutruction, model, vectorsize):
    if not one_insutruction:  # check blank
        return 0
    one_insutruction = refine_asmcode(one_insutruction)
    splited_instruction = one_insutruction.split()

    #########opcode postion##########
    opcode_box = splited_instruction[0]

    #########oprand 2 vec##########
    # operand_list=''.join(splited_instruction[1:])
    operand_str = one_insutruction[len(opcode_box):]  # del opcode
    # operand_list=operand_list.split(',')
    operand_list = operand_str.split(',')

    oprand_2_boxs = [['0', '0', '0', '0'], ['0', '0', '0', '0']]
    for idx, operand in enumerate(operand_list):
        # 0 : reg, 1 : hex_address, 2 : second reg, 3 : second int
        operands = operand.split()

        if not operands:  # empty list
            continue

        operand_list_empty = ['0', '0', '0', '0']

        for operands_one in operands:

            num_format = re.compile("[1-9]")
            isnumber = re.match(num_format, operands_one)

            # only hex
            if (operands_one[:2] == '0x') or (operands_one[:3] == '-0x'):
                operand_list_empty[1] = operands_one
            # only int DWORD PTR [ebp+eax*4-0x2c],edx -> 4!!
            elif isnumber:
                operand_list_empty[3] = operands_one
            # only reg
            elif len(operands_one):
                if operand_list_empty[0] == '0':
                    operand_list_empty[0] = operands_one
                else:
                    operand_list_empty[2] = operands_one

        if idx >= 2:
            continue
        oprand_2_boxs[idx] = operand_list_empty

    zeroes_arry = np.zeros(vectorsize)
    try:
        ret_arry = model.wv[opcode_box]

        for operand in oprand_2_boxs:
            for oprand_values in operand:
                if oprand_values == '0':
                    ret_arry = np.hstack([ret_arry, zeroes_arry])
                else:
                    ret_arry = np.hstack([ret_arry, model.wv[oprand_values]])
    except:
        print("Error!!!")
        print(opcode_box, oprand_2_boxs)
        print(one_insutruction)

    # print ret_arry
    return ret_arry
