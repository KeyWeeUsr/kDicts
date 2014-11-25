# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BoundedNumericProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.modalview import ModalView

import os
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

Builder.load_string('''
<Body>:
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1,0.08
        Button:
            text: 'Add'
            on_release: root.modalnew.open()
        Label:
            text: 'Glossary v0.1\\n(c)P.B. 2014'
        Button:
            text: 'Save'
            on_release: root.save()
    ScrollView:
        GridLayout:
            cols: 1
            id: scrollwords
            size_hint: 1,None
            size: 0,root.words_height
    
<Word>
    size_hint: 1,None
    height: 30
    Label:
        text: root.word
    Label:
        text: root.val
<NewWord>:
    id: ModalNew
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: newone
            size_hint: 1,0.1
        Label:
            id: newonetrans
            size_hint: 1,0.1
        ScreenManager:
            id: kboard
            Screen:
                name: 'default'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        Button:
                            text: '<-'
                            on_release: root.body.back()
                        Button:
                            text: '->'
                            on_release: root.body.next()
                    BoxLayout:
                        Button:
                            text: 'q'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'w'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'e'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'r'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 't'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'y'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'u'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'i'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'o'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'p'
                            on_release: root.body.write(self.text)
                    BoxLayout:
                        Button:
                            text: 'a'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 's'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'd'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'f'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'g'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'h'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'j'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'k'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'l'
                            on_release: root.body.write(self.text)
                    BoxLayout:
                        Button:
                            text: '^'
                            on_release: root.body.shift()
                        Button:
                            text: 'z'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'x'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'c'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'v'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'b'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'n'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'm'
                            on_release: root.body.write(self.text)
                        Button:
                            text: '<<'
                            on_release: root.body.erase()
                    BoxLayout:
                        Button:
                            text: '?'
                            on_release: root.body.change('others')
                        Button:
                            text: '<space>'
                            on_release: root.body.write(' ')
                        Button:
                            text: 'Done'
                            on_release: root.body.add()
            Screen:
                name: 'others'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        Button:
                            text: '<-'
                            on_release: root.body.back()
                        Button:
                            text: '->'
                            on_release: root.body.next()
                    BoxLayout:
                        Button:
                            text: 'ä'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ë'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ö'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ü'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ß'
                            on_release: root.body.write(self.text)
                    BoxLayout:
                        Button:
                            text: 'Ä'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Ë'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Ö'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Ü'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'á'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'é'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'í'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ó'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ú'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ý'
                            on_release: root.body.write(self.text)
                    BoxLayout:
                        Button:
                            text: 'ŕ'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ĺ'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ř'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ť'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'š'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ď'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ľ'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'ž'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'č'
                            on_release: root.body.write(self.text)
                    BoxLayout:
                        Button:
                            text: 'ň'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Ú'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Ř'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Ľ'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Š'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Č'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Ť'
                            on_release: root.body.write(self.text)
                        Button:
                            text: 'Ž'
                            on_release: root.body.write(self.text)
                        Button:
                            text: '<<'
                            on_release: root.body.erase()
                    BoxLayout:
                        Button:
                            text: 'Back'
                            on_release: root.body.change('default')
                        Button:
                            text: '<space>'
                            on_release: root.body.write(' ')
                        Button:
                            text: 'Done'
                            on_release: root.body.add()
''')

class NewWord(ModalView):
    pass

class Word(BoxLayout):
    word = StringProperty()
    val = StringProperty()
    
class Body(BoxLayout):
    def __init__(self, **kwargs):
        super(Body,self).__init__(**kwargs)
        self.modalnew = NewWord()
        self.modalnew.body = self
        self.load()
    temp = {}
    dictionary = {}
    path = os.path.dirname(os.path.abspath(__file__))+'/data'
    words_height = BoundedNumericProperty(0,min=0)
    def load(self):
        with open(self.path+'/gloss.txt') as f:
           for line in f:
               (key,val) = line.split()
               self.temp[str(key)] = val
        #print 'file to temp done'
        self.dictionary = self.temp
        self.temp = {}
        #print 'temp to dict done, temp del'
        #print self.dictionary
        #print 'dict^^'
        #print self.temp
        #print 'temp^^'
        self.ids.scrollwords.clear_widgets(children=None)
        for i in sorted(self.dictionary):
            self.words_height = self.words_height + 20
            self.ids.scrollwords.add_widget(Word(word=str(i),val=str(self.dictionary[i])))
    def save(self):
        with open(self.path+'/gloss.txt','w') as f:
            for i in self.dictionary:
                f.write(str(i + ' ' + self.dictionary[i] + '\n'))
        print 'save done'
        with open(self.path+'/gloss.txt', 'rU') as f:
            print f.readlines()
    def backup(self):
        filetime = str(time.ctime())
        filetime = filetime.replace(' ','_')
        filetime = filetime.replace(':','_')
        with open(self.path+'/gloss' + filetime + '.txt', 'w') as f:
            for i in self.dictionary:
                f.write(str(i + ' ' + self.dictionary[i] + '\n'))
    def next(self):
        self.selectedlabel = 'trans'
    def back(self):
        self.selectedlabel = 'word'
    selectedlabel = 'word'
    def add(self):
        self.backup()
        word = self.modalnew.ids.newone.text
        tran = self.modalnew.ids.newonetrans.text
        self.dictionary[word] = tran
        self.save()
        print self.dictionary
        self.selectedlabel = 'word'
        self.load()
        self.modalnew.ids.newone.text = ''
        self.modalnew.ids.newonetrans.text = ''
        self.modalnew.dismiss()
    def write(self, letter):
        if self.capital == 0:
            if self.selectedlabel == 'word':
                self.modalnew.ids.newone.text = self.modalnew.ids.newone.text + letter
            elif self.selectedlabel == 'trans':
                self.modalnew.ids.newonetrans.text = self.modalnew.ids.newonetrans.text + letter
        elif self.capital == 1:
            if self.selectedlabel == 'word':
                self.modalnew.ids.newone.text = self.modalnew.ids.newone.text + letter.upper()
            elif self.selectedlabel == 'trans':
                self.modalnew.ids.newonetrans.text = self.modalnew.ids.newonetrans.text + letter.upper()
    def erase(self):
        if self.selectedlabel == 'word':
            self.modalnew.ids.newone.text = self.modalnew.ids.newone.text[:-1]
        elif self.selectedlabel == 'trans':
            self.modalnew.ids.newonetrans.text = self.modalnew.ids.newonetrans.text[:-1]
    capital=0
    def shift(self):
        self.capital=1
    def change(self, screen):
        self.modalnew.ids.kboard.current = screen
class Glossary(App):
    def build(self):
        return Body()

if __name__ == '__main__':
    Glossary().run()