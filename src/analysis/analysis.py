import json

def analysis(data, parameters):
    to_analyze = []
    analyzed = {}
    for i in parameters.keys():
        if i not in ('inputfile', 'outputfile', 'fields', 'outputformat'):
            if parameters[i] != False:
                to_analyze.append(i)
    if "mfip" in to_analyze:
        analyzed.update(top_ip(data,str(parameters['mfip'])))
    if "lfip" in to_analyze:
        analyzed.update(least_ip(data,str(parameters['lfip'])))
    if "eps" in to_analyze:
        analyzed.update(eps(data, str(parameters['eps'])))
    if "bytes" in to_analyze:
        analyzed.update(bytes(data, str(parameters['bytes'])))
    return analyzed

def top_ip(data, fields):
    fields = fields.split(',')
    result_top_ip = {}
    for i in fields:
        data[i] = data[i].str.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})').str[0]
        result_top_ip['top_'+i] = data[i].value_counts().idxmax()
    return result_top_ip

def least_ip(data, fields):
    fields = fields.split(',')
    result_least_ip = {}
    for i in fields:
        data[i] = data[i].str.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})').str[0]
        result_least_ip['least_'+i] = data[i].value_counts().idxmin()
    return result_least_ip

def eps(data, fields):
    fields = fields.split(',')
    result_eps = {}
    for i in fields:
        result_eps['eps_'+i] = len(data)/(max(data[i]) - min(data[i]))
    return result_eps

def bytes(data, fields):
    fields = fields.split(',')
    result_bytes = {}
    for i in fields:
        result_bytes['total_'+i] = int(data[i].sum())
    if len(fields) != 1:
        result_bytes['total_bytes'] = int(sum(result_bytes.values()))
    return result_bytes