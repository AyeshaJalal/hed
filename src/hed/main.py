def decor(f):
    print("****************")

    def wrapper():
        f()
        print("****************")

    return wrapper


@decor
def msg():
    print("🎉Hello, World!🎉")


# can be done this way
# m = decor(msg)
# m()

msg()
