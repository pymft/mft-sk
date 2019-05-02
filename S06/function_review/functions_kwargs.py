def fun(*args, **kwargs):
    print(args)
    print(kwargs)
    # kwargs['mode']
    mode = kwargs.get('mode', 'nothing')
    print(mode)


fun(1, 2, 3, 4, 5, state='nothing', val=1)