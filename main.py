# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib as plt

def convert_string_to_numeric_data():
    df = pd.read_csv("C:\\Users\\aviza\\Desktop\\CSE 674\\Project 1\\alarm10K.csv"); #Reading the dataset in a dataframe using Pandas
    print ("File reading is done");
    #print df.head(10);
    
    print "",df.TPR.unique();
    print df.dtypes
    
    cat_columns  = df.columns
    print cat_columns
    
    print "Coverting object type column into category "
    for col in cat_columns:
        df[col] = df[col].astype('category')
    
    print df.dtypes
    #print df.head(10)
    for col in cat_columns:
        print col ,"=", df[col].cat.categories
        df[col] = df[col].cat.codes
    
    print df.dtypes
    print df.head(10);
    
    print df.TPR.describe();
    return df;

def main():
    df = convert_string_to_numeric_data();
    print df.dtypes;
    # df.TPR.hist()
    pd.options.display.mpl_style = 'default'
    # df.boxplot()
    # df.hist()
    # df.groupby('TPR').hist()
if __name__ == "__main__":
    main()