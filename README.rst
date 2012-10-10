=========
massfetch
=========

simple script for downloading text content from the list and storing to database for later processing. 

Based on:
- `Requests <https://github.com/kennethreitz/requests>` is an ISC Licensed HTTP library, written in Python
- `kvlite <https://github.com/ownport/kvlite` is key-value database wrapper for SQL database (MySQL, SQLite)

massfetch supports the next HTTP methods: HEAD and GET. 

Requests interface
==================

To fetch HTTP content via massfetch you can use the list of URLs, or create container (kvlite database) with detail request parameters.

The list of URLs:

    http://localhost:8080/page0001
    http://localhost:8080/page0002
    http://localhost:8080/page0003
    http://localhost:8080/page0004
    ...
    http://localhost:8080/page1000

In case of use URL list all requests will be done via GET method.

If you need to make more specific request to web resource, better to create container.

Container
=========

The container is kvlite database with limited amount of records. Each record has parameters to specify request more detail.

The parameters for request

Parameters:	

- method,  HTTP method 
- url, URL for the request.
- params,  (optional) Dictionary or bytes to be sent in the query string.
- data, (optional) Dictionary or bytes to send in the body of the request.
- headers, (optional) Dictionary of HTTP Headers to send with the request.
- cookies, (optional) Dict to send with the Request.
- auth, (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
- timeout, (optional) Float describing the timeout of the request.
- allow_redirects, (optional) Boolean. Set to True by default.
- proxies, (optional) Dictionary mapping protocol to the URL of the proxy.
- config, (optional) A configuration dictionary. See request defaults for allowed keys and their default values.

Requests defaults
=================

Configurations:

- base_headers, Default HTTP headers. Default: {'Accept-Encoding': 'gzip, deflate, compress', 'Accept': '*/*', 'User-Agent': 'massfetch/x.x.x'}
- max_redirects, Maximum number of redirects allowed within a request. Default: 30
- keep_alive, Reuse HTTP Connections/ Default: True
- max_retries, The number of times a request should be retried in the event of a connection failure. Default: 0
- pool_maxsize, The maximium size of an HTTP connection pool. Default: 10
- pool_connections: The number of active HTTP connection pools to use. Default: 10
- encode_uri, If true, URIs will automatically be percent-encoded. Default: True
- trust_env, If true, the surrouding environment will be trusted (environ, netrc). Default: True
- store_cookies, If false, the received cookies as part of the HTTP response would be ignored. Default: True






