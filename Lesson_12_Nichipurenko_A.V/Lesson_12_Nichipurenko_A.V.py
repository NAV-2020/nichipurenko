
"""
def make_code_better(foo):
    def  wrapper():
        print("Wrapper is started")
        func()
        print("Hello")
        return wrapper

@ make_code_better
def foo():
    print("My coe is exec")

foo()


def connection()ip: str, port: int):

    def make_connection(printer_function):
        def connection(printer):
            def wrapper(mode: str, color: str):
                print('*'*10)
                printer(model=model, color=color)
                print('*'*10)
            return wrapper
        return make_connection

@connection(ip:'192.168.10.2', port: int)
def hp_printer(mode: str, color: str):
    # OS API CONNECT...
    print('Model:', model)
    print('Color', color)

if __name__ == "__main__":
    #! printer_models = ['hp', 'sumsung']
    hp = hp_printer
    hp(model='HP', color='red')
    

def benchmark(inter):
    def decorator(func):
        import time
        
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start_time = time.time()
                return_value = func(*args, **kwargs)
                end_time = time.time90
                totel = totel + (end_time - start_time)

            print()
"""