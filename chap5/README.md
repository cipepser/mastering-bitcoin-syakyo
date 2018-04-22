# 第5章 トランザクション

## UTXO

addressを指定してUTXOを確認する

```python
import json
import requests

address = '1Dorian4RoXcnBv9hnQ4Y2C1an6NJ4UrjX'

resp = requests.get('https://blockchain.info/unspent?active=%s' % address)
utxo_set = json.loads(resp.text)["unspent_outputs"]

for utxo in utxo_set:
    print "%s:%d - %ld Satoshis" % (utxo['tx_hash'], utxo['tx_output_n'], utxo['value'])
```

実行結果

```sh
dbb3853afdb127cb7555bf44a033fa69b57335720132b8c016239ca80e4e570b:0 - 101010 Satoshis
```

### 貪欲法で利用するUTXOを選ぶ

tx_hashは記載をサボってる。

```python
from sys import argv

class OutputInfo:
    def __init__(self, tx_hash, tx_index, value):
        self.tx_hash = tx_hash
        self.tx_index = tx_index
        self.value = value
        
    def __repr__(self):
        return "<%s:%s with %s Satoshis>" % (self.tx_hash, self.tx_index, self.value)

def select_outputs_greedy(unspent, min_value):
    if not unspent:
        return None
    
    lessers = [utxo for utxo in unspent if utxo.value < min_value]
    greaters = [utxo for utxo in unspent if utxo.value >= min_value]
    key_func = lambda utxo: utxo.value
    if greaters:
        min_greater = min(greaters)
        change = min_greater.value - min_value
        return [min_greater], change
    
    lessers.sort(key=key_func, reverse=True)
    result = []
    accum = 0
    for utxo in lessers:
        result.append(utxo)
        accum += utxo.value
        if accum >= min_value:
            change = accum - min_value
            return result, "Change: %d Satoshis" % change
    
    return None, 0

def main():
    unspent = [
        OutputInfo("addr0", 0, 1000000),
        OutputInfo("addr1", 1, 2500000),
        OutputInfo("addr2", 2, 1000000),
        OutputInfo("addr3", 3, 3000000),
        OutputInfo("addr4", 4, 5000000),
    ]
    
    if len(argv) > 1:
        target = long(argv[1])
    else:
        target = 5500000
    
    print "For transaction ammout %d Satoshis (%f bitcoin) use: " % (target, target/10.0**8)
    print select_outputs_greedy(unspent, target)
    
if __name__ == "__main__":
    main()
```

実行結果

```sh
❯ python select-utxo.py 5500000
For transaction ammout 5500000 Satoshis (0.055000 bitcoin) use:
([<addr4:4 with 5000000 Satoshis>, <addr3:3 with 3000000 Satoshis>], 'Change: 2500000 Satoshis')
```

所持金が足りないと以下のようになる。

```sh
❯ python select-utxo.py 55000000
For transaction ammout 55000000 Satoshis (0.550000 bitcoin) use:
(None, 0)
```
