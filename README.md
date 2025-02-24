# Solidity_funcsig_checker


## Description
This Python script analyzes multiple dictionaries of smart contract functions and their corresponding function selectors to detect potential function signature collisions. In Ethereum smart contracts—especially when using proxy patterns—it's crucial to ensure that two different functions do not unintentionally share the same selector. Such collisions can lead to unexpected behavior, vulnerabilities, or security breaches.

__Why is this important?__
In a proxy contract pattern, calls to functions are forwarded to implementation contracts using only the function selector (first 4 bytes of the Keccak-256 hash of the function signature). If two different functions (with different names or argument types) share the same selector, the proxy may misroute calls, leading to critical bugs or exploits.

## How to use it?

1. Generate Function Selectors with Foundry
To populate the `.txt` file with function signatures and selectors, use the Foundry command:
```
forge inspect {ContractName} methods >> funcsigs.txt
```
Replace {ContractName} with your specific contract name. Repeat this for each contract you want to include.

2. Paste `.txt` in the root of this dir
3. Ensure you have python installed and run `python check_signatures.py {txt file name}`
4. If there are matching selectors for different func names, it will print to the console
