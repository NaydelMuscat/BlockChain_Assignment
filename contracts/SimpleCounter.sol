// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

library SimpleCounter {
    struct Counter {
        uint256 value;
    }

    function currentValue(
        Counter storage counter
    ) internal view returns (uint256) {
        return counter.value;
    }

    function increment(Counter storage counter) internal {
        counter.value += 1;
    }

    function reset(Counter storage counter) internal {
        counter.value = 0;
    }
}
