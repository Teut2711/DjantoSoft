from Master import models

from abc import ABCMeta

import json
import pickle
import pandas as pd
import os
import pathlib
from more_itertools.more import split_before


PATH = pathlib.Path(__file__).parent


def get_cols(cols_file):
    with open(cols_file, "rb") as p:
        cols = pickle.load(p)
    return cols


class GetAllInfo:
    TOTAL_ROWS_INPUT_FILE = 0
    IN_TABLE_DEMATAD = 0  # models.Dematad.objects.count()
    IN_TABLE_Demathol = 0  # models.Demathol.objects.count()
    inserts_DEMATAD = 0  # models.Dematad.objects.count() - IN_TABLE_DEMATAD
    inserts_Demathol = 0  # models.Demathol.objects.count() - IN_TABLE_Demathol
    updates_DEMATAD = 0
    updates_Demathol = 0


class GetDataFrame:

    @staticmethod
    def read_file_obj(file_obj, cols):
        # from nodeirc by _habnabit
        for chunk in split_before(
            (l.decode().strip() for l in file_obj),
                lambda l: l.startswith('01')):
            if len(chunk) <= 1:
                continue
            yield GetDataFrame.chunk_to_df(chunk, cols)
        # from nodeirc by _habnabit

    @staticmethod
    def chunk_to_df(chunk, cols):

        isin, date = chunk[0].split("##")[1:3]
        chunk = chunk[1:]
        data = [i.split("##")[2:] for i in chunk]

        df = pd.DataFrame(data=data, columns=cols)
        df["ISEN"] = isin
        df["DATE"] = date
        return df


class CleanFuncs:
    @staticmethod
    def dematad_clean(df):
        return df.drop_duplicates(
            subset=["DPID", "CLID"],
            keep='first')

    @staticmethod
    def Demathol_clean(df):
        return df.drop_duplicates(
            subset=["DPID", "CLID"],
            keep='first')


class ProcessDf:

    def processdematad(self, df, cols_dematad, first_time=True):
        if first_time:
            models.Dematad.bulk_create(df[cols_dematad].to_dict(
                orient="records"), ignore_conflicts=True)
        else:
            for i in df[cols_dematad].to_dict(orient="records"):
                created_or_not = models.Dematad.update_or_create(i)[1]
                if not(created_or_not):
                    GetAllInfo.updates_DEMATAD += 1
                else:
                    GetAllInfo.inserts_DEMATAD += 1

    def processDemathol(self, df, cols_Demathol, first_time=True):
        if first_time:
            models.Demathol.bulk_create(df[cols_Demathol].to_dict(
                orient="records"), ignore_conflicts=True)
        else:
            for i in df[cols_Demathol].to_dict(orient="records"):
                created_or_not = models.Demathol.update_or_create(i)[1]
                if not(created_or_not):
                    GetAllInfo.updates_Demathol += 1
                else:
                    GetAllInfo.updates_Demathol += 1


def main(file_obj):

    cols_df = get_cols(os.path.join(PATH, 'cols', 'cols.pk'))
    cols_dematad = get_cols(os.path.join(PATH, 'cols', 'dematad.pk'))
    cols_Demathol = get_cols(os.path.join(PATH, 'cols', 'Demathol.pk'))

    if models.Dematad.objects.exists():
        for df in reversed(GetDataFrame.read_file_obj(file_obj, cols_df)):
            ProcessDf.processdematad(df, cols_dematad, True)
            ProcessDf.processDemathol(df, cols_Demathol, True)

    else:
        for df in GetDataFrame.read_file_obj(file_obj, cols_df):
            ProcessDf.processdematad(df, cols_dematad, False)
            ProcessDf.processDemathol(df, cols_Demathol, False)
    return json.dumps({key: value for key, value in vars(GetAllInfo)
            if not key.startswith('__') and not callable(key)})
