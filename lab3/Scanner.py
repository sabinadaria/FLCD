from SyT import SymbolTable
import re


class Scanner:
    def __init__(self):
        self.st = SymbolTable
        self._listOperators = ["+", "-", "*", "/", "%", "is", "<", ">", "<=", ">=", "="]
        self._listSeparators = ["{", "}", ":", "(", ")", ","]
        self._listReservedWords = ["if", "else", "for", "is", "to", "by", "and", "or", "while", "iGot", "youGot",
                                   "myNameIs", "iamNumber", "iamBoolean", "iamChar", "True", "False"]

        temp = self._listSeparators
        everything = temp + self._listOperators + self._listReservedWords
        self.codification = {'identifier': 0, 'constant': 1}
        for i in range(len(everything)):
            self.codification[everything[i]] = i + 2

    def verifyOperator(self, token):
        return token in self._listOperators

    def verifySeparator(self, token):
        return token in self._listSeparators

    def verifyReservedWords(self, token):
        return token in self._listReservedWords

    def verifyConstant(self, token):
        for c in token:
            if c not in "0123456789":
                return False
        return True

    def verifyIdentifierVariable(self, token):
        if token[0] != "^":
            return False
        i = 1
        while (i < len(token) - 1):
            if not token[i].isalpha():
                return False
            i = i + 1
        if token[-1] != "^":
            return False
        return True

    def verifyVector(self,token):
        if token[0] != "^" or token[1] != "^":
            return False
        i = 2
        while (i < len(token) - 2):
            if not token[i].isalpha():
                return False
            i = i + 1
        if token[-1] != "^" or token[-2] != "^":
            return False
        return True

    def verifyIdentifier(self, token):
        if not self.verifyIdentifierVariable(token) and not self.verifyVector(token):
            return False
        else:
            return True

    def getTokensByOperators(self, line):
        return re.split(r'([\+|-|\*|/|%|<|>|<=|>=]|is)', line)

    def getTokens(self, line):
        x = re.split(r'([{}:\(\), ])', line)
        y = []
        for i in range(len(x)):
            if not self.verifyOperator(x[i]) and not self.verifySeparator(x[i]) and not self.verifyReservedWords(
                    x[i]) and not self.verifyConstant(x[i]) and not self.verifyIdentifier(x[i]):
                if any(operator in x[i] for operator in self._listOperators):
                    y.extend(self.getTokensByOperators(x[i]))
                    y = list(filter(lambda a: a != '' and a != '\n', y))
                else:
                    y.append(x[i])
            else:
                y.append(x[i])
        y = list(filter(lambda a: a != '' and a != '\n', y))
        return y
