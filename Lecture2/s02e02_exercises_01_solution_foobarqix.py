# Filip's solution to https://codingdojo.org/kata/FooBarQix/

def fooBarQix(number_as_str):
    i = int(number_as_str)
    result = ""

    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or\
        "3" in number_as_str or "5" in number_as_str or "7" in number_as_str:
        if i % 3 == 0: result += "Foo"
        if i % 5 == 0: result += "Bar"
        if i % 7 == 0: result += "Qix"
        appendix = number_as_str \
            .replace("3", "Foo") \
            .replace("5", "Bar") \
            .replace("7", "Qix") \
            .replace("0", "*") \
            .replace("1", "") \
            .replace("2", "") \
            .replace("4", "") \
            .replace("6", "") \
            .replace("8", "") \
            .replace("9", "")
        result += appendix
    else:
        result = number_as_str.replace("0", "*")

    return result


print(fooBarQix("1"))
print("1")

print(fooBarQix("3"))
print("FooFoo")

print(fooBarQix("5"))
print("BarBar")

print(fooBarQix("6"))
print("Foo")

print(fooBarQix("7"))
print("QixQix")

print(fooBarQix("15"))
print("FooBarBar")

print(fooBarQix(str(3*5*7)))
print("FooBarQixBar")

print(fooBarQix("153"))
print("FooBarFoo")

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 21, 33, 51, 53, 101, 303, 105, 10101]:
    print(f"{x} => {fooBarQix(str(x))}")