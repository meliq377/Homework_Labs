def vigenere_gaxtnagrum(mutq_text, key):
  
    mutq_text = mutq_text.upper()
    key = key.upper()

    key_len = len(key)
    padded_key = key * (len(mutq_text) // key_len + 1)[:len(mutq_text)]

    shift_dict = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}

    ciphertext = ""
    for i, tar in enumerate(mutq_text):
      if tar not in shift_dict:
        ciphertext += tar
        continue
      shift = shift_dict[padded_key[i]]
      new_char = chr((ord(tar) + shift - ord('A')) % 26 + ord('A'))
      ciphertext += new_char

    return ciphertext