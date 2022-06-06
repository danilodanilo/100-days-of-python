# unlimited arguments to functions example
def add(*args):
    print(type(args))
    sum_total = 0
    for n in args:
        sum_total += n
    return sum_total


print(add(2, 10, 20, 30))


# unlimited key word arguments example
def calculate(n, **kwargs):
    n += kwargs["add_value"]
    n *= kwargs["multiply_value"]

    print(n)
    # loop over dict
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(2, add_value=3, multiply_value=5)


# optional argument when initializing an object
class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        # line 31 and 32 can be done this way for avoiding errors, by doing so, kwargs can be empty
        self.make = kwargs.get("make")
        self.make = kwargs.get("model")


my_car = Car(make="Nissan")
# print(my_car.model)
print(my_car.make)
