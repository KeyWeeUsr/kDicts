# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BoundedNumericProperty
from kivy.uix.modalview import ModalView

import os
import time
import sys

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
        TextInput:
            id: newone
            size_hint: 1,0.1
            multiline: False
        TextInput:
            id: newonetrans
            size_hint: 1,0.1
            multiline: False
        BoxLayout:
            Button:
                text: 'Done'
                on_release: root.body.add()
''')

class NewWord(ModalView):
    pass

class Word(BoxLayout):
    val = StringProperty()
    word = StringProperty()
    
class Body(BoxLayout):

    capital=0
    dictionary = {}
    path = os.path.dirname(os.path.abspath(__file__))+'/data'
    selectedlabel = 'word'
    temp = {}
    words_height = BoundedNumericProperty(0,min=0)

    def __init__(self, **kwargs):
        super(Body,self).__init__(**kwargs)
        self.modalnew = NewWord()
        self.modalnew.body = self
        self.load()

    def load(self):
        with open(self.path+'/gloss.txt') as f:
           for line in f:
               (key,val) = line.split()
               self.temp[str(key)] = val
        self.dictionary = self.temp
        self.temp = {}
        self.ids.scrollwords.clear_widgets(children=None)
        for i in sorted(self.dictionary):
            self.words_height = self.words_height + 20
            self.ids.scrollwords.add_widget(Word(word=str(i),val=str(self.dictionary[i])))

    def save(self):
        with open(self.path+'/gloss.txt','w') as f:
            for i in self.dictionary:
                f.write(str(i + ' ' + self.dictionary[i] + '\n'))

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

    def add(self):
        self.backup()
        word = self.modalnew.ids.newone.text
        tran = self.modalnew.ids.newonetrans.text
        self.dictionary[word] = tran
        self.save()
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

    def shift(self):
        if self.capital == 0:
            self.capital=1
        elif self.capital ==1:
            self.capital=0

    def change(self, screen):
        self.modalnew.ids.kboard.current = screen

class Glossary(App):
    def build(self):
        return Body()

if __name__ == '__main__':
    Glossary().run()
