def vigenere_gaxtnagrum_sym(mutq_text, key):

    mutq_text_ints = [ord(char) for char in mutq_text]
    key_ints = [ord(char) for char in key]

    key_len = len(key_ints)
    padded_key = key_ints * (len(mutq_text_ints) // key_len + 1)[:len(mutq_text_ints)]

    ciphertext_ints = []
    for i, char_int in enumerate(mutq_text_ints):
        shift = padded_key[i]
        new_int = (char_int + shift) % 256
        ciphertext_ints.append(new_int)

    ciphertext = ''.join([chr(int) for int in ciphertext_ints])

    return ciphertext