__author__ = 'Fossum'


class foo():
    notagoodidea = "what am I now?"
    pass

object1 = foo()
object1.notagoodidea = "who knows"
object2 = object1
object2.notagoodidea = "who's on first?"
print(foo.notagoodidea)
