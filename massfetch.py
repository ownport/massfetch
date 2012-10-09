#!/usr/bin/env python
#
#   Mass Fetch
#

# TODO specify JSON format for requests
# TODO handle requests in JSON format
import requests

__version__ = '0.1'

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description='massfetch text content')
    parser.add_argument('-u', '--urls', help='url list')
    parser.add_argument('-r', '--requests', help='request list')
    parser.add_argument('-d', '--db', help='database uri')
    
    args = parser.parse_args()
    
    print args
