#!/usr/bin/env python
#
#   Mass Fetch
#

__author__ = 'Andrey Usov <https://github.com/ownport/massfetch>'
__version__ = '0.1'
__license__ = """
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE."""

import os
import sys
import time
import random
import kvlite
import hashlib
import requests

class MassFetch(object):
    ''' Mass fetch '''    

    # Default HTTP headers
    base_headers = {
        'Accept-Encoding': 'gzip, deflate, compress', 
        'Accept': '*/*', 
        'User-Agent': 'massfetch/?'.format(__version__)
    }
    # Maximum number of redirects allowed within a request
    max_redirects = 10
    # Reuse HTTP Connections
    keep_alive = True
    # The number of times a request should be retried in the event of a connection failure
    max_retries = 0
    # The maximium size of an HTTP connection pool
    pool_maxsize = 10
    # The number of active HTTP connection pools to use
    pool_connections = 10
    # If encode_uri is true, URIs will automatically be percent-encoded
    encode_uri = True
    # If trust_env is true, the surrouding environment will be trusted (environ, netrc)
    trust_env = True
    # If store_cookies is false, the received cookies as part of the HTTP response would be ignored.  
    store_cookies = True
    
    # start_urls
    start_urls = list()
    
    # containter (database where responses will be stored)
    container = None
    
    # fetch delay (in seconds)
    fetch_delay = 5
    
    # random fetch delay
    random_fetch_delay = True

    def __init__(self):
        ''' init 
        '''
        if self.container:
            self._container = kvlite.open(self.container)        
        else:
            raise RuntimeError('Undefined container: %s', self.container)
        
        self.urls_queue = list()
        self._processed_urls = list()
        
        requests.defaults.defaults['pool_connections'] = self.pool_connections
        requests.defaults.defaults['keep_alive'] = self.keep_alive
        requests.defaults.defaults['max_retries'] = self.max_retries
        requests.defaults.defaults['store_cookies'] = self.store_cookies
        requests.defaults.defaults['trust_env'] = self.trust_env
        requests.defaults.defaults['base_headers'] = self.base_headers
        requests.defaults.defaults['pool_maxsize'] = self.pool_maxsize
        requests.defaults.defaults['encode_uri'] = self.encode_uri
        requests.defaults.defaults['max_redirects'] = self.max_redirects

    def parse(self, data):
        ''' this method can be overridden '''
        pass
                            
    def run(self):
        ''' run massfetch 
        '''
        #self.init()
        
        self.urls_queue.extend(self.start_urls)
        
        for url in self.urls_queue:
        
            if url in self._processed_urls:
                continue
        
            response = requests.get(url)
            if response.status_code <> 200:
                print 'url: %s, status: %d' % (url, response.status)
                continue
            else:                
                print url
                data = {'headers': response.headers, 'content': response.content}
                data['headers']['source_url'] = url
                data['headers']['status_code'] = response.status_code
                self._container.put(hashlib.sha1(url).hexdigest(), data)
                self._container.commit()
                
                self.parse(data)
                
                self._processed_urls.append(url)
            
            if self.fetch_delay:
                if self.random_fetch_delay:
                    delay = int(random.uniform(0.5, 1.5) * self.fetch_delay)
                else:
                    delay = self.fetch_delay
                time.sleep(delay)
                


