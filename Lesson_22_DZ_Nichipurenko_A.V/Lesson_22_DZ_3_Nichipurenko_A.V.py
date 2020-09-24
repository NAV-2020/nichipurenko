"""
Запрограммируйте класс Money (объект класса 
оперирует одной валютой) для работы с деньгами.
В классе должны быть предусмотрены поле для 
хранения целой части денег (доллары, евро, 
гривны и т.д.) и поле для хранения копеек 
(центы, евроценты, копейки и т.д.).
Реализовать методы для вывода суммы на экран, задания значений для частей. 
"""

class Money:
    """Class displays money balance information."""

    def __init__(self, uah:int=0, kopek:int=0, usd:int=0, cents:int=0, eur:int=0, euro_cents:int=0):
        """Initialize the object"""
        self._uah = uah
        self._kopek = kopek
        self._usd = usd
        self._cents = cents
        self._eur = eur
        self._euro_cents = euro_cents

    ######################### UAH ###########################################
    @property
    def uah(self) -> int:
        """Returning the property value"""
        return self._uah

    @uah.setter
    def uah(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._uah = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Name input error!!!')
            print('Initialization will happen with an unspecified name...')
            input('Press to continue...')
    
    @property
    def kopek(self) -> int:
        """Returning the property value"""
        return self._kopek

    @kopek.setter
    def kopek(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._kopek = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Name input error!!!')
            print('Initialization will happen with an unspecified name...')
            input('Press to continue...')
    
########################### USD #########################################
    @property
    def usd(self) -> str:
        """Returning the property value"""
        return self._usd

    @usd.setter
    def usd(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._usd = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Name input error!!!')
            print('Initialization will happen with an unspecified name...')
            input('Press to continue...')
            
    @property
    def cents(self) -> str:
        """Returning the property value"""
        return self._cents

    @cents.setter
    def cents(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._cents = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Name input error!!!')
            print('Initialization will happen with an unspecified name...')
            input('Press to continue...')
   
########################### EUR ###########################################
    @property
    def eur(self) -> str:
        """Returning the property value"""
        return self._eur

    @eur.setter
    def eur(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._eur = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Name input error!!!')
            print('Initialization will happen with an unspecified name...')
            input('Press to continue...')

    @property
    def euro_cents(self) -> str:
        """Returning the property value"""
        return self._euro_cents

    @euro_cents.setter
    def euro_cents(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._euro_cents = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Name input error!!!')
            print('Initialization will happen with an unspecified name...')
            input('Press to continue...')
   
######################################################################
   
    def __str__(self):
        return (f"""
         UAH: {self._uah} (грн.) {self._kopek} (коп.)
         USD: {self._usd} (usd) {self._cents} (cents)
         EUR: {self._eur} (eur) {self._euro_cents} (eur. cents)
         """)
    
    #def __del__(self):
        #"""Class destructor"""
        #print("Data deleted!")
    
    def display_money(self):
        '''Class method displays balance.'''
        if (self._uah != 0) or (self._kopek != 0):
            print(f"UAH: {self._uah} (грн.) {self._kopek} (коп.)")
        elif (self._usd != 0) or (self._cents != 0):
            print(f"USD: {self._usd} (usd) {self._cents} (cents)")
        elif (self._eur != 0) or (self._euro_cents != 0):
            print(f"EUR: {self._eur} (usd) {self._euro_cents} (eur. cents)")
        else:
            print("There is no money on the balance!!!")
        
if __name__ == "__main__":

    qqq = Money()
    www = Money() 
    eee = Money()

    aaa = Money()
    
    qqq.uah = 100
    qqq.kopek = 58
    
    www.usd = 26
    www.cents = 34
    
    eee.eur = 67
    eee.euro_cents = 54

    print('*'*40)
    qqq.display_money()
    www.display_money()
    eee.display_money()
    aaa.display_money()
    print('*'*40)

    print(qqq)
    print(www)
    print(eee)
    print(aaa)


