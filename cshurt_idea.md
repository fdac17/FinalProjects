# Bitcoin Money Laundering
Bitcoin is a pseudo-anonymous cryptocurrency, known for making millionaires of random internet geeks and its association with online drug trafficking.
The most interesting feature (for our purposes) of bitcoin is the [blockchain](https://en.bitcoin.it/wiki/Block_chain): a completely public ledger that records every transaction ever performed, and is updated in real time as new transactions occur.
The blockchain represents a public treasure trove of data, ripe for interested data scientist to play with.
There are [many](https://bitinfocharts.com/bitcoin/) [sites](https://blockchain.info/) and [programs](https://github.com/bitbart/bitcoin-analytics-api) that perform various levels of analysis on the blockchain.
My interest, with this project, will be part of an attempt to de-anonymize certain transactions by finding a measure that can determine how related two transactions are.

Bitcoin transactions can be modeled as unidirectional, sparse [graphs](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)).
This [has been done](https://eprint.iacr.org/2012/584.pdf) [many times](https://blogs.cornell.edu/info2040/2013/10/03/busting-the-silk-road-with-graph-theory/) before.
The goal for this project would be to model bitcoin transactions as a graph, and identify an easy method or tool to measure how related two transactions are.
This measure or technique could be useful in identifying money laundering operations, where criminals seek to obscure the 'dirty' source of money to create 'clean' cash for legal uses.
A stretch goal for this project would be to create a web scraper designed to look for and identify valid bitcoin addresses online, and associate those with posted identities.
