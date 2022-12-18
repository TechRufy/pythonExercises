import asyncio


@asyncio.coroutine
def DefaultHandlet(succesor=None):
    while True:
        Interi = (yield)

        print("Richiesta {0} gestita da Default_Handler: non è stato possibile gestire la richiesta {1}".format(Interi,
                                                                                                                Interi))


@asyncio.coroutine
def gestoreHandler_04(succesor=None, default=None):
    while True:
        Interi = (yield)
        succesor.send(None)
        default.send(None)

        if not isinstance(Interi[0], int) or Interi[0] < 0:
            default.send(Interi)
        elif 0 <= Interi[0] <= 4:
            print("Richiesta {0} gestita da Handler_04".format(Interi))
        elif succesor is not None:
            succesor.send(Interi)


@asyncio.coroutine
def gestoreHandler_59(succesor=None, default=None):
    while True:
        Interi = (yield)
        succesor.send(None)
        default.send(None)

        if Interi[0] < 0 or not isinstance(Interi[0], int):
            default.send(Interi)

        elif 5 <= Interi[0] <= 9:
            print("Richiesta {0} gestita da Handler_59".format(Interi))
        elif succesor is not None:
            succesor.send(Interi)


@asyncio.coroutine
def gestoreHandler_gt9(succesor=None, default=None):
    while True:
        Interi = (yield)
        ##succesor.send(None)
        default.send(None)

        if Interi[0] < 0 or not isinstance(Interi[0], int):
            default.send(Interi)

        elif 0 < Interi[0]:
            print(
                "Messaggio da Handler_gt9: non è stato possibile gestire la richiesta {0}. Richiesta modificata".format(
                    Interi))
            Interi[0] = Interi[0] - Interi[1]
            prendirequest(Interi)


def prendirequest(Event):
    pipeline = gestoreHandler_04(gestoreHandler_59(gestoreHandler_gt9(default=DefaultHandlet()), DefaultHandlet()),
                                 DefaultHandlet())

    pipeline.send(None)
    pipeline.send(Event)


def main():
    ListEvent = [[1, 3], [5, 7], [10, 3], ["ciao", 3], [15,1]]
    for event in ListEvent:
        prendirequest(event)


if __name__ == "__main__":
    main()
