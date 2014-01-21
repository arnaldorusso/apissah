#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#import time, os
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string("""
<ListViewModal>:
    size_hint: None, None
    size: 400, 400
    ListView:
        size_hint: .6, .6
        item_strings: [str(index) for index in range(25)]
<ListViewRight>:
    size_hint: None, None
    size: 400, 400
    ListView:
        size_hint: .6, .6
        item_strings: [str(index) for index in range(61)]
""")


class ListViewModal(ModalView):
    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)


class ListViewRight(ModalView):
    def __init__(self, **kwargs):
        super(ListViewRight, self).__init__(**kwargs)


class MainView(GridLayout):

    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        super(MainView, self).__init__(**kwargs)
        
        listview_modal = ListViewModal()
        self.add_widget(listview_modal) 
        listview_right = ListViewRight()
        self.add_widget(listview_right)


if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MainView(width=800))
    
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
