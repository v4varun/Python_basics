import io
import logging
import sys
from datetime import date,datetime as dt
import pandas as pd
import json
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment
from Modules.config_reader import table_info

class Dataval:

    def __init__(self, env):
        try:
            self.env = env
            self.target_table_name = sys.argv[1]
        except Exception as e:
            print("Error exception")
        
        self.conf_dict = table_info(self.target_table_name)
        

da = Dataval('dev')

#if "Error" not in da.conf_dict.keys():
print(da.conf_dict)
#else:
 #   print("something went wrong")

exit(0)  