# -*- coding: utf-8 -*-
# @Author: Tcarry
import pandas as pd
import numpy as np

def DataFrame(*args,name=None):
    if len(name) == len(args):

        def write_name(title):
            for tit in title:
                yield tit

        def write_data(info):
            for item in info:
                yield item

        leng_box = {len(i) for i in args}
        if len(leng_box) !=1:
            for i in args :
                while len(i) != max(leng_box):
                    i.append(np.nan)
        obj1 = write_name(name)
        obj2 = write_data(args)
        embed = {next(obj1):next(obj2)}
        try:
            value = next(obj1)
            while value:
                embed[value]=next(obj2)
                try:
                    value  = next(obj1)
                except StopIteration:
                    break

            table=pd.DataFrame(embed)
            return table
        except StopIteration:
            table=pd.DataFrame(embed)
            return table
    else:
        raise ValueError(" Check the length of name and data")

def read_csv(file_path,encoding='utf-8'):
    df = pd.read_csv(file_path,encoding=encoding)
    return df

def read_excel(file_path,encoding='utf-8',sheet_name=0):
    df = pd.read_excel(io = file_path,encoding=encoding,sheet_name=sheet_name)
    return df

def tolist(*args):
    q = [[j for j in i if not(pd.isnull(j))] for i in args]
    return q

def add_sheet(file_name,*DF,sheet_name=None):

    writer = pd.ExcelWriter(file_name)
    # sheet_name= ['0','1']
    for df in range(len(DF)):
        DF[df].to_excel(excel_writer=writer,sheet_name=sheet_name[df])
    writer.save()
    writer.close()
