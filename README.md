# massfetch

simple script for downloading text content from the list and storing to database for later processing. 

Based on:
- [Requests](https://github.com/kennethreitz/requests) is an ISC Licensed HTTP library, written in Python
- [kvlite](https://github.com/ownport/kvlite) is key-value database wrapper for SQL database (MySQL, SQLite)

massfetch supports the next HTTP methods: HEAD and GET. 

## Requests interface

To fetch HTTP content via massfetch you can use the list of URLs, or create container (kvlite database) with detail request parameters.

The list of URLs:
```
http://localhost:8080/page0001
http://localhost:8080/page0002
http://localhost:8080/page0003
http://localhost:8080/page0004
...
http://localhost:8080/page1000
```

In case of use URL list all requests will be done via GET method.

If you need to make more specific request to web resource, better to create container.

## Container

The container is kvlite database with limited amount of records. Each record has parameters to specify request more detail.









