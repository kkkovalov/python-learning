def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func('Hello, I am new here! YAY')
    print(greeting)
    
    
greet(shout)