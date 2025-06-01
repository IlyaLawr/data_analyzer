from argparse import ArgumentParser


class SetupCliParser:
    def __init__(self, description: str) -> None:
        self.parser = ArgumentParser(description=description)


    def parse(self) -> list[str]:
        self.parser.add_argument('question',
                                 nargs='+',
                                 help='question text.'
        )

        return self.parser.parse_args()
