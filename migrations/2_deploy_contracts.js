const VictoryToken = artifacts.require("VictoryToken");
const BattleToken = artifacts.require("BattleToken");

module.exports = async function(deployer) {
  await deployer.deploy(VictoryToken);
  const victoryTokenInstance = await VictoryToken.deployed();
  console.log(`VictoryToken deployed at address: ${victoryTokenInstance.address}`);

  await deployer.deploy(BattleToken, victoryTokenInstance.address);
  const battleTokenInstance = await BattleToken.deployed();
  console.log(`BattleToken deployed at address: ${battleTokenInstance.address}`);
};
