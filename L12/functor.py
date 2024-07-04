class WalletFunctor:
    def __init__(self, coins=0):
       self.__startCoins = self.__startCoins + coins
       return self.__startCoins
    def __str__(self):
        return f"{self.__startCoins}"

w = WalletFunctor

print(w(50))
print(w)


