#!/bin/bash
cd ../
/home/miro/anaconda2/bin/python modeller_workflow/model_custom.py | tee modeller.log
cd - 
