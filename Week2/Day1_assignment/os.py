import os

def count_files():
    files = os.listdir('.')
    txt = 0
    py = 0

    for file in files:
        if file.endswith('.txt'):
            txt += 1
        elif file.endswith('.py'):
            py += 1

    print("Text files: ",txt)
    print("Python files: ",py)

count_files()