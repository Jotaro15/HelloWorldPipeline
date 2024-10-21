# Est aussi le fichier main.py de l'exercice 2 de l'examen

def addition(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Les deux arguments doivent être des nombres (int ou float)")
    return a + b

if __name__ == "__main__":
    print("Hello, World, it's us!")
    print(f"3 + 5 = {addition(3, 5)}")