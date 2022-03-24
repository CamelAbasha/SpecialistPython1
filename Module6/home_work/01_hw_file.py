# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
    with open(file, "r", encoding="utf-8") as f:
        lines = len(f.readlines())              #считает количество строк в файле
    with open(file, "a", encoding="utf-8") as f:
        if lines>0:
            f.write('\n'+text)                  #если файл не пустой, то переносим строку и пишем текст
        else:
            f.write(text)                       #если файл пустой, то сразу пишем текст


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
