class ChangePrint:
    def __enter__(self):
        global print
        self.old_print = print
        print = lambda *args, **kwargs: self.old_print('HACKED!!!', *args, **kwargs)

    def __exit__(self, *sys_exc):
        global print
        print = self.old_print


def main():
    print('Hello World!')

if __name__ == '__main__':
    main()

    with ChangePrint():
        main()

        print('Ha HA HA')

    main()

    print('hellooooo')