#! /usr/bin/env python

import sayhello

# these are explicitly defined in the people and things namespaces of the
# sayhello module.
sayhello.people.hello_bob()
sayhello.things.hello_chair()

# hello_frank and hello_table are not defined in the people and things
# namespaces by default.
print "hello_frank in people:", 'hello_frank' in dir(sayhello.people)
print "hello_table in things:", 'hello_table' in dir(sayhello.things)

# populate the namespaces with additional function defined in the extra
# directory.
sayhello.extra.populate_namespace_with_extra()

sayhello.people.hello_frank()
sayhello.things.hello_table()

# hello_frank and hello_table are now defined in the people and things
# namespaces.
print "hello_frank in people:", 'hello_frank' in dir(sayhello.people)
print "hello_table in things:", 'hello_table' in dir(sayhello.things)
