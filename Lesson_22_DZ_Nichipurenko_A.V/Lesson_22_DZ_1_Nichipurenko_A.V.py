'''
Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте класс
CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые
для работы методы.
'''
class Device:
    """Class with general device information."""

    valDevice = 0
    
    def __init__(self, device: str = "not set", serial_num: int = 0):
        """Initialize the object"""
        self._device = device
        self._serial_num = serial_num

        Device.valDevice += 1

    #def __del__(self):
        #"""Class destructor"""
        #Device.valDevice -= 1
        #print(f"Left:{Device.valDevice}")

    @property
    def device(self) -> str:
        """Returning the property value"""
        return self._device

    @device.setter
    def device(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._device = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Name input error!!!')
            print('Initialization will happen with an unspecified name...')
            input('Press to continue...')
    
    @property
    def serial_num(self) -> int:
        """Returning the property value"""
        return self._serial_num

    @serial_num.setter
    def serial_num(self, serial_num):
        """Setting property value"""
        if isinstance(serial_num, int):
            self._serial_num = serial_num
        else:
            print('Serial number entry error!!!')
            print('The serial number will be initialized by default...')
            input('Press to continue...')

    def __str__(self):
        """Method returns a representation of the object"""
        return f'''
        Device: {self._device}
        Serial number: {self._serial_num}'''


class CoffeeMachine(Device):
    """The class presents information about the coffee machine."""

    def __init__(self, breand: str = 'Undefined', power: int = 0):
        """Initialize the object"""
        super().__init__(self)
        self._breand = breand
        self._power = power

    @property
    def breand(self) -> int:
        """Returning the property value"""
        return self._breand

    @breand.setter
    def breand(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._breand = val
        else:
            print('BREAND input ValueError!!!')
            print('Initialization will take place by default...')
            input('Press to continue...')

    @property
    def power(self) -> int:
        """Returning the property value"""
        return self._power

    @power.setter
    def power(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._power = val
        else:
            print('POWER input ValueError!!!')
            print('Initialization will take place by default ...')
            input('Press to continue...')
    
    def __str__(self):
        """Method returns a representation of the object"""
        return f'''
        {super().__str__()}
        Brand: {self._breand}
        Pover: {self._power} (W)
        '''

class Blender(Device):
    """The class represents information about the blender."""

    def __init__(self, breand: str = 'Undefined', power: int = 0, speed: int = 0 ):
        """Initialize the object"""
        super().__init__(self)
        self._breand = breand
        self._power = power
        self._speed = speed

    @property
    def breand(self) -> int:
        """Returning the property value"""
        return self._breand

    @breand.setter
    def breand(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._breand = val
        else:
            print('BREAND input ValueError!!!')
            print('Initialization will take place by default...')
            input('Press to continue...')

    @property
    def power(self) -> int:
        """Returning the property value"""
        return self._power

    @power.setter
    def power(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._power = val
        else:
            print('POWER input ValueError!!!')
            print('Initialization will take place by default ...')
            input('Press to continue...')

    @property
    def speed(self) -> int:
        """Returning the property value"""
        return self._speed

    @speed.setter
    def speed(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._speed = val
        else:
            print('SPEED input ValueError!!!')
            print('Initialization will take place by default ...')
            input('Press to continue...')
    
    def __str__(self):
        """Method returns a representation of the object"""
        return f'''
        {super().__str__()}
        Brand: {self._breand}
        Pover: {self._power} (W)
        Speed: {self._speed} (rpm)
        '''

class MeatGrinder(Device):
    """The class presents information about the grinder."""

    def __init__(self, breand: str = 'Undefined', power: int = 0, nozzle: int = 0 ):
        """Initialize the object"""
        super().__init__(self)
        self._breand = breand
        self._power = power
        self._nozzle = nozzle

    @property
    def breand(self) -> int:
        """Returning the property value"""
        return self._breand

    @breand.setter
    def breand(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._breand = val
        else:
            print('BREAND input ValueError!!!')
            print('Initialization will take place by default...')
            input('Press to continue...')

    @property
    def power(self) -> int:
        """Returning the property value"""
        return self._power

    @power.setter
    def power(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._power = val
        else:
            print('POWER input ValueError!!!')
            print('Initialization will take place by default ...')
            input('Press to continue...')

    @property
    def nozzle(self) -> int:
        """Returning the property value"""
        return self._nozzle

    @nozzle.setter
    def nozzle(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._nozzle = val
        else:
            print('NOZZLE input ValueError!!!')
            print('Initialization will take place by default ...')
            input('Press to continue...')
    
    def __str__(self):
        """Method returns a representation of the object"""
        return f'''
        {super().__str__()}
        Brand: {self._breand}
        Pover: {self._power} (W)
        Nozzle: {self._nozzle} (pieces)
        '''

if __name__ == "__main__":
    
    q = CoffeeMachine()
    w = Blender()
    e = MeatGrinder()

    q.device = 'Coffee Machine'
    q.serial_num = 1111
    q.breand = 'Domotec'
    q.power = 100
    print(q)
    print("-"*40)

    w.device = 'Blender'
    w.serial_num = 2222
    w.breand = 'Saturn'
    w.power = 100
    w.speed = 800
    print(w)
    print("-"*40)

    e.device = 'Meat Grinder'
    e.serial_num = 3333
    e.breand = 'MOULINEX'
    e.power = 400
    e.nozzle = 4
    print(e)
    
    print("-"*40)
    print(Device.valDevice)
    print("-"*40)
