#!/usr/bin/python
import sys, os, argparse, requests, ethereum, binascii, time
from multiprocessing import Pool

def scanether(balance):
    try:
        # Convert private key to address and print the result
        eth_address = ethereum.utils.privtoaddr(INPUTFILE)
        eth_address_hex = binascii.hexlify(eth_address).decode("utf-8")
        eth_balance = requests.get("https://api.etherscan.io/api?module=account&action=balance&address=0x" + eth_address_hex + "&tag=latest&apikey=V9GBE7D675BBBSR7D8VEYGZE5DTQBD9RMJ").json()["result"]

        # Check if the result is > 0
        if ('result' != 0) in r.eth_balance: 
            print("[*] Address with balance found: " + eth_address_hex + priv)
            # Write match to OUTPUTFILE
            fHandle = open(OUTPUTFILE,'a')
            fHandle.write(eth_address_hex + privkey + "\n")
            fHandle.close()
        else:
            print("balance: {} address: 0x{} privkey: {}".format(float(eth_balance)/100000000, eth_address_hex, priv))
            time.sleep(1)


    except Exception as e:
        return

if __name__ == '__main__':
    print("""
# Finding the Ethereum address with balance
        """)
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', default='input.txt', help='input file')
    parser.add_argument('-o', '--outputfile', default='output.txt', help='output file')
    parser.add_argument('-t', '--threads', default=200, help='threads')
    args = parser.parse_args()

    INPUTFILE=args.inputfile
    OUTPUTFILE=args.outputfile
    MAXPROCESSES=int(args.threads)

    try:
        addresses = open(INPUTFILE, "r").readlines()
    except FileNotFoundError as e:
        print(e)
        exit(e.errno)

    print("Scan in progress...")
    pool = Pool(processes=MAXPROCESSES)
    pool.map(scanether, addresses)
    print("Scan finished.")