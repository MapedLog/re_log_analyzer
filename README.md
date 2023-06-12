# re_log_analyzer

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
o input: Path to one or more input files.
o output: Path to a file to save output in plain text JSON format.
- Options:
o --mfip: most frequent IP
o --lfip: least frequent IP
o --eps: events per second
o --bytes: total amount of bytes exchanged
Sample data
As sample input file, please use the Squid Proxy access logs from the following URL1
:
https://www.secrepo.com/squid/access.log.gz