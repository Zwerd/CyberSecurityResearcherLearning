from Crypto.Cipher import AES
'''
cipher = AES.new(self.key, AES.MODE_EBC)
return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
'''

encoded_file = open(str(input('Please type the encryptrd file name: ')), 'r')
decoded_file = open(str(input('Please type the name for output file: ')), 'w')

enc_algo = AES.new(key, AES.MODE_EBC)
enc_algo.decrypt(encoded_file)