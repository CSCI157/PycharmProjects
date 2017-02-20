__author__ = 'Fossum'

import copy


class Foo:
    notagoodidea = "what am I now?"
    pass

object1 = Foo()
object1.notagoodidea = "who knows"
object2 = object1
object2.notagoodidea = "who's on first?"
object3 = copy.copy(object1)
object3.notagoodidea = "I'm lost"

print(Foo.notagoodidea, id(Foo.notagoodidea))
print(object1.notagoodidea, id(object1.notagoodidea))
print(object2.notagoodidea, id(object2.notagoodidea))
print(object3.notagoodidea, id(object3.notagoodidea))