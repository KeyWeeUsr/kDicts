# -*- coding: utf-8 -*-

__author__ = "KeyWeeUsr"
__version__ = "0.2.0"

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, BoundedNumericProperty

import os
import sys
import time

Builder.load_string('''
<Body>:
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1,0.08
        Button:
            text: 'Add'
            on_release: root.newword.open()
        Label:
            text: 'kDicts v0.2'
        Button:
            text: 'About'
            on_release: root.about()
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
        text: root.translation

<NewWord>:
    BoxLayout:
        spacing: 10
        size_hint:0.5,0.7
        pos_hint: {'center_x':0.5,'center_y':0.5}
        orientation: 'vertical'
        Label:
            text: 'Insert a word'
            size_hint: None,0.2
            size: self.texture_size
            pos_hint: {'center_x':0.5}
        TextInput:
            id: newone
            pos_hint: {'center_x':0.5}
            size_hint: 0.8,0.2
            size: 0,30
            multiline: False
        Label:
            text: 'Insert a translation'
            size_hint: None,0.2
            size: self.texture_size
            pos_hint: {'center_x':0.5}
        TextInput:
            id: newonetrans
            pos_hint: {'center_x':0.5}
            size_hint: 0.8,0.2
            size:0,30
            multiline: False
        BoxLayout:
            spacing: 20
            size_hint: 1,0.2
            size: 0,50
            pos_hint: {'center_x':0.5}
            Button:
                text: 'Done'
                on_release: root.body.add()
            Button:
                text: 'Back'
                on_release: root.dismiss()
                
<AboutPopup>:
    size_hint: 0.4,0.4
    BoxLayout:
        size_hint: 0.8,0.8
        orientation: 'vertical'
        Label:
            text: '(C) KeyWeeUsr\\n(P.B.) 2014'
        Button:
            size_hint: 0.6,0.2
            pos_hint: {'center_x':0.5}
            on_release: root.dismiss()
            text: 'Dismiss'
''')

class Word(BoxLayout):
    word = StringProperty()
    translation = StringProperty()

class NewWord(ModalView):
    pass

class AboutPopup(ModalView):
    pass
    
class Body(BoxLayout):

    dictionary = {}
    path = os.path.dirname(os.path.abspath(__file__))+'/data'
    words_height = BoundedNumericProperty(0,min=0)

    def __init__(self, **kwargs):
        super(Body,self).__init__(**kwargs)
        self.newword = NewWord()
        self.newword.body = self
        self.aboutpopup = AboutPopup()
        self.load()

    def load(self):
        with open(self.path+'/kDicts.txt') as f:
           for line in f:
               (word,translation) = line.split()
               self.dictionary[str(word)] = translation
        self.ids.scrollwords.clear_widgets(children=None)
        for i in sorted(self.dictionary):
            self.words_height = self.words_height + 20
            self.ids.scrollwords.add_widget(Word(word=str(i),translation=str(self.dictionary[i])))

    def backup(self):
        filetime = str(time.ctime()).replace(' ','_').replace(':','_')
        with open(self.path+'/kDicts' + filetime + '.txt', 'w') as f:
            for i in self.dictionary:
                f.write(str(i + ' ' + self.dictionary[i] + '\n'))

    def save(self):
        with open(self.path+'/kDicts.txt','w') as f:
            for i in self.dictionary:
                f.write(str(i + ' ' + self.dictionary[i] + '\n'))


    def add(self):
        self.backup()
        word = self.newword.ids.newone.text
        translation = self.newword.ids.newonetrans.text
        self.dictionary[word] = translation
        self.save()
        self.load()
        self.newword.dismiss()
        self.newword.ids.newone.text = ''
        self.newword.ids.newonetrans.text = ''

    def about(self):
        self.aboutpopup.open()

class kDicts(App):

    use_kivy_settings = False
    def open_settings(self,*largs):
        pass

    def build(self):
        return Body()

if __name__ == '__main__':
    kDicts().run()
