#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    arr = dir(hidden_4)
    for i in arr:
        if i[0:2] != "_":
            print(i)
