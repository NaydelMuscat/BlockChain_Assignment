const BattleToken = artifacts.require("BattleToken");
const VictoryToken = artifacts.require("VictoryToken");

module.exports = function (deployer) {
    deployer.deploy(VictoryToken).then(function() {
        return deployer.deploy(BattleToken);
    });
};