## Cloudflare bypasser for skystreaming
## Copyleft 2015 gajm
## Released under the WTFPLv2

import sys
from gi.repository import Gtk
from gi.repository import WebKit
from gi.repository import Soup

UA = sys.argv[1]
COOKIE = sys.argv[2]
URL = sys.argv[3]

view = WebKit.WebView()
settings = WebKit.WebSettings()
settings.set_property('user-agent', UA)
settings.set_property('enable-plugins', False)
view.set_settings(settings)

cookiejar = Soup.CookieJarText.new(COOKIE, False)
cookiejar.set_accept_policy(Soup.CookieJarAcceptPolicy.ALWAYS)
session = WebKit.get_default_session()
session.add_feature(cookiejar)
#proxy_uri = Soup.URI.new('http://127.0.0.1:8080')
#session.set_property('proxy-uri', proxy_uri)
##session.set_property('proxy-uri', None)

win = Gtk.Window()
win.set_title('Cloudflare Annoyance')
win.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
win.set_default_size(360, 400)
win.connect('destroy', Gtk.main_quit)
scroll_win = Gtk.ScrolledWindow()
scroll_win.add(view)
win.add(scroll_win)
win.show_all()

def cf_bypass(view, frame):
    for line in open(COOKIE):
        if 'cf_clearance' in line:
            print(line)
            Gtk.main_quit()
            
view.connect('load-progress-changed', cf_bypass)

view.open(URL)
Gtk.main()
