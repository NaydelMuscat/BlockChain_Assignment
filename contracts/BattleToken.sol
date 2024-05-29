// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "./SimpleCounter.sol";

contract BattleToken is ERC721 {
    using SimpleCounter for SimpleCounter.Counter;
    SimpleCounter.Counter private _tokenIds;
    mapping(uint256 => uint256) public tokenPower;

    constructor() ERC721("BattleToken", "BTK") {}

    function mint(address to) external {
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        _mint(to, newTokenId);
        tokenPower[newTokenId] = randomPower();
    }

    function battle(uint256 tokenId1, uint256 tokenId2) external {
        require(ownerOf(tokenId1) == msg.sender, "Not owner of token1");
        require(ownerOf(tokenId2) == msg.sender, "Not owner of token2");

        uint256 power1 = tokenPower[tokenId1];
        uint256 power2 = tokenPower[tokenId2];

        if (power1 > power2) {
            // Handle victory condition
        } else if (power2 > power1) {
            // Handle loss condition
        } else {
            // Handle draw condition
        }

        tokenPower[tokenId1] = randomPower();
        tokenPower[tokenId2] = randomPower();
    }

    function randomPower() internal view returns (uint256) {
        return
            uint256(
                keccak256(abi.encodePacked(block.timestamp, block.prevrandao))
            ) % 100;
    }
}
