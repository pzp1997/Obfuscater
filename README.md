Obfuscater
==========

<h3>Encodes and decodes .txt documents using your randomly generated, personal key.</h3>

Thanks for trying out my program (it really means a lot to me). The purpose of this program is to encode and decode .txt (other document types may, or may not work… I know that .rtf doesn't) documents using your very own, randomly generated personal keys. The defualt key is generated for you the first time that you run the program (and all other keys are created using the same algorithm). This means that every user should (theoretically) have different keys, and I will not know what your keys are! If one tries to decode the document with a wrong key (or if a document was encoded with multiple keys, in the wrong order), gibberish will result! This program can encode and decode documents almost instantaneously, and no programming knowledge or downloads (other than the program itself) are required to get you up and running. Here are the steps to encode/decode a document:

1. Open Terminal
2. Type in the following information: 
	"python" -- Lets the Terminal know what kind of file we're running
	Path of Obfuscater.py -- Fancy name for Obfuscater's location (see example)
	"--encode" or "--decode" -- Let the program know if you want to encode or decode the document
	Path of document -- Location of the document you wish to encode/decode
	Key name (optional) -- name of the key that you would like to use to encode/decode your file
3. Press enter
4. Open the document!

…or expressed more succinctly: ./Obfuscater.py {--encode | --decode} file.txt {key_name}

For more security, you can encode a document multiple times with different keys (just remember to decode the document in the reverse order that it was encoded!).

NOTE: I cannot guarantee that others will not be able to decode your document. The security that Obfuscater uses is far from foolproof. So with that being said, don't use Obfuscater to protect "state secrets" or classified documents. I will not be held responsible for any damages incurred as a result of your using of Obfuscater, including if a document encoded by Obfuscater was decoded by an unintended party.

I hope you find this program useful! <br/>
<strong>Palmer Paul (pzp1997)</strong>

P.S. If you have any bug reports (please include the error message!), feature ideas, or just want to chat about Python in general, send me an email at pzpaul2002@yahoo.com or a <a href="https://twitter.com/pzp1997">tweet</a>.

