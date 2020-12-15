#!/usr/bin/python3

"""
Utilities used by RPi Monitor
"""

import subprocess

# Subprocess input

def vcgencmd(*args):
    """
    Creates VCGENCMD command line string
    """
    return ('vcgencmd', ) + args

def free(*args):
    """
    Creates Free command line string
    """
    return ('free', ) + args

def df_string(*args):
    """
    Creates DF command line string
    """
    return ('df', ) + args

# CPU

def cpu_temp():
    """
    Returns current CPU temp
    """
    temp = subprocess.check_output(vcgencmd("measure_temp"))
    return temp.split('=')[-1].strip().split("'")[0]


def cpu_clock():
    """
    Returns current CPU clock speed
    """
    clock = subprocess.check_output(vcgencmd("measure_clock arm"))
    return clock.split('=')[-1].strip()

# Memory

def parse_free(free_output):
    """
    Cleans free output
    """

    # Removing Headers, and text
    no_headers = [i.split("\\n")[0].strip() for i in free_output.split(':')[1:]]

    categories = ['total', 'used', 'free', 'shared', 'cached', 'available']
    output = {'Memory': '', "Swap": ''}

    # Cleaning Routine
    for number, value in enumerate(no_headers):
        line = value.split(' ')
        cleaned_line = []
        for j in line:
            if j != '':
                try:
                    cleaned_line.append(int(j))
                except ValueError:
                    pass

        if number == 0:
            output['Memory'] = {k:v for k,v in zip(categories, cleaned_line)}
            print(output)
        else:
            output['Swap'] = {k:v for k,v in zip(categories, cleaned_line)}

    return output

def mem_usage():
    """
    Returns current memory usage
    """
    mem_info = str(subprocess.check_output(free()))
    return parse_free(mem_info)

# Storage

def parse_df(df_output):
    """
    Cleans DF output
    """
    no_headers = df_output.split('\\n')[1:-1]

    output = {}
    categories = ['size', 'used', 'available', 'percentage', 'mount_point']

    # Cleaned Lines
    lines = [list(filter(None, i.split(" "))) for i in no_headers]

    for line in lines:
        output[line[0]] = {k:v for k,v in zip(categories, line[1:]) }

    return output


def storage():
    """
    Returns current storage information
    """
    try:
        storage_info = str(subprocess.check_output(df_string('-h')))
        output = parse_df(storage_info)
    except Exception as ex:
        print(ex)
        return {}

    return output
