## dumps()-> Encryption
## loads()-> Decryption

'''
1. JSON: to save data in an organised manner, data will convert into string
2. pickle
'''

import pickle
file = open('temp.txt', 'ab+')
data = {
    'fullName': 'Rahul',
    'userid': 7898456526,
    'password': '******'
}
print(f'Original Data: {data}')
print(f'Type of original Data: {type(data)}')

enc_data = pickle.dumps(data)
file.write(enc_data)

file.seek(0)
print(file.read())

# print(f'Encrypted Data: {enc_data}')
# print(f'Type of encrypted Data: {type(enc_data)}')

dec_data = pickle.loads(enc_data)
print(f'Decrypted Data: {dec_data}')
print(f'Type of decrypted Data: {type(dec_data)}')

file.close()