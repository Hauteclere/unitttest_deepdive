import unittest
from unittest.mock import Mock, patch
from game import get_input, main_loop
from src import BreakingMock

class LoopException(Exception):
    pass

class TestCase(unittest.TestCase):
    def test_get_input_raises_exception(self):
        my_mock = BreakingMock(values_to_return=["\quit"], exception_to_raise=LoopException)

        with patch('builtins.input', my_mock):
            with self.assertRaises((KeyboardInterrupt), msg="The get_input function needs to raise a KeyboardInterrupt exception when the user wants to quit!"):
                    user_input = get_input("giff numba")
                
    def test_can_quit_from_main_loop(self):
        my_mock = BreakingMock(values_to_return=["\quit"], exception_to_raise=LoopException)
        
        with patch('builtins.input', my_mock):
            try:
                main_loop()
            except LoopException:
                self.fail("The program does not quit if the user enters '\quit' for the first prompt.")
            except:
                self.fail("Your code generates an uncaught exception!")

    def test_can_quit_mid_game(self):
        my_mock = BreakingMock(values_to_return=["", "\quit"], exception_to_raise=LoopException)
        with patch('builtins.input', my_mock):
            try:
                main_loop()
            except LoopException:
                self.fail("The program does not quit if the user enters '\quit' for the first prompt.")
            except:
                self.fail("Your code generates an uncaught exception!")  