// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract VictoryToken is ERC20 {
    constructor() ERC20("VictoryToken", "VTK") {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    function mintTokens(address recipient, uint256 amount) external {
        _mint(recipient, amount);
    }
}
