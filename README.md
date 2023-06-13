# RE_LOG_ANALYZER

## INTRODUCTION

Project that collects the data from file/s and  

## GETTING STARTED

### Prerequisites

In order to execute this project you must install the following software in your computer
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org//) Python3.11 or higher.

### Python libraries

- pandas

### Previous steps

After installing Docker and Python, you must configure the environment and download this repository

`PATH=$PATH:~/.local/bin`

## EXECUTION

For the following executions, please take into account that you should be at the project's path

`cd re_log_analyzer`

### Python

To execute through python cli

`python3 main.py <inputfile> <outputfile> ...`

### CLI

To convert the python script into a CLI tool, execute the following steps.

`python3 -m build`

This generates `dist` directory inside the project

`pip3 install dist/re_log_analyzer.*.tar.gz`

After it, the command can be run on the terminal

`re_log_analyzer`


### Docker

First, build the docker image from the Dockerfile

`docker build -t re_log_analyzer . `

Remember, before running that volume is stated on `/data` path inside the container. Remember also to write `inputfile` and `outputfile`
`docker run -it  -v /data:</path/for_your_files> re_log_analyzer:latest <inputfile> <outputfile> ...`

##  PARAMETERS

Requirements
- Python >= 3.11
- A functioning and standalone cli is the minimum requirement, however you can enhance your
project according to DevSecOps best practices. The more mature your solution is the better.
- The tool should be as fault tolerant as possible and also should be built with future extensibility
in mind. Consider different input or output formats.
- Please also create a Dockerfile in your solution with the application as its entry point and include
instructions on how to run it as a container/service
Program arguments
- Arguments:
`inputfile : Path to one or more input files

outputfile : Path to a file to save output in plain text JSON format`
- Options:
`--mfip : most frequent IP. Must specify field names. If more than one, split them by commas. "field1,field2"
--lfip : least frequent IP. If more than one, split them by commas. "field1,field2"
--eps : events per second. If more than one, split them by commas. "field1,field2"
--bytes : total amount of bytes exchanged. If more than one, split them by commas. "field1,field2"
--fields :  provide the fields and its type in order to serve proper analytics, which are separated by ";" and "," respectively
 Default: "date,float;header_bytes,int;client_IP,string;http_code,string;response_bytes,int;http_req,string;url,string;user,string;accessType_destIP,string;resp_type,string"
--outputformat, data format for the outputfile. Options: "json","csv"
--inputformat , data format for the inputfile. Options: "json","csv". CSV format is customizable. It can be chosen between quote, whitespace, comma, or tab -delimited
Default:" csv,whitespace"`

## SAMPLE DATA

https://www.secrepo.com/squid/access.log.gz

## ROADMAP

- [] Usage of pandas to output statistics and correlation on graphics
- [] Accept more file types than CSV or JSON, giving the option for a custom parser
- [] Generate more statistics options to give more insight to analyst
- [] Analyze more than a single type of format at the same time. This is to 
