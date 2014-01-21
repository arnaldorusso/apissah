#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#import time, os
from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.button import Button

class apissah(App):
    def build(self):
        return Button(text = 'Test')

apissah().run()
    #~ def running(tt):
        #~ for j in range(tt, -1, -1):
            #~ os.system('clear')
            #~ print('%0.2d'  % (j/60) + ':' + '%0.2d' % (j%60))
            #~ time.sleep(1.0)
        #~ Over()
    #~ 
    #~ def Over():
        #~ for i in range(5):
            #~ os.system('clear')
            #~ print 'Atention!!!'
            #~ time.sleep(0.5)
            #~ os.system('clear')
            #~ time.sleep(0.5)
        #~ Repeat()
    #~ 
    #~ def Repeat():
        #~ again = raw_input('Again? (y/n): ')
        #~ if again == 'y' or again == 'Y':
            #~ main()
        #~ elif again == 'n' or again == 'N':
            #~ print('Goodbye!')
            #~ time.sleep(1.0)
            #~ return
        #~ else:
            #~ print('Press `y` or `n`')
            #~ Repeat()
    #~ 
    #~ def func_except():
        #~ print('Time must be positive seconds')
        #~ main()
    #~ 
    #~ def main():
        #~ try:
            #~ value = raw_input('Type time in seconds or `q` to quit: ')
            #~ if value == 'q':
                #~ print('Goodbye!')
                #~ return
            #~ else:
                #~ if int(value) < 0:
                    #~ func_except()
                #~ if int(value) > 0:
                    #~ running(int(value))
                #~ else:
                    #~ func_except()
            #~ return Button(text=value)
        #~ except KeyboardInterrupt:
            #~ return
    #~ 
    #~ if __name__ == '__main__':
        #~ main()
