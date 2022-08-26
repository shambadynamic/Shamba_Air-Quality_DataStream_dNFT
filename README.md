# Shamba_Air-Quality_DataStream_dNFT


## dNFT Smart Contract creation

Inside the **contracts** folder, you can see the **AirQuality_dNFTs.sol**, that is having the **PolyAirQuality** contract that is inheriting **ERC721URIStorage** and **ShambaDataStream** contracts using the imported smart contract kits of [openzeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts) and [shamba](https://github.com/shambadynamic/Shamba-smartcontractkit) respectively, configured in the **brownie-config.yaml** file.


## Using desired dNFT artworks by storing the same in filecoin-ipfs web3 storage

You can create your own dNFT artworks' images or gifs as per your creativity or choice, and then you can store the same in [filecoin-ipfs web3 storage](https://web3.storage/). Or otherwise, you can use the ones that are already being defined there and stored in shamba's web3 storage, and referred in the `array of strings` as:

```
string[] IpfsUri = [
    "https://bafybeigf6dd7f3vnw5q7vvl2n5blk3ex4g55r2b7vshjs6cu2gbghnp7be.ipfs.dweb.link/no-data-emoji.json",
    "https://bafybeifgoedfpeuhiyhe4mw24bzcizzcjryvceubujosi2n4xe37o7brgi.ipfs.dweb.link/good-air-quality-emoji.json",
    "https://bafybeifgoedfpeuhiyhe4mw24bzcizzcjryvceubujosi2n4xe37o7brgi.ipfs.dweb.link/intermediate-air-quality-emoji.json",
    "https://bafybeifgoedfpeuhiyhe4mw24bzcizzcjryvceubujosi2n4xe37o7brgi.ipfs.dweb.link/bad-air-quality-emoji.json"
];
```

You can see that each `string` in the array is pointing out to a `json` file stored in web3 storage. In this case they are storing the information about the emoji animations/gifs corresponding to *no data, good air quality, intermediate air quality and bad air quality* use-cases according to the data that is being returned by the **Shamba Geospatial Oracle**.


## dNFT Smart Contract deployment

Inside the **scripts** folder, you can see the **deploy.py** script, as the contructor of the smart contract is accepting 5 parameters in total i.e., *_interval (in seconds) for dNFT state updation, dNFT_name, dNFT_symbol, shamba_DON_Number, shamba_Data_Stream_Code*, among which *dNFT_name* and *dNFT_symbol* are further passed into the parent **ERC721** contract, and *shamba_DON_Number* and *shamba_Data_Stream_Code* are passed into the parent **ShambaDataStream** contract.

For getting the values of *shamba_DON_Number* and *shamba_Data_Stream_Code*, you can refer to the following table:

```
DON_Number          Network           Number of Nodes       Data_Stream_Codes

    1            Ethereum Kovan            3               temperature_new-delhi
                                                           temperature_nairobi                  

    2            Ethereum Kovan            5               fire_riverside

    3            Polygon Mumbai            3               air-quality_new-delhi
```


**NOTE**: Due to the deprecatation of Kovan testnet on Ethereum Layer 1 network, we're currently serving only `DON_Number 3` i.e. on Polygon Mumbai network.

## Usage of Chainlink Keepers

After the successful deployment of the dNFT contract, you'll get the deployed address for the same. Now, you can verify and publish the source code of the contract to [Mumbai Polygonscan](https://mumbai.polygonscan.com/). And after that, you can copy the deployed contract address and go to [Chainlink Keepers](https://keepers.chain.link/) and click on [Register new Upkeep](https://keepers.chain.link/mumbai/new) and proceed with filling the details accordingly, in the *Upkeep address* field, paste your copied deployed contract address i.e., a keeper-compatible contract due to the presence of `checkUpkeep()` and `performUpkeep()` functions in the smart contract. In the `performUpkeep()` function itself, we're calling the `update_dNFT()` function in order to schedule it on the basis of the passed interval parameter value i.e., 86400 seconds equivalent to 24 hours or 1 day in our case, so as to make it keep updating the state of the dNFT every 24 hours according to the updated value of the *lastest geospatial data* (i.e., itself updating everyday) provided by the corresponding Shamba Data Stream. You can check the latest value of the same by running the **getGeostatsData.py** script available inside the **scripts** folder.


## Minting of the deployed dNFT

Inside the **scripts** folder, you can see the **mint_dNFT.py** script, so you can execute the same in order to mint your deployed dNFT contract so as to make it available on the NFT marketplace like [Opensea](https://testnets.opensea.io/).


## States of the dNFT

According to the value of the latest geospatial data provided by the Shamba Data Stream, the states of the dNFT keep changing on the basis of the conditions that are being put in the `update_dNFT()` function.

In this case, the conditions are:

> If the value is less than or equal to 0.3 * 10 ^ 17 (i.e., 30000000000000000) ->  Good Air Quality <br /><br />
> If the value is greater than 0.3 * 10 ^ 17 (i.e., 30000000000000000) and less than 0.4 * 10 ^ 17 (i.e., 40000000000000000) ->  Intermediate Air Quality <br /><br />
> If the value is greater than or equal to 0.4 * 10 ^ 17 (i.e., 40000000000000000) ->  Bad Air Quality <br /><br />


### Good Air Quality dNFT

![Good Air Quality dNFT](/assets/images/GoodAirQuality_dNFT.png)


### Intermediate Air Quality dNFT

![Intermediate Air Quality dNFT](/assets/images/IntermediateAirQuality_dNFT.png)


### Bad Air Quality dNFT

![Bad Air Quality dNFT](/assets/images/BadAirQuality_dNFT.png)



#### Inforamtion about our deployed dNFT:

> Smart contract: https://mumbai.polygonscan.com/address/0x8228a2974A3015Abc49a5CD56cE7549A90FB8Da0

> Upkeep: https://keepers.chain.link/mumbai/33554517935830133558858453378819953745431036423431830498880781053640827894198

> Opensea: https://testnets.opensea.io/collection/air-quality-dnft

> Flux Aggregator: https://mumbai.polygonscan.com/address/0x4b7c440b5e980Ae67bA801979cAbDb155976e6c1