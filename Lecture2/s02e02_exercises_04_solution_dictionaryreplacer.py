def replace(text, dict):
    for key in dict.keys():
        text = text.replace(f'${key}$', dict[key])
    return text


def test(args, expected):
    actual = replace(args[0], args[1])
    print(f'Expected: {expected:20} Actual: {actual:20} {"OK" if expected == actual else "ER"}')


test(('', {}), '')
test(('aaa', {}), 'aaa')
test(('$x$', {'x': 'test'}), 'test')
test(('$temp$', {'temp': 'temporary'}), 'temporary')
test(('$temp$ here comes the name $name$', {'temp': 'temporary', 'name': 'John Doe'}), 'temporary here comes the name John Doe')
