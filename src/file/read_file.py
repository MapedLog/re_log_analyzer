import os
import pandas as pd
import json
import csv

def readPath(path: str, fields): 
    return readFile(path, fields)

def checkPath(path: str):
    if os.path.isdir(path):
        #check all files in path
        return "multiple"
    elif os.path.isfile(path):
        print(str(path))
        return "single"

def readFile(path: str, fields: str):
    print(str(fields))
    if fields  == "None":
        fields = "date,float;header_bytes,int;client_IP,string;http_code,string;response_bytes,int;http_req,string;url,string;user,string;accessType_destIP,string;resp_type,string"
    print(str(fields))
    fields_dict = dict(map(str.strip, sub.split(',', 1))
           for sub in fields.split(';') if ',' in sub)
    data_frame = pd.DataFrame()
    if checkPath(path) == "multiple":
        files = os.listdir(path)
        #ASK IF ALL THESE FILES ARE TO BE ANALYZED. IF NOT MOVE THE FILES THAT YOU WANT TO ANALYZE TO ANOTHER DIRECTORY
        files_paths  = [os.path.join(path,i) for i in files]
        for i in files_paths:
            df = pd.read_csv(i, delim_whitespace=True, header=None)
            data_frame = data_frame._append(df, ignore_index=True)
    else:
        #put single file into dataset
        data_frame = pd.read_csv(path, delim_whitespace=True, header=None)
    column_names = list(fields_dict.keys())
    data_frame.columns = column_names
    for  i in column_names:
        if fields_dict[i] not in ("string", "int", "float", "bool"):
            fields_dict[i] = "string" 
        data_frame[i] = data_frame[i].astype(fields_dict[i], errors='ignore')
    return data_frame

def outputPath(file: str, format: str, data_output):
    if os.path.isfile(file):
        print("File already exists. Please introduce a new output file or delete the existing one")
        return
    if format == "json":
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data_output, f, ensure_ascii=False, indent=4)
    elif format == "csv":
        data_aux = pd.DataFrame.from_dict(data_output, orient='index')
        data_aux.iloc[0:].to_csv(file)
    else:
        print("Must specify an accepted format. Use --help parameter to know how to specify it")
        return
    print(str("Process Completed. File saved in destination"))
