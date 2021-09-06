import pickle
import os
import glob
from pathlib import Path
import smtplib
from xlutils.copy import copy
import csv
from xlsxwriter.workbook import Workbook
import codecs
import xlwt
import xlrd
import openpyxl
from copy import copy
import re

#This function will take the data with Preferences of the teachers from the google-form and provide it to the analysis.
def getFromGoogleForm():
  print()
  
#This function will classify the data (by removing the undesirable variants) in order to compose the proper schedule for the education.   
def analyze():
  print()
  
#This function will the analized data into the Google Form in the format of schedule with all possible variants.
def putIntoGoogleTable():
  print()
