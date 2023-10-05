#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for args in dir(hidden_4):
        if args[0] != "_" and args[1] != "_":
            print("{}".format(args))
