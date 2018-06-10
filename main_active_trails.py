# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:41:24 2017

@author: aviza
"""

import openpyxl
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.linalg import inv
import pgmpy
from pgmpy.models import BayesianModel
#from pgmpy.factors import TabularCPD
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination

#alarmdata=openpyxl.load_workbook('C:\\Users\\gaura\\Anaconda3\\alarm10K.xlsx')
#aladata=alarmdata.get_sheet_by_name('alarm10K')

df = pd.read_csv("C:\\Users\\aviza\\Desktop\\CSE 674\\Project 1\\alarm10K - Copy.csv");
print(df.head(10))

model=BayesianModel([('HIST', 'PCWP'),
('CVP', 'PCWP'),('CVP', 'LVV'),
('PCWP', 'LVV'),('PCWP', 'HYP'),
('HYP', 'LVV'),
('LVV', 'LVF'),
('LVF', 'STKV'),
('STKV', 'CO'),
('ERLO', 'HRBP'),
('HRBP', 'HREK'),('HRBP', 'HR'),
('HREK', 'ERCA'),('HREK', 'HRSA'),('HREK', 'CCHL'),('HREK', 'HR'),
('ERCA', 'HRSA'),
('HRSA', 'CCHL'),('HRSA', 'HR'),('HRSA', 'CO'),
('TPR', 'BP'),
('ECO2', 'VLNG'),('ECO2', 'VALV'),
('MINV', 'PVS'),('MINV', 'SAO2'),('MINV', 'VTUB'),('MINV', 'INT'),('MINV', 'MVS'),('MINV', 'VLNG'),('MINV', 'VALV'),('MINV', 'ACO2'),
('PVS', 'SAO2'),('PVS', 'VMCH'),('PVS', 'VTUB'),('PVS', 'ACO2'),
('SAO2', 'VMCH'),('SAO2', 'VLNG'),('SAO2', 'VALV'),('SAO2', 'ACO2'),
('SHNT', 'INT'),
('INT', 'VALV'),
('PRSS', 'VTUB'),
('DISC', 'VTUB'),
('MVS', 'VMCH'),
('VMCH', 'VTUB'),('VMCH', 'VALV'),
('VTUB', 'VLNG'),('VTUB', 'VALV'),
('VLNG', 'VALV'),('VLNG', 'ACO2'),
('VALV', 'ACO2'),
('CCHL', 'HR'),
('HR', 'CO'),
('CO', 'BP')])


# mle = MaximumLikelihoodEstimator(model, df)
# print(mle.estimate_cpd('VALV'))  # unconditional
# print(mle.estimate_cpd('PVS'))  # conditional

print (model.active_trail_nodes("MINV"))
print (model.active_trail_nodes("PVS"))
print (model.active_trail_nodes("SAO2"))
print (model.active_trail_nodes("MVS"))
print (model.active_trail_nodes("VMCH"))
print (model.active_trail_nodes("PRSS"))
print (model.active_trail_nodes("DISC"))
print (model.active_trail_nodes("VTUB"))
print (model.active_trail_nodes("ECO2"))
print (model.active_trail_nodes("VLNG"))
print (model.active_trail_nodes("VALV"))
print (model.active_trail_nodes("ACO2"))
print (model.active_trail_nodes("INT"))
print (model.active_trail_nodes("SHNT"))