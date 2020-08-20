def foo(args):
    args.insert(args.index(args[-1]), 2)
    args.pop(0)

numbers = replica = [3,4,5,6]

foo(replica)
print(replica)