

import json

from contratos.abi import *

from web3 import Web3

from web3.contract import ConciseContract

#connection to our private eth net
ethNodeUrl=""
web3 = Web3(Web3.HTTPProvider(ethNodeUrl))

#conexión contrato completo

cont_complet_adress = ""
cont_complet_abi = abi()
contractComplete_instance = web3.eth.contract(address=cont_complet_adress,
                                              abi=cont_complet_abi, ContractFactoryClass=ConciseContract)


def putData(_id, _data):
    try:
        web3.personal.unlockAccount(web3.eth.accounts[0], 'password')

        contractComplete_instance.putData(_id,
                                                _data['A'],
                                                _data['B'],
                                                _data['C']['D'],
                                                _data['C']['E'],
                                                transact={'from':web3.eth.accounts[0], 'gas': 410000})

        return True
    except:
        return False





def getSubasta(_id):
    data = {}
    try:
        data['A'] = contractComplete_instance.getData(_id)[0]
        data['B'] = contractComplete_instance.getData(_id)[1]
        data['C']={}
        data['C']['D'] = contractComplete_instance.getData(_id)[2]
        data['C']['E'] = contractComplete_instance.getData(_id)[3]

    except:
        subasta['status'] = False
    return json.dumps(data)





