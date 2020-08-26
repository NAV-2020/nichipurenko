

def get_footballers():
    return footballers

def add_footaller(name: str, surname: str, age: int):
    footballer = {
    name: name,
    surname: surname,
    age: age
}

footballers.append(footballer)

def pprint(*args):
    print("--------")
    for i in args:
        print(i)
    print("--------")

if __name__ == "__main__":
    fs = get_footballers()
    pprint(fs)

add_footaller(
    name = "and",
    surname = "surname",
    age = 25
)    