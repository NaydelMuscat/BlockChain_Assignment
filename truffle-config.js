require('dotenv').config();
const HDWalletProvider = require('@truffle/hdwallet-provider');

const MNEMONIC = process.env.MNEMONIC || "source public cave mechanic stove anxiety float pig vessel mobile disease manual";
const PROJECT_ID = process.env.PROJECT_ID || "1c588de8a6c74e4082197e91926699a5";

module.exports = {
  networks: {
    development: {
      host: "127.0.0.1", // Localhost for Ganache
      port: 7545, // Standard Ganache port
      network_id: "*", // Match any network id
    },
    sepolia: {
      provider: () => new HDWalletProvider(MNEMONIC, `https://sepolia.infura.io/v3/${PROJECT_ID}`),
      network_id: 11155111, // Sepolia's network ID
      confirmations: 2, // # of confirmations to wait between deployments
      timeoutBlocks: 200, // # of blocks before a deployment times out
      skipDryRun: true, // Skip dry run before migrations
    },
  },
  mocha: {
    timeout: 100000
  },
  compilers: {
    solc: {
      version: "0.8.21", // Fetch exact version from solc-bin
      settings: {
        optimizer: {
          enabled: true,
          runs: 200,
        },
        evmVersion: "petersburg"
      }
    }
  }
};
