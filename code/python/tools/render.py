#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
from optparse import OptionParser

import PyQt4
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication
#from PyQt4.QtWidgets import QApplication
from PyQt4.QtWebKit import QWebPage

# From: https://impythonist.wordpress.com/2015/01/06/ultimate-guide-for-scraping-javascript-rendered-web-pages/
class Render(QWebPage):  
  def __init__(self, url,fn):  
    self.app = QApplication(sys.argv)
    self.fname=fn
    self.url=QUrl(url)
    #url = QUrl(url)
    #username = input('username')
    #password = input('password')

    #base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    #authheader = "Basic %s" % base64string
    
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(self.url)  
    self.app.exec_()  
    time.sleep(5)
  
  def _loadFinished(self, result):  
    f = open( self.fname, 'wt' )
    f.write( self.mainFrame().toHtml() )
    f.close()
    self.app.quit()  


def main():
    options = get_cmd_options()
    Render(options.url,options.file)
    

def get_cmd_options():
    """
        gets and validates the input from the command line
    """
    usage = "usage: %prog [options] args"
    parser = OptionParser(usage)
    parser.add_option('-u', '--url' , dest = 'url' , help = 'URL to fetch data from')
    parser.add_option('-f', '--file', dest = 'file', help = 'Local file path to save data to')

    (options,args) = parser.parse_args()

    if not options.url:
        print 'You must specify an URL.',sys.argv[0],'--help for more details'
        exit(1)
    if not options.file:
        print 'You must specify a destination file.',sys.argv[0],'--help for more details'
        exit(1)

    return options

if __name__ == '__main__':
    main()