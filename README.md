Small python script that converts the list of Ethereum private keys into public addresses and checks the current balance of the address.

Requirements: 
```python
python 3
```

Usage:
```python
git clone https://github.com/AhrimanSefid/ethercheck.git
pip install ethereum
pip install binascii
pip install requests
pip install time 
python eth.py
```

This tool uses Google [BigQueryDB](https://cloud.google.com/bigquery/) query results as input. 
That input comes from scanning regex expression for all public Github repos matching the Ethereum private key.

BigQueryDB query:
``` 
#standardSQL
SELECT f.repo_name, f.path, c.pkey
FROM `bigquery-public-data.github_repos.files` f JOIN
     (SELECT id,
             REGEXP_EXTRACT(content, r'(?:^|[^a-zA-Z0=9])([123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ]{64,64})(?:$|[^a-zA-Z0-9])') AS pkey
      FROM `bigquery-public-data.github_repos.contents`
      WHERE REGEXP_CONTAINS(content, r'(?:^|[^a-zA-Z0=9])([123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ]{64,64})(?:$|[^a-zA-Z0-9])')
     ) c
     ON f.id = c.id;

```

After that, it uses [Etherscan's](http://etherscan.io) public API to check the balances for the given address.

Note: you may be rate limited if triggering too many ruquests, sign up for API key [HERE](https://etherscan.io/) 


Usage Example:
![ethercheck](https://i.imgur.com/Fe1fNwp.png)


Any suggestions, fixes or PR's are more then welcome.

Update: Added normalized CSV for testing purposes.
