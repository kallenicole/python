class Secret():
    def __init__(self):
        self._secret = 99
        self.__super_secret = 1001
    
    def _createSecret_(self):
        var = self._secret
        return var

    def __superCreateSecret__(self):
        var = self.__super_secret
        return var
        #print(self.__super_secret)
        #return self.__super_secret

kalleSecret = Secret()

print(kalleSecret._secret)
print(kalleSecret.__super_secret)
print(kalleSecret._createSecret_())
print(kalleSecret.__superCreateSecret__())