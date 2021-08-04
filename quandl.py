# -*- coding: utf-8 -*-
import pandas as pd
import quandl

appl = quandl.get("WIKI/AAPL.11", start_date="2013-12-31", end_date="2015-12-31")
cisco = quandl.get("WIKI/CSCO.11", start_date="2013-12-31", end_date="2015-12-31")
amzn = quandl.get('WIKI/AMZN.11', start_date="2013-12-31", end_date="2015-12-31")
ibm = quandl.get('WIKI/IBM.11', start_date="2013-12-31", end_date="2015-12-31")

appl.to_csv('C:\\software\\python\\APPL_CLOSE')
cisco.to_csv('C:\\software\\python\\CISCO_CLOSE')
amzn.to_csv('C:\\software\\python\\AMZN_CLOSE')
ibm.to_csv('C:\\software\\python\\IBM_CLOSE')

                    
                                         