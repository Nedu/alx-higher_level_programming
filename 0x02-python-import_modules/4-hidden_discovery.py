#!/usr/bin/python3

if __name__ == "__main__":
    """Print all the names defined by the compiled module"""
    import hidden_4

    for name in dir(hidden_4):
        if name[:2] != "__":
            print(name)
