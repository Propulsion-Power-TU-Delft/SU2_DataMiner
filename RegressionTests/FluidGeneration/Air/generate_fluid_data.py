#!/usr/bin/env python3

import os 
import sys
from Data_Generation.DataGenerator_NICFD import DataGenerator_CoolProp 
from Common.DataDrivenConfig import EntropicAIConfig 

Config = EntropicAIConfig(sys.argv[-1])

D = DataGenerator_CoolProp(Config_in=Config)
D.SetOutputDir(os.getcwd())

D.PreprocessData()

D.ComputeData()
D.VisualizeFluidData()
D.SaveData()