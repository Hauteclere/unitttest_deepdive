import ast
import inspect
from unittest.mock import Mock

def uses_for(fn, statement):
    """Tests if a given function uses a given statement - ex, `ast.For`. Available statements are listed here: https://docs.python.org/3/library/ast.html"""
    nodes = ast.walk(ast.parse(inspect.getsource(fn)))
    return any(isinstance(node, statement) for node in nodes)

def uses_nesting(fn, statement):
    """Tests if a given function contains a nested statement - ex, a nested for loop."""
    nodes = [node for node in ast.walk(ast.parse(inspect.getsource(fn))) if isinstance(node, statement)]
    for node in nodes:
        subnodes = [subnode for subnode in ast.walk(node) if isinstance(subnode, statement)]
        if len(subnodes) > 1:
            return True
    return False

class BreakingMock(Mock):
    """Returns the values it is initialised with, and then raises an exception when no more values are available."""

    def __init__(self, *args, values_to_return=[], exception_to_raise=KeyboardInterrupt, **kwargs):
        super().__init__(*args, **kwargs)
        self.values_to_return = values_to_return
        self.exception_to_raise = exception_to_raise
        self.side_effect = self.return_value_or_raise_exception
        

    def return_value_or_raise_exception(self, *args, **kwargs):
        if self.values_to_return:
            return self.values_to_return.pop(0)
        else:
            raise self.exception_to_raise("The loop was terminated by the test suite.")