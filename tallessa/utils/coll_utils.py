from collections import namedtuple

Node = namedtuple('Node', 'key leaves branches')


def to_prefix_tree(items):
    """
    Given an iterable of iterables (such as a list of tuples of strings), turns them into a tree
    with common prefixes grouped together.

    >>> to_prefix_tree([
    ...     ('Apple', 'iPhone', '64GB', 'Space', 'Gray'),
    ...     ('Apple', 'iPhone', '64GB', 'Rose', 'Gold'),
    ...     ('Apple', 'iPad', 'Air', '2', '64GB', 'Space', 'Gray'),
    ...     ('Apple', 'MacBook', 'Pro')
    ... ])
    Node(key='Apple', leaves=[('MacBook', 'Pro')], branches=[
        Node(key='iPhone', leaves=[], branches=[
            Node(key='64GB', leaves=[
                ('Space', 'Gray'),
                ('Rose', 'Gold')
            ], branches=[])
        ]),
        Node(key='iPad', leaves=[
            ('Air', '2', '64GB', 'Space', 'Gray')
        ], branches=[])
    ])
    """
