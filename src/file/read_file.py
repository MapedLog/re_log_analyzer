import os
import pandas as pd
import json
import csv

def readPath(path: str, fields, inputFormat): 
    return readFile(path, fields, inputFormat)

def checkPath(path: str):
    if os.path.isdir(path):
        return "multiple"
    elif os.path.isfile(path):
        return "single"

def readFile(path: str, fields: str, inputFormat: str):
    if fields  == "None":
        fields = "date,float;header_bytes,int;client_IP,string;http_code,string;response_bytes,int;http_req,string;url,string;user,string;accessType_destIP,string;resp_type,string"
    fields_dict = dict(map(str.strip, sub.split(',', 1))
           for sub in fields.split(';') if ',' in sub)
    data_frame = pd.DataFrame()
    if checkPath(path) == "multiple":
        files = os.listdir(path)
        print("Showing all the files to be analyzed in this path\n")
        print(str(files)+"\n")
        answer = input("Are you sure you want to continue analyzing all these files [y/n]")
        if answer.lower() in ["y"]:
            files_paths  = [os.path.join(path,i) for i in files]
            for i in files_paths:
                df = inputformat(i, inputFormat)
                data_frame = data_frame._append(df, ignore_index=True)
        elif answer.lower() in ["n"]:
            print("Cancelling analysis")
            return
        else:
            print("Cancelling analysis")
            return        
    else:
        data_frame = inputformat(path, inputFormat)
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

def inputformat(file: str, inputFormat: str):
    df = pd.DataFrame()
    if inputFormat == "json":
        df = pd.read_json(file, orient="index")
    elif "csv" in inputFormat:
        parser = inputFormat.split(',')
        if parser[1] == "whitespace":
            df = pd.read_csv(file, delim_whitespace=True, header=None)
        elif parser[1] == "comma":
            df = pd.read_csv(file, sep="\,", header=None)
        elif parser[1] == "tab":
            df = pd.read_csv(file, sep="\t", header=None)
        elif parser[1] == "quote":
            df = pd.read_csv(file, sep="\"", header=None)
        else:
            print("Must specify an accepted format. Use --help parameter to know how to specify it")
    else:
        print("Must specify an accepted format. Use --help parameter to know how to specify it")
        return
    return df
