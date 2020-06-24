import xlwings as xw


@xw.func
def hello(name):
    return 'Hello {0}'.format(name)


print(hello("maricio"))
