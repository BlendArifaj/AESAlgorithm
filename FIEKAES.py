class FIEKAES():
    import base64
    import hashlib
    from Crypto import Random
    from Crypto.Cipher import AES
    #Blendi
    def __init__(self): 
        #block size (16/32)
        self.bs = 16
        self.celesi = self.celesi()
        
    def celesi(self):
        import random
        qelesi  = ''.join(chr(random.randint(0,0xFF)) for i in range(16))
        return hashlib.sha256(celesi.encode()).digest()
    
    def vektoriInicializues(self):
        #iv generation (needed for cbc mode implementation)
        return Random.new().read(AES.block_size)
    
    def kontrollo(self, text, tekstiDekriptuar):
        if text == tekstiDekriptuar:
            print("Dekriptimi eshte kryer me sukses")
        else:
            print("Gabim gjate dekriptimit")
    #Arianiti
    def enkripto(self, teksti):
        teksti = self._pad(teksti)
        iv = self.vektoriInicializues()
        cipher = AES.new(self.celesi, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(teksti))
    
    #Fjolla
    def dekripto(self, tekstiEnkriptuar):
        tekstiEnkriptuar = base64.b64decode(tekstiEnkriptuar)
        iv = tekstiEnkriptuar[:AES.block_size]
        cipher = AES.new(self.celesi, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(tekstiEnkriptuar[AES.block_size:])).decode('utf-8')

    
    
    
