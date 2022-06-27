from brownie import PolyAirQuality

def main():
    contract = PolyAirQuality[-1]
    PolyAirQuality.publish_source(contract)