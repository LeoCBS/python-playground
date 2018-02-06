# bogus.py
#
# Bogus example of a generator that produces and receives values


def countdown(n):
    print("Counting down from {}".format(n))
    while n >= 0:
        newvalue = (yield n)
        print("getting new value {}".format(newvalue))
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


c = countdown(5)
for x in c:
    # call coroutine always that call x
    print(x)
    if x == 5:
        c.send(3)
