import os
import ast
import json

PATH = '../Marion_files/sm_database/'

index = 88
pay_in = 0
pay_out = 0
contract_hash = a.op[0][index]
for tx in a.tr_dico[0][index][0]:
    if tx['from'] in [contract_hash, '']:
        pay_out += 1
    elif tx['to'] in [contract_hash, '']:
        pay_in += 1
    else:
        print(f"con={contract_hash}, in={tx['from']}, out={tx['to']}")

for tx in a.tr_dico[0][index][1]:
    if tx['from'] in [contract_hash, '']:
        pay_out += 1
    elif tx['to'] in [contract_hash, '']:
        pay_in += 1
    else:
        print(f"con={contract_hash}, in={tx['from']}, out={tx['to']}")

print(f"in={pay_in}, out={pay_out}")
