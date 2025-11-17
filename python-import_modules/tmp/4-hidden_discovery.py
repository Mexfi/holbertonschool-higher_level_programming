#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # dir() moduldakı bütün adları verir
    names = sorted(dir(hidden_4))
    for name in names:
        if not name.startswith("__"):  # __ ilə başlayan adları çıxart
            print(name)
