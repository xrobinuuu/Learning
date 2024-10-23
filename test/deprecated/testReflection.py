from ppppackage import testReflection2

imp = __import__('ppppackage.testReflection2')


def reflect():
    fun = getattr(testReflection2, 'ref')
    fun()


b = getattr(testReflection2, "a")
print(b)
reflect()
d = getattr(imp, "a")
print(d)
