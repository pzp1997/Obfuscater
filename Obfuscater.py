#!/usr/local/bin/python

from random import choice
from json import dump, load
from sys import argv

def genCode():
    char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", " "]
    copy = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", " "]
    encode = {}
    decode = {}
    for x in range(len(char)):
        randChar1 = choice(char)
        randChar2 = choice(copy)
        encode[randChar1] = randChar2
        decode[randChar2] = randChar1
        char.remove(randChar1)
        copy.remove(randChar2)
    return (encode, decode)
    
def loadCode():
    filename = "ObfuscaterKeys.txt"
    cleanLoad = False
    try:
        fp_read = open(filename, "r")
        try:
            data_read = load(fp_read)
            cleanLoad = True
        except ValueError:
            data_read = {"Default": genCode()}
            fp_write = open(filename, "w")
            dump(data_read, fp_write)
            fp_write.close()
        fp_read.close()
    except IOError:
        data_read = {"Default": genCode()}
        create = open(filename, "w")
        dump(data_read, create)
        create.close()
    return (data_read, cleanLoad)

def addCode(name):
    codeData = loadCode()
    codeStatus = codeData[1]
    if codeStatus:
        codeFile = codeData[0]
        newCode = genCode()
        codeFile[name] = newCode
        fp_write = open("ObfuscaterKeys.txt", "w")
        dump(codeFile, fp_write)
        fp_write.close()
        return True
    else:
        return False

def coder(s, d):
    s_new = ""
    for x in range(len(s)):
        try:
            s_new = s_new + d[s[x]]
        except KeyError:
            s_new = s_new + s[x]
    return s_new

def main():
    if len(argv) != 3 and len(argv) != 4:
        if len(argv) == 2 and argv[1] == "--list":
            codeNames = list(loadCode()[0].keys())
            for x in range(len(codeNames)):
                print codeNames[x]
        else:
            print "usage: ./Obfuscater.py {--encode | --decode} file.txt {key_name}"
        raise SystemExit

    codeFile = loadCode()[0]
    if len(argv) == 3:
        codes = codeFile["Default"]
    else:
        try:
            codes = codeFile[argv[3]]
        except KeyError:
            print "Key name \"" + argv[3] + "\" not recognized."
            if argv[3].isalpha():
                addSuccess = addCode(argv[3])
                if addSuccess:
                    print "A new key has been created with that name."
            raise SystemExit
        
    filename = argv[2]
    read = open(filename, "r")
    text = read.read()
    read.close()

    option = argv[1]
    if option == "--encode" or option == "--decode":
        if option == "--encode":
            codedText = coder(text, codes[0])
            action = "encoded"
        else:
            codedText = coder(text, codes[1])
            action = "decoded"
        write = open(filename, "w")
        write.write(codedText)
        write.close()
        print "Document successfully " + action + "!"
    else:
        print "unknown option: " + option
        raise SystemExit

if __name__ == "__main__":
    main()
