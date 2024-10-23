import copy


class MaxProfit:
    @staticmethod
    def gaussian_elimination(a, b):
        a, b = copy.deepcopy(a), copy.deepcopy(b)
        n = len(a)
        for i in range(n):
            max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
            a[i], a[max_row] = a[max_row], a[i]
            b[i], b[max_row] = b[max_row], b[i]
            for j in range(i + 1, n):
                factor = a[j][i] / a[i][i]
                for k in range(i, n):
                    a[j][k] -= factor * a[i][k]
                b[j] -= factor * b[i]

        x = [0] * n
        for i in range(n - 1, -1, -1):
            sum_ax = 0
            for j in range(i + 1, n):
                sum_ax += a[i][j] * x[j]
            x[i] = (b[i] - sum_ax) / a[i][i]
        return x

    @classmethod
    def calculate_max_profit(cls, a, b, c):
        n = len(a)
        intersect_point = cls.gaussian_elimination(a, b)
        x_is_0 = (0, min([b[i] / a[i][-1] for i in range(n)]))
        y_is_0 = (min([b[i] / a[i][0] for i in range(n)]), 0)
        optimum_points = [intersect_point, x_is_0, y_is_0]
        value2point = {}
        for point in optimum_points:
            value = sum(x * y for x, y in zip(point, c))
            value2point[value] = point
        max_value = max(value2point.keys())
        optimum_point = value2point[max_value]
        return max_value, optimum_point

    def optimum_milk_profit(self):
        unit_material = [[1, 2, 3], [5, 3, 5], [3, 4, 5]]
        materials = [86, 150, 190]
        profit = [3, 4, 5]
        milk_profit, milk_crop = self.calculate_max_profit(unit_material, materials, profit)
        print(f'最大利润为{milk_profit}万元，此时生产甲的数量为{milk_crop[0]}吨，')


if __name__ == '__main__':
    MaxProfit().optimum_milk_profit()
    # print(x)
