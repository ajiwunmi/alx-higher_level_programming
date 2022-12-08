def muilt_by_num(num):
    return num * 2


def do_math(func, num):
    return func(num)


# print("8 * 2= ", do_math(muilt_by_num, 8))


def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value

    return mult_by


generated_func = get_func_mult_by_num(5)

# print("10 * 2 = {}".format(generated_func(10)))

lifOffuncs = [muilt_by_num, generated_func]

print("5 * 9 = ", lifOffuncs[1](9))
print("5 * 9 = ", lifOffuncs[0](9))
