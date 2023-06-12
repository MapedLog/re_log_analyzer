import csv
import json
import time
import os
import sys, argparse
import datetime
from file.read_file import readPath,outputPath
from analysis.analysis import analysis

def main():
    args = argparse.ArgumentParser(description="Returns a custom analysis from log files in JSON format",
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args.add_argument("inputfile", help="Path to one or more input files")
    args.add_argument("outputfile", help="Path to a file to save output in plain text JSON format")
    args.add_argument("--mfip", help="most frequent IP")
    args.add_argument("--lfip", help="least frequent IP")
    args.add_argument("--eps", help="events per second")
    args.add_argument("--bytes", help="total amount of bytes exchanged")
    args.add_argument("--fields", default="date,float;header_bytes,int;client_IP,string;http_code,string;response_bytes,int;http_req,string;url,string;user,string;accessType_destIP,string;resp_type,string", help="provide the fields and its type in order to serve proper analytics, which are separated by \";\" and \",\" respectively ")
    args.add_argument("--outputformat", default="json", help="data format for the outputfile. Options: \"json\",\"csv\"")
    arguments = args.parse_args()
    config = vars(arguments)
    print(str(config))
    
    

    #2
    #read_data_from_file & parsing
    #check if multiple files or if file is zip with multiple files inside or with multiple folders inside
    #parse_data_function_csv -> maybe in need of mini-parsing for specific fields ( timestamp,IP,numbers...)
    input_file = readPath(config['inputfile'], str(config['fields']))
    
    ##EXTRA


    #3
    #Statistic functions from options in script

    #3.1 Most Frequent IP
    #3.2 least Frequent IP
    #3.3 Events Per Second
    #3.4 Total amount of bytes exchanged
    analyzed_file = analysis(input_file, config)
    #5
    #export results from options into JSON
    #if none parameters are requested save CSV data in JSON format
    outputPath(config['outputfile'], config['outputformat'], analyzed_file)


if __name__ == "__main__":
   main()