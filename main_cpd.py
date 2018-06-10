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

pe = ParameterEstimator(model, df)
print("\n", pe.state_counts('SAO2')) 

mle = MaximumLikelihoodEstimator(model, df)
# print(mle.estimate_cpd('VALV'))  # unconditional
print ("MLE estimater cpd PVS");
print(mle.estimate_cpd('PVS'))  # conditional

'''
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
'''

model.fit(df, MaximumLikelihoodEstimator)
infer = VariableElimination(model)

print ("infer.query(['VALV'])");
print (infer.query(['VALV'])['VALV']);

print ("infer.query(['VALV'],evidence={'VLNG':1,'SAO2':1,'ECO2':0,'VMCH':3,'VTUB':1,'MINV':3,'INT':2}) ['VALV']");
print (infer.query(['VALV'],evidence={'VLNG':1,'SAO2':1,'ECO2':0,'VMCH':3,'VTUB':1,'MINV':3,'INT':2}) ['VALV'])

print (model.estimate_cpd('PVS'));
print (infer.query(['VALV'],evidence={'VLNG':0,'DISC':1}) ['VALV'])
print ("PRSS : VTUB = 0 | ACO2 = 1")
print (infer.query(['PRSS'],evidence={'VTUB':0,'ACO2':1}) ['PRSS'])


print ("PRSS : 'VTUB':0,'VMCH':1");
print (infer.query(['PRSS'],evidence={'VTUB':0,'VMCH':1}) ['PRSS'])

print ("PRSS : 'VTUB':0,'VMCH':0");
print (infer.query(['PRSS'],evidence={'VTUB':0,'VMCH':0}) ['PRSS'])

print ("'DISC':0,'MVS':1")
print (infer.query(['PRSS'],evidence={'DISC':0,'MVS':1}) ['PRSS'])

print ("'DISC':1,'MVS':0")
print (infer.query(['PRSS'],evidence={'DISC':1,'MVS':0}) ['PRSS'])

print ("PRSS : 'VTUB':0,'VLNG':0");
print (infer.query(['PRSS'],evidence={'VTUB':0,'VLNG':0}) ['PRSS'])

print ("PRSS : 'VTUB':0,'VLNG':1");
print (infer.query(['PRSS'],evidence={'VTUB':0,'VLNG':1}) ['PRSS'])

print ("PRSS : 'VTUB':0,'INT':0");
print (infer.query(['PRSS'],evidence={'VTUB':0,'INT':0}) ['PRSS'])

print ("PRSS : 'VTUB':0,'INT':1");
print (infer.query(['PRSS'],evidence={'VTUB':0,'INT':1}) ['PRSS'])

print ("VALV : 'VTUB':0,'PRSS':1");
print (infer.query(['VALV'],evidence={'VTUB':0,'PRSS':1}) ['VALV'])

print ("VALV : 'VTUB':0,'PRSS':0");
print (infer.query(['VALV'],evidence={'VTUB':0,'PRSS':0}) ['VALV'])

print ("VALV : 'VTUB':0,'DISC':0");
print (infer.query(['VALV'],evidence={'VTUB':0,'DISC':0}) ['VALV'])

print ("VALV : 'VTUB':0,'DISC':1");
print (infer.query(['VALV'],evidence={'VTUB':0,'DISC':1}) ['VALV'])








