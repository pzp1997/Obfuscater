#!/usr/local/bin/python

from random import choice
from json import dump, load
from sys import argv

def randCode():
    char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", " "]
    copy = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", " "]
    encode = {}
    decode = {}
    for x in range(len(char)):
        randChar = choice(copy)
        encode[char[x]] = randChar
        decode[randChar] = char[x]
        copy.remove(randChar)
    return (encode, decode)
    
def loadCode(filename):
    try:
        fp_read = open(filename, "r")
        try:
            data_read = load(fp_read)
        except ValueError:
            data_read = randCode()
            fp_write = open(filename, "w")
            dump(data_read, fp_write)
            fp_write.close()
        fp_read.close()
    except IOError:
        data_read = randCode()
        create = open(filename, "w")
        dump(data_read, create)
        create.close()
    return data_read

def coder(s, d):
    s_new = ""
    for x in range(len(s)):
        try:
            s_new = s_new + d[s[x]]
        except KeyError:
            s_new = s_new + s[x]
    return s_new

def main():
    if len(argv) != 3:
        print "usage: ./Obfuscater.py {--encode | --decode} file.txt"
        raise SystemExit

    codes = loadCode("DefaultKey.txt")
    encoder = codes[0]
    decoder = codes[1]
    
    filename = argv[2]
    read = open(filename, "r")
    text = read.read()
    read.close()

    option = argv[1]
    if option == "--encode" or option == "--decode":
        if option == "--encode":
            codedText = coder(text, encoder)
            print "Document sucessfully encoded!"
        else:
            codedText = coder(text, decoder)
            print "Document sucessfully decoded!"
        write = open(filename, "w")
        write.write(codedText)
        write.close()
    else:
        print "unknown option: " + option
        raise SystemExit

if __name__ == "__main__":
    main()
