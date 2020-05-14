from django.db import IntegrityError

from Master import models

import logging
from abc import ABCMeta
import pickle
import pandas as pd
import os
import pathlib
from more_itertools.more import split_before

logging.basicConfig(filename="Master/backend/Master/Logs/loggs.log", level=logging.INFO)

PATH = pathlib.Path(__file__).parent


def get_cols(cols_file):
    with open(cols_file, "rb") as p:
        cols = pickle.load(p)
    return cols


class GetAllInfo:
    TOTAL_ROWS_INPUT_FILE = 0
    WERE_IN_TABLE_DEMATAD = 0
    WERE_IN_TABLE_DEMATHOL = 0
    INSERTS_DEMATAD = 0
    INSERTS_DEMATHOL = 0
    UPDATES_DEMATAD = 0
    UPDATES_DEMATHOL = 0


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


# class CleanFuncs:
#     @staticmethod
#     def Dematad_clean(df):
#         return df.drop_duplicates(
#             subset=["DPID", "CLID"],
#             keep='first')

#     @staticmethod
#     def Demathol_clean(df):
#         return df.drop_duplicates(
#             subset=["DPID", "CLID"],
#             keep='first')


class ProcessDf:
    # ANCHOR The following class takes in a pandas dataframe and creates/updates the tables

    @staticmethod
    def processDematad( df, cols_Dematad, first_time=True):
        if first_time:
            for i in (df[cols_Dematad]).to_dict(orient="records"):
                try:
                    models.Dematad.objects.create(**i)
                except IntegrityError:
                    pass
                else:
                    GetAllInfo.INSERTS_DEMATAD += 1
        else:
            for i in df[cols_Dematad].to_dict(orient="records"):

                try:
                    DPID = i.pop("DPID")
                    CLID = i.pop("CLID")
                    created_or_not = models.Dematad.objects.update_or_create(
                        DPID=DPID, CLID=CLID, defaults=i)[1]
                    print(created_or_not)
                except IntegrityError:
                    pass
                else:
                    if not(created_or_not):
                        GetAllInfo.UPDATES_DEMATAD += 1
                    else:
                        GetAllInfo.UPDATES_DEMATAD += 1
                    print("Dematad", " :  ", GetAllInfo.UPDATES_DEMATAD)

    @staticmethod
    def processDemathol( df, cols_Demathol, first_time=True):

        if first_time:

            for i in (df[cols_Demathol]).to_dict(orient="records"):
                try:
                    models.Demathol.objects.create(**i)
                except IntegrityError:
                    pass
                else:
                    GetAllInfo.INSERTS_DEMATHOL += 1
        else:
            for i in df[cols_Demathol].to_dict(orient="records"):

                try:
                    DPID = i.pop("DPID")
                    CLID = i.pop("CLID")
                    created_or_not = models.Demathol.objects.update_or_create(
                        DPID=DPID, CLID=CLID, defaults=i)[1]
                except IntegrityError:
                    pass
                else:
                    if not(created_or_not):
                        GetAllInfo.UPDATES_DEMATHOL += 1
                    else:
                        GetAllInfo.UPDATES_DEMATHOL += 1
                    print("Demathol", " :  ", GetAllInfo.UPDATES_DEMATHOL)


def main(file_obj):

    GetAllInfo.WERE_IN_TABLE_DEMATAD = models.Dematad.objects.count()
    GetAllInfo.WERE_IN_TABLE_DEMATHOL = models.Dematad.objects.count()

    cols_df = get_cols(os.path.join(PATH, 'cols', 'cols.pk'))
    cols_Dematad = get_cols(os.path.join(PATH, 'cols', 'Dematad.pk'))
    cols_Demathol = get_cols(os.path.join(PATH, 'cols', 'Demathol.pk'))
    
    if models.Dematad.objects.exists():
        dematad = True
    else:      
        dematad = False

    if models.Demathol.objects.exists():
        demathol = True
    else:      
        demathol = False
          
    for df in GetDataFrame.read_file_obj(file_obj, cols_df):


        if not(dematad):
             ProcessDf.processDematad(df, cols_Dematad, first_time=True)
        else:
            ProcessDf.processDematad(df, cols_Dematad, first_time =False)
            
        if not(demathol):
             ProcessDf.processDemathol(df, cols_Demathol, first_time = True)
        else:
            ProcessDf.processDemathol(df, cols_Demathol, first_time = False)

        GetAllInfo.TOTAL_ROWS_INPUT_FILE += df.shape[0]
    print("Returning")
    return {key: value for key, value in vars(GetAllInfo)
            if not key.startswith('__') and not callable(key)}
