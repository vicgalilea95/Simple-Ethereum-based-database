def abi():
	abi=[
	{
		"constant": "false",
		"inputs": [
			{
				"name": "id",
				"type": "string"
			},
			{
				"name": "A",
				"type": "uint256"
			},
			{
				"name": "B",
				"type": "string"
			},
			{
				"name": "D",
				"type": "uint256"
			},
			{
				"name": "E",
				"type": "uint256"
			}
		],
		"name": "putData",
		"outputs": [],
		"payable": "true",
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "id",
				"type": "string"
			}
		],
		"name": "getData",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	}
]
	return abi
