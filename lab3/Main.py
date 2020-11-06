from SyT import SymbolTable
from Scanner import *
from PIF import *

if __name__ == "__main__":
    fileName = "token.in"
    scanner = Scanner()


    with open(fileName,"r") as file:
        for line in file:
            print([token for token in scanner.getTokens(line)])

    symbolTable = SymbolTable()
    pif = ProgramInternalForm()
    with open(fileName,"r")as file:
        lineNumber =0
        for line in file:
            lineNumber += 1
            line = line.replace('\n','')
            for token in scanner.getTokens(line):
                if token == '' or token =='\n' or token == ' ':
                    pass
                elif scanner.verifySeparator(token) or scanner.verifyOperator(token) or scanner.verifyReservedWords(token):
                    pif.add(scanner.codification[token],-1)
                elif scanner.verifyConstant(token):
                    id = symbolTable.add(token)
                    pif.add(scanner.codification['constant'], id)
                elif scanner.verifyIdentifier(token):
                    id = symbolTable.add(token)
                    pif.add(scanner.codification['identifier'],id)
                else:
                    raise Exception('Unknown token ' + token + ' at line ' + str(lineNumber))
    outPif = open("pif.txt", "w")
    outSt = open("St.txt", "w")
    outCodification = open("codification.txt", "w")
    outSt.write(str(symbolTable))
    outPif.write(str(pif))
    s = ""
    for x, y in scanner.codification.items():
        s += (str(x) + " " + str(y) + '\n')
    outCodification.write(s)

