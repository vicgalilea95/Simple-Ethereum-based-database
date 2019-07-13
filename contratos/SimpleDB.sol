pragma solidity ^0.5.0;

contract SimpleDB {

    address private owner;


    struct substruct {
      uint D;
      uint E;
    }

    struct Data {
	    uint A;
	    string B;
	    substruct C;
	}

	mapping (string=> Data) DataById;

    function getData(string memory  id) public
        view returns(uint, string memory, uint, uint){

         return(DataById[id].A, DataById[id].B, DataById[id].C.D, DataById[id].C.E);

        }

     function putData(string  memory  id, uint A, string  memory  B, uint D,
     uint E) public payable
     {
        DataById[id].A=A;
        DataById[id].B=B;
        DataById[id].C.E=E;
        DataById[id].C.D=D;
    }

}
