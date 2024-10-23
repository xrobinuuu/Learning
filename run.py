import argparse
import importlib


class DynamicRun:
    @classmethod
    def run(cls):
        module, function = cls._parser_args()
        module = importlib.import_module(module)
        function = getattr(module, function)
        function()

    @staticmethod
    def _parser_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--module', type=str, )
        parser.add_argument('--function', type=str, default='main')
        args = parser.parse_args()
        function = args.function
        module = args.module
        return module, function


if __name__ == '__main__':
    DynamicRun.run()
