import random
seedOrder = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', ' ', '?', ';', '"', ',', '.', '/', '~', '_', '+', '{', '}', '|']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
print("FYI, this program is not case sensitive and will \nonly return uppercase letters and other characters. \n")
choice = input("Do you wish to encrypt or decrypt a message? \nType 'E' for encrypt and 'D' for decrypt. \n \n").upper()
if choice == 'E':
  encryptedmessage = ''
  seed = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', ' ', '?', ';', '"', ',', '.', '/', '~', '_', '+', '{', '}', '|']
  random.shuffle(seed)
  message = str(input('\nMessage to encrypt: ')).upper()
  for char in message:
    if char == ' ':
      encryptedmessage = encryptedmessage + ' '
    else:
      encryptTo = seed[letters.index(char)]
      encryptedmessage += letters[seedOrder.index(encryptTo)]
      #experimental
  print(f'Your encrypted message is: {encryptedmessage}')
  seed = ''.join(seed)
  print(f'Your seed is: {seed}')
elif choice== "D":
  decryptedmessage = ''
  message = str(input('Message to decrypt: ')).upper()
  seed = str(input('Encryption seed: '))
  for char in message:
    if char == ' ':
      decryptedmessage = decryptedmessage + ' '
    else:
      decryptTo = seedOrder[letters.index(char)]
      decryptedmessage += letters[seed.index(decryptTo)]
  print(decryptedmessage)
else:
  print('Invalid Input. Try again')