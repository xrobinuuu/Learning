import random
import time
from itertools import chain
from typing import List

import numpy as np
import pandas as pd
from pydantic import BaseModel


def reshape(data: List[str], dim1_size: int = 500) -> List[List[str]]:
    data.sort()
    div, mod = divmod(len(data), dim1_size)
    normal_num = div * dim1_size
    new_data = np.array(data[:normal_num]).reshape(-1, dim1_size).tolist()
    if mod != 0:
        new_data.append(data[normal_num:])
    return new_data


class RowsFilter(BaseModel):
    rows: List[str] = []

    def load_partition(self, rows_in_partition: int = 200) -> pd.DataFrame:
        kwargs_df = pd.DataFrame({"rows": reshape(self.rows, rows_in_partition)})
        info_series = self._new_load_runway_info_by_rows(kwargs_df)
        info_series = self._load_runway_info_by_rows(kwargs_df)
        return pd.DataFrame({"kwargs": kwargs_df.to_dict(orient="records"), "info": info_series})

    @staticmethod
    def _load_runway_info_by_rows(kwargs_df: pd.DataFrame) -> pd.Series:
        info_df = pd.DataFrame({
            "uuid": map(str, range(600000)),
            "DepRunway": [str(random.randint(10, 20)) for _ in range(600000)],
            "ArrRunway": [str(random.randint(30, 40)) for _ in range(600000)]
        })
        t_1 = time.perf_counter()
        runway_df = pd.DataFrame({"key": chain.from_iterable(kwargs_df["rows"].values)})
        runway_df.loc[:, "uuid"] = runway_df["key"].apply(lambda row_key: row_key.split("-")[-1])
        runway_df = pd.merge(runway_df, info_df, on="uuid", how="left")
        info = kwargs_df["rows"].apply(
            lambda rows: runway_df.loc[np.isin(runway_df["key"], rows), ["key", "DepRunway", "ArrRunway"]].to_dict(
                orient="records"))
        t_2 = time.perf_counter()
        print(f"耗时: {t_2 - t_1}")
        return info

    @staticmethod
    def _new_load_runway_info_by_rows(kwargs_df: pd.DataFrame) -> pd.Series:
        info_df = pd.DataFrame({
            "uuid": map(str, range(600000)),
            "DepRunway": [str(random.randint(10, 20)) for _ in range(600000)],
            "ArrRunway": [str(random.randint(30, 40)) for _ in range(600000)]
        })
        t_1 = time.perf_counter()
        runway_df = kwargs_df.reset_index().explode('rows').rename(columns={"rows": "key", })
        runway_df.loc[:, "uuid"] = runway_df["key"].apply(lambda row_key: row_key.split("-")[-1])
        runway_df = pd.merge(runway_df, info_df, on="uuid", how="left")
        info = runway_df.groupby(by='index').apply(
            lambda rows: rows[['key', 'DepRunway', 'ArrRunway']].to_dict(orient="records"),
            include_groups=False,
        ).reset_index(drop=True)
        t_2 = time.perf_counter()
        print(f"耗时: {t_2 - t_1}")
        return info

    @staticmethod
    def _load_runway_info_by_date(kwargs_df: pd.DataFrame) -> pd.Series:
        if kwargs_df.empty:
            return pd.Series()
        runway_df = pd.DataFrame([], columns=["fl_date", "uuid", "DepRunway", "ArrRunway"])
        runway_df.loc[:, ["key"]] = runway_df[["fl_date", "uuid"]].apply(
            lambda s: f"{s['fl_date'].strftime('%Y%m%d-')}{s['uuid']}", axis=1)
        runway_gb = runway_df.groupby("fl_date")
        info = kwargs_df.apply(lambda s: pd.concat(
            pd.date_range(s["row_start"], s["row_stop"], freq="1D", inclusive="left").map(
                lambda d: runway_df.loc[runway_gb.indices.get(d, []), ["key", "DepRunway", "ArrRunway"]])).to_dict(
            orient="records"), axis=1)
        return info


if __name__ == '__main__':
    n = 600000
    rs = list(map(lambda i: f"{i}-{i}", range(n)))

    rf = RowsFilter(rows=rs)
    res = rf.load_partition()
    print(res)
