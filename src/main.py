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
    args.add_argument("--inputformat", default="csv,whitespace", help="data format for the inputfile. Options: \"json\",\"csv\". CSV format is customizable. It can be chosen between quote, whitespace, comma, or tab -delimited")
    arguments = args.parse_args()
    config = vars(arguments)
    
    
    input_file = readPath(config['inputfile'], str(config['fields']), config['inputformat'])
    analyzed_file = analysis(input_file, config)
    outputPath(config['outputfile'], config['outputformat'], analyzed_file)


if __name__ == "__main__":
   main()