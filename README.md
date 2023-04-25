# chain-analysis
Perform chain analysis on a set of provided UTXOs (or descriptors)

A python CLI bitcoin analysis tool to inspect the inputs and outputs of Bitcoin transactions and identify potential privacy issues.

Given a PSBT(Partially Signed Bitcoin Transactions) it provides heuristics information on:

Address Reuse: identifies instances where input addresses are being reused as outputs addresses.
Common Inputs: detect if inputs in a transaction are likely to come from the same wallet.



Installation Guide
Application will be published on PYPI

Current set up process
- Clone repo
- Activate Virtual Enviroment
- Run commands

# Available Cli commands
- python -m analyser -v  # Returns application version
- python -m analyser --help # Provides help memu
- python -m analyser check-addr-reuse  # checks address reuse
- python -m analyser check-common-inputs  # checks common inputs
- python -m analyser check-privacy  # checks for address resuse and common inputs


To Run test
$  python -m pytest
