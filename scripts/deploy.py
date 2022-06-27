from brownie import PolyAirQuality, config, accounts
def main():
    deployer_account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    print(deployer_account.address)
    # Passing the interval to update the state of the dNFT every 86400 seconds (equivalent to 24 hours)
    # So, according to this deployment, the state of the dNFT will be updated everyday according to the data returned by the ShambaDataStream

    contract = PolyAirQuality.deploy(86400, "AIR-QUALITY-dNFT", "dNFT", 3, "air-quality_new-delhi", {'from': deployer_account})
    print("Deployed at: ", contract.address)
