#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
from optparse import OptionParser

try:
    __import__('PyQt5')
    use_pyqt5 = True
except ImportError:
    use_pyqt5 = False

if use_pyqt5:
  from PyQt5.QtCore import QUrl , QTimer
  from PyQt5.QtWidgets import QApplication
  from PyQt5.QtWebKitWidgets import QWebPage
  from PyQt5.QtWebKit import QWebSettings
else:
  import PyQt4
  from PyQt4.QtCore import QUrl, QTimer
  from PyQt4.QtGui import QApplication
  from PyQt4.QtWebKit import QWebPage, QWebSettings

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
    self.settings().setAttribute(QWebSettings.AutoLoadImages,False)
    self.settings().setAttribute(QWebSettings.PluginsEnabled,False)
    self.loadFinished.connect(self._loadFinished)

    # doesnt work as expected
    self.timeout_timer = QTimer()
    self.timeout_timer.timeout.connect(self._request_timed_out)
    self.timeout_timer.start(6 * 1000)
    #print ('Init timer')
    self.mainFrame().load(self.url)  
    self.app.exec_()  
    time.sleep(5)
  
  def _loadFinished(self, result):
    #print ("_loadFinished") #comment-replies-renderer-expander-down
    #button = self.mainFrame().findFirstElement('button[class~=comment-replies-renderer-expander-down]')#'button[class="yt-uix-expander-head"]')
    #print (button.toPlainText().toUtf8()) # .encode('utf-8'))
    #res=button.evaluateJavaScript("self.click()")
    #print (res.typeName())
    f = open( self.fname, 'wt' )
    f.write( self.mainFrame().toHtml() )
    f.close()
    print("... Done.")
    self.app.quit()

  def _request_timed_out(self):
    print('Custom request timeout value exceeded.')
    self.timeout_timer.stop()
    self.loadFinished.emit(False)
    self.app.quit()
    sys.exit(0)

def main():
    options = get_cmd_options()
    print ("Start downloading...")
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
        print ('You must specify an URL.',sys.argv[0],'--help for more details')
        exit(1)
    if not options.file:
        print ('You must specify a destination file.',sys.argv[0],'--help for more details')
        exit(1)

    return options

if __name__ == '__main__':
    main()
