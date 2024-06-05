// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "./SimpleCounter.sol";
import "./VictoryToken.sol";

contract BattleToken is ERC721 {
    using SimpleCounter for SimpleCounter.Counter;
    SimpleCounter.Counter private _tokenIds;
    mapping(uint256 => uint256) public tokenPower;

    VictoryToken public victoryTokenContract;

    event TokenMinted(address indexed recipient, uint256 indexed tokenId);

    constructor(address victoryTokenAddress) ERC721("BattleToken", "BTK") {
        victoryTokenContract = VictoryToken(victoryTokenAddress);
    }

    function mintToken(address recipient) external {
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.currentValue();
        _mint(recipient, newTokenId);
        tokenPower[newTokenId] = _generateRandomPower();
        emit TokenMinted(recipient, newTokenId);
    }

    function battleTokens(uint256 tokenId1, uint256 tokenId2) external {
        require(
            ownerOf(tokenId1) == msg.sender,
            "Caller is not the owner of token1"
        );
        require(
            ownerOf(tokenId2) == msg.sender,
            "Caller is not the owner of token2"
        );

        uint256 power1 = tokenPower[tokenId1];
        uint256 power2 = tokenPower[tokenId2];

        if (power1 > power2) {
            victoryTokenContract.mintTokens(
                msg.sender,
                1 * 10 ** victoryTokenContract.decimals()
            );
        } else if (power2 > power1) {
            victoryTokenContract.mintTokens(
                msg.sender,
                1 * 10 ** victoryTokenContract.decimals()
            );
        }

        tokenPower[tokenId1] = _generateRandomPower();
        tokenPower[tokenId2] = _generateRandomPower();
    }

    function _generateRandomPower() internal view returns (uint256) {
        return
            uint256(
                keccak256(abi.encodePacked(block.timestamp, block.prevrandao))
            ) % 100;
    }
}
