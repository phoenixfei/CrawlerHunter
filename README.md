Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

# Installing Scrapy
Alternatively, if you are already familiar with installation of Python Packages, you can install Scrapy and its dependencies from PyPI with: pip install Scrapy
Scrapy is written in pure Python and depends on a few key Python packages (among others):  
***lxml***, an efficient XML and HTML parser  
***parsel***, an HTML/XML data extraction library written on top of lxml  
***w3lib***, a multi-purpose helper for dealing with URLs and web page encodings  
***twisted***, an asynchronous networking framework
***cryptography and pyOpenSSL***, to deal with various network-level security needs  
In windows, you should install twisted by wheel files. See [install scrapy in windows](https://blog.csdn.net/qinlingheshang/article/details/79684537)

# Scrapy Tutorial
## Creating a project
Use command 
> scrapy startproject tutorial[project name] 

This will create a tutorial directory with the following contens:
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
            
## Controlling projects
Go inside the spiders directory, to create a new spieder, 
> scrapy genspider [-t template] <name> <domain>

Usage example:  
> scrapy genspider -l  

Available templates:  
&emsp;&emsp;    basic    
&emsp;&emsp;    crawl  
&emsp;&emsp;    csvfeed  
&emsp;&emsp;    xmlfeed  

> scrapy genspider example example.com

Created spider 'example' using template 'basic'

> scrapy genspider -t crawl scrapyorg scrapy.org

Created spider 'scrapyorg' using template 'crawl'

## Available tool commands
This section contains a list of the available built-in commands with a description. Remember, you can always get more info about each command by running: 
> scrapy <command> -h.   

And you can see all available commands with: 
> scrapy -h.

***Global commands*** :  
**startproject**: create a new scrapy project  
**genspider**: create a new spider in the current project’s spiders folder.   
**runspider**: start crawling using a spider.  
**shell**: start the scrapy shell for the given URL  

***Project-only commands***:   
**crawl**: start crawling using a spider.  

## Our first Spider
