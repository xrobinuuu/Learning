


import pandas as pd


class Rank:

    def __init__(self, data_input: list[int | float]):
        self.data_input = data_input

    @timer
    def output(self, reverse: bool = False) -> list[tuple[int, int | float]]:
        sorted_data = sorted(set(self.data_input), reverse=reverse)
        rank_mapping = dict(zip(sorted_data, range(1, len(sorted_data) + 1)))
        return sorted([(rank_mapping[d], d) for d in self.data_input], key=lambda d: d[0], reverse=False)

    @timer
    def output2(self, reverse: bool = False) -> list[tuple[int, int | float]]:
        df = pd.DataFrame(data=self.data_input, columns=['score'])
        df['rank'] = df.rank(method='dense', ascending=reverse)
        df.sort_values(by='rank', inplace=True)
        return df.to_dict('split')['data']


if __name__ == '__main__':
    d_input = [4.00, 3.50, 3.65, 3.85, 3.65, 4.00]

    Rank(data_input=d_input).output(reverse=True)
    result = Rank(data_input=d_input).output2(reverse=False)
    print(result)
