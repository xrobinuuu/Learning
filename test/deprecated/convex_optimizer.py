IntFloat = int | float


class BaseModel:

    def __init__(self, **data):
        for attr, data_type in type(self).__annotations__.items():
            if attr in data:
                if isinstance(data[attr], data_type):
                    self.__setattr__(attr, data[attr])
                else:
                    raise TypeError(f"'{attr}' type doesn't match '{data_type.__name__}'")
            elif hasattr(type(self), attr):
                self.__setattr__(attr, getattr(type(self), attr))
            else:
                raise ValueError(f"Field required: {attr}")

    def model_dump(self) -> dict:
        data = dict()
        for attr in self.__dict__:
            value = self.__getattribute__(attr)
            if isinstance(value, list | set | tuple):
                sub_value = type(value)(v.model_dump() if hasattr(v, "model_dump") else v for v in value)
            elif hasattr(value, "model_dump"):
                sub_value = value.model_dump()
            else:
                sub_value = value
            data.update({attr: sub_value})
        return data

    def __str__(self) -> str:
        return str(self.model_dump())


class Element(BaseModel):
    name: str
    num: IntFloat

    def __init__(self, **data):
        super().__init__(**data)
        if self.num <= 0:
            raise ValueError(f"The expected 'num' is greater than 0, but got {self.num}.")


class Elements:

    def __init__(self, elements: list[dict[str, str | IntFloat]]):
        self.elements = [Element(**element) for element in elements]
        self.elements_name = list(set(element.name for element in self.elements))
        if len(self.elements_name) != len(self.elements):
            raise ValueError("Elements within the variable cannot be duplicated.")

    def __getitem__(self, name: str) -> IntFloat:
        for element in self.elements:
            if element.name == name:
                return element.num


class Variate(Elements):

    def __init__(self, name: str, elements: list[dict[str, str | IntFloat]], coefficient: IntFloat):
        self.name = name
        self.coefficient = coefficient
        super().__init__(elements)


class LinearEquationAnswer(BaseModel):
    x: IntFloat
    y: IntFloat


class LinearEquation22(BaseModel):
    a11: IntFloat
    a12: IntFloat
    b1: IntFloat
    a21: IntFloat
    a22: IntFloat
    b2: IntFloat

    def gaussian_elimination(self) -> LinearEquationAnswer:
        r1 = self.a21 / self.a11
        r2 = self.a22 / self.a12
        if r1 != r2:
            y = (r1 * self.b1 - self.b2) / (r1 * self.a12 - self.a22)
            x = (self.b1 - self.a12 * y) / self.a11
            return LinearEquationAnswer(x=x, y=y)
        raise ValueError(
            f"Can't solve linear equation:\n{self.a11}x + {self.a12}y = {self.b1}\n{self.a21}x + {self.a22}y = {self.b2}"
        )


class TargetAnswer(BaseModel):
    variates: LinearEquationAnswer
    value: IntFloat

    def _comparison(self, other: "TargetAnswer", operator: str) -> bool:
        if not isinstance(other, TargetAnswer):
            return NotImplemented
        return getattr(self.value, operator)(other.value)

    def __lt__(self, other: "TargetAnswer") -> bool:
        return self._comparison(other, "__lt__")

    def __le__(self, other: "TargetAnswer") -> bool:
        return self._comparison(other, "__le__")

    def __eq__(self, other: "TargetAnswer") -> bool:
        return self._comparison(other, "__eq__")


class Target(BaseModel):
    x_coefficient: IntFloat
    y_coefficient: IntFloat

    def __call__(self, variates: LinearEquationAnswer) -> TargetAnswer:
        return TargetAnswer(variates=variates, value=self.x_coefficient * variates.x + self.y_coefficient * variates.y)


class TargetAnswers(BaseModel):
    answers: list[TargetAnswer] = []

    def append(self, target_answer: TargetAnswer) -> None:
        self.answers.append(target_answer)

    def extend(self, target_answers: "TargetAnswers") -> None:
        self.answers.extend(target_answers.answers)

    def __iter__(self):
        if self.answers:
            return iter(self.answers)
        raise ValueError("answers is empty!")


class ConvexOptimizer(Elements):

    def __init__(self, variates: list[dict], elements: list[dict[str, str | IntFloat]]):
        variates = [Variate(**variate) for variate in variates]
        if len(variates) != 2:
            raise ValueError("The number of variables can only be two.")
        self.x: Variate = variates[0]
        self.y: Variate = variates[1]
        super().__init__(elements)
        if self.x.elements_name != self.elements_name or self.y.elements_name != self.elements_name:
            raise ValueError("Elements name are inconsistent.")
        self.target = Target(x_coefficient=self.x.coefficient, y_coefficient=self.y.coefficient)

    def is_constrained(self, x: IntFloat, y: IntFloat) -> bool:
        return all(self.x[element] * x + self.y[element] * y <= self[element] for element in self.elements_name)

    def init_target_answers(self) -> TargetAnswers:
        target_answers = TargetAnswers()
        for element in self.elements_name:
            le_answer_x0 = LinearEquationAnswer(x=0, y=self[element] / self.y[element])
            if self.is_constrained(x=le_answer_x0.x, y=le_answer_x0.y):
                target_answers.append(self.target(le_answer_x0))
            le_answer_y0 = LinearEquationAnswer(x=self[element] / self.x[element], y=0)
            if self.is_constrained(x=le_answer_y0.x, y=le_answer_y0.y):
                target_answers.append(self.target(le_answer_y0))
        return target_answers

    def run(self, include_zero: bool = True) -> TargetAnswers:
        target_answers = TargetAnswers()
        if include_zero:
            target_answers.extend(self.init_target_answers())
        i = 0
        while i < len(self.elements_name) - 1:
            element_1 = self.elements_name[i]
            for j in range(i + 1, len(self.elements_name)):
                element_2 = self.elements_name[j]
                a11, a12, b1 = self.x[element_1], self.y[element_1], self[element_1]
                a21, a22, b2 = self.x[element_2], self.y[element_2], self[element_2]
                le_answer = LinearEquation22(a11=a11, a12=a12, b1=b1, a21=a21, a22=a22, b2=b2).gaussian_elimination()
                if self.is_constrained(x=le_answer.x, y=le_answer.y):
                    target_answers.append(self.target(le_answer))
            i += 1
        return target_answers

    def format(self, include_zero: bool = True) -> str:
        target_answer = max(self.run(include_zero=include_zero))
        print(target_answer)
        return f"当{self.x.name}的数量为{target_answer.variates.x:.2f}，{self.y.name}的数量为{target_answer.variates.y:.2f}时，达到最大值{target_answer.value:.2f}。"


if __name__ == '__main__':
    d = {
        "variates": [
            {
                "name": "甲",
                "elements": [
                    {
                        "name": "纯牛奶",
                        "num": 1
                    },
                    {
                        "name": "酸牛奶",
                        "num": 5
                    },
                    {
                        "name": "牛奶",
                        "num": 2
                    }
                ],
                "coefficient": 3
            },
            {
                "name": "乙",
                "elements": [
                    {
                        "name": "纯牛奶",
                        "num": 2
                    },
                    {
                        "name": "酸牛奶",
                        "num": 3
                    },
                    {
                        "name": "牛奶",
                        "num": 5
                    }
                ],
                "coefficient": 4
            }
        ],
        "elements": [
            {
                "name": "纯牛奶",
                "num": 86
            },
            {
                "name": "酸牛奶",
                "num": 150
            },
            {
                "name": "牛奶",
                "num": 70
            }
        ]
    }

    print(ConvexOptimizer(**d).format())
