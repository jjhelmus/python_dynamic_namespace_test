def populate_namespace_with_extra():

    # add hello_frank function to people namespace
    from .. import people
    from .frank import hello_frank
    people.hello_frank = hello_frank

    # add hello_table to things namespace
    from .. import things
    from .table import hello_table
    things.hello_table = hello_table
