#!/bin/python3
import requests
import argparse
import os

# print banner

banner = '''
'''
# get arguments 

argumentInit = argparse.ArgumentParser(description="Directory Brute Force on web application")
argumentInit.add_argument("-w","--wordlist",type=str,help="wordlist : example ->  /usr/share/wordlist/...")
argumentInit.add_argument("-u","--url",help="example: http://example.com")

get_arguments = argumentInit.parse_args() 
try:
    wordlist = open(get_arguments.wordlist,encoding='UTF-8',errors='ignore')

# brute force

    for i in wordlist:
        r = requests.get(f"{get_arguments.url}/{i.strip()}",headers={
            "User-Agent":"Mozilla FireFox"
            },allow_redirects=True).status_code
        if r == 200:
            print(f"\033[1;33m[ + ] found : {get_arguments.url} -> {i.strip()}")
        else:
            print( "\033[1;31m" + " Not found : " + get_arguments.url+ "->" +i.strip())
except:
    os.system("python3 fdirbrute.py -h")
    

