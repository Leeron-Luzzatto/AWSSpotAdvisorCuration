from DataLoaders.Concrete.SpotAdvisorDataLoader import SpotAdvisorDataLoader
from DataLoaders.Concrete.SpotPriceDataLoader import SpotPriceDataLoader


def main():
    for loader in (SpotAdvisorDataLoader(), SpotPriceDataLoader()):
        loader.fetch()


if __name__ == '__main__':
    main()
