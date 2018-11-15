"""This module provides the syntax to form propositional logic."""


class Sentence:
    """Sentence is formed from simple Symbols."""

    def __init__(self, op, *args):
        """
        Construct a sentence from operator/name and optional args.

        :param op: operator
        :param args: optional arguments
        """
        self.op = op
        self.args = args

    def implies(self, sentence):
        pass

    def iff(self, sentence):
        pass

    def __eq__(self, other):
        return (isinstance(other, Sentence) and self.op == other.op
                and self.args == other.args)


class Symbol:
    """A symbol is an atomic sentence with only a single proposition symbol."""

    def __new__(cls, *args, **kwargs):
        if len(args) > 1:
            symbols = list()
            for symbol in args:
                o = super().__new__(cls)
                o.__init__(symbol)
                symbols.append(o)
            return symbols
        else:
            return super().__new__(cls)

    def __init__(self, symbol):
        """
        Construct a new Symbol.
        """
        self._symbol = symbol

    def __eq__(self, other):
        return type(self) == type(other) and self._symbol == other._symbol

    def __str__(self):
        return self._symbol
