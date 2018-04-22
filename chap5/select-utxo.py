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