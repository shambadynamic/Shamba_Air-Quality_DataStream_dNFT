from brownie import PolyAirQuality, config, accounts

def printGeoData(contract):

    if contract.getShambaGeostatsData() != 0:
        print("Air Quality Data by Shamba Oracle: ", contract.getShambaGeostatsData())
    else:
        print("Data isn't available yet. Please check the job run in the oracle node.")
        
def main():
    deployer_account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    print(deployer_account.address)
    print('\n')
    contract = PolyAirQuality[-1]
    printGeoData(contract)