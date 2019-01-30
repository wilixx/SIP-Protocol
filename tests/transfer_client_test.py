import sys
sys.path.insert(0, 'C:\\Users\\R&DTrainee3\\Desktop\\SIP-Protocol\\src')

import transfer_client

client = transfer_client.transfer_client()
client.get_file('closure_seth_power.mp3')
