# BlockChain_Assignment

BlockChain_Assignment

--- Contracts

BattleToken.sol

- This contract enables minting tokens, battling them, and rewarding victory tokens to winners.

1.  Imports: Necessary contracts are imported such as ERC721 and OpenZeppelin, and custom contracts.
2.  External Functions:
    a. mintToken: Creates a new token, assigns it to a recipient, and assigns a random power level.
    b. battleTokens: Allows token owners to battle, with the winner receiving a victory token.
3.  Internal Functions:
    a. \_generateRandomPower: Generates a random power level for a token

SimpleCouner.sol

1. Functions:
   a. currentValue: Retrieves the current value of the counter.
   b. increment: Increments the counter by one.
   c. reset: Resets the counter to zero.

VictoryToken.sol

- This contract provides functionality to mint tokens and transfer them to other addresses.

1. Functions:
   a. mintTokens: This allows the contract owner to Mint additional tokens and assign them to a specified recipient.

Backend.py

- Enables users to mint tokens and conduct battles between them using the provided routes. This interacts with the local host network Ganache and also the App when using the Frontend to execute the transactions.

1. Imports: Necessary libraries were needed such as Flask, Web3, Flask-CORS
2. Web3: Connection with Ganache
3. Mint Route: This handles the POST request to mint new tokens, validate required fields, retrieve the account details, and transaction hash, token ids
4. Battle Route: This handles the POST request to initiate a battle between the 2 tokens. Validates the required fields.

Frontend Folder

- This folder contains the frontend side of the app with functions and styling of the application.
