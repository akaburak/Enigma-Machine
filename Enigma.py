# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:22:24 2022

@author: burak
"""
#DICTIONARY
word_dict = {"a":2,"s":22,"d":222,
             "f":2222,"g":22222,"h":222222,
             "j":2222222,"k":22222222,
             "l":222222222,"ş":2222222222,
             "i":22222222222,"q":222222222222,
             "w":2222222222222,"e":22222222222222,
             "r":222222222222222,"t":2222222222222222,
             "u":222222222222222222,"ı":2222222222222222222,
             "o":22222222222222222222,"p":222222222222222222222,
             "ü":22222222222222222222222,
             "z":222222222222222222222222,
             "x":2222222222222222222222222,
             "c":22222222222222222222222222,
             "v":222222222222222222222222222,
             "b":2222222222222222222222222222,
             "n":22222222222222222222222222222,
             "m":222222222222222222222222222222,
             "ö":2222222222222222222222222222222,
             "ç":22222222222222222222222222222222,
             "y":222222222222222222222222222222222,
             ",":3,".":33,"'":333}

#ENCODER
def encoder(file,word_dict):
    encoder_file = open(file,"r")
    file_write = open("encoded_file.txt","w")
    pre_file = encoder_file.read()
    word_list = pre_file.split(" ")
    sentence = ""
    for word in word_list:
        for char in word:
            sentence+=str(word_dict[char.lower()])
            sentence+="0"
        sentence+="1"
    file_write.write(sentence)
    return sentence

#DECODER
def decoder(file,word_dict):
    decoder_file = open(file,"r")
    decoder_file_write = open("decoded_file.txt","w")
    decoder_pre_file = decoder_file.read()
    decoder_list = decoder_pre_file.split("1")
    decoded_sentence = ""
    for word in decoder_list:
        char_list = word.split("0")
        for char in char_list:
            for i in word_dict:
                if str(char) == str(word_dict[i]):
                    decoded_sentence+=i
        decoded_sentence+=" "
    decoder_file_write.write(decoded_sentence)
    return decoded_sentence

print(encoder("enigma.txt",word_dict))
print(decoder("encoded_file.txt",word_dict))