from PGP_All_Common import *

bob_privatekey = './HybridBob/bobprivatekey.txt'
bob_publickey = './HybridBob/bobpublickey.txt'
alice_publickey = './HybridBob/received_alicepublickey.txt'

bob_received_output_b64 = './HybridBob/received_outputAlice_b64.txt'
PGP_Server_Receive_File_byUDP('localhost', 9001, bob_received_output_b64)

bob_received_output = './HybridBob/received_outputAlice.txt'
B64Decoding(bob_received_output_b64, bob_received_output)

bob_received_sig_MSG_alice = './HybridBob/sig_MSG_Alice.txt'
Generate_AES_Dec_For_DigSig_Plus_Key(bob_received_output, bob_privatekey, bob_received_sig_MSG_alice)
Verify_DigSig_On_Hashed_File(bob_received_sig_MSG_alice, alice_publickey)

