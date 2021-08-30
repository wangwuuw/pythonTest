def decrypts(text):
    from Crypto.Cipher import AES
    from binascii import b2a_hex, a2b_hex

    encrypt_mod = AES.MODE_CBC
    key = "CryptoExchangeAESRandomSecureKey".encode(encoding="utf-8")
    iv = text[4:20].encode(encoding="utf-8")

    cryptor = AES.new(key, encrypt_mod, iv)
    encrypt_text = a2b_hex(text[25:])
    plain_text = cryptor.decrypt(encrypt_text)
    return (
        plain_text.decode("utf-8")
            .rstrip("\0")
            .replace(text[4:20], "")
    )
s = decrypts("AES:4f63abb9c7c33c43100007a2cfbd90c3a4c8ce6f1cc99f1652eeee4a11eb8bb67e54f6a66f9cbd04f4122");
print(s);