import datetime

from mnemonic import Mnemonic
from eth_account import Account

# Number of accounts to create
num_accounts = 10  # Change this to the desired number of accounts

# Initialize the mnemonic generator
mnemo = Mnemonic("english")  # You can specify other languages if needed
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Enable Mnemonic features
Account.enable_unaudited_hdwallet_features()

# Open files for writing
with open(f'seed_phrases_{timestamp}.txt', 'w') as seed_file, \
     open(f'addresses_{timestamp}.txt', 'w') as address_file, \
     open(f'private_keys_{timestamp}.txt', 'w') as private_key_file:

    for _ in range(num_accounts):
        # Generate a random seed phrase
        seed_phrase = mnemo.generate(128)  # 128 bits is a common length
        seed_file.write(seed_phrase + '\n')

        # Derive the private key from the seed phrase
        private_key = Account.from_mnemonic(seed_phrase)

        # Get the Ethereum address and private key
        address = private_key.address
        private_key_hex = private_key.key.hex()  # Convert to hex string

        # Write the address and private key to their respective files
        address_file.write(address + '\n')
        private_key_file.write(private_key_hex + '\n')

print(f'{num_accounts} Ethereum accounts created and saved to files.')
