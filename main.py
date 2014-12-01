# -*- coding: utf-8 -*-

__author__ = "KeyWeeUsr"
__version__ = "0.3.0"

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
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
            text: 'kDicts v0.3'
        Button:
            text: 'About'
            on_release: root.about()
    Carousel:
        id: slides
        ScrollView:
            GridLayout:
                cols: 1
                id: scrollwords
                size_hint: 1,None
                size: 0,root.words_height
        BoxLayout:
            orientation: 'vertical'
            TextInput:
                background_color: 0,0,0,1
                foreground_color: 1,1,1,1
                id: EditText
                hint_text: 'Press \\'Load\\' button.'
            BoxLayout:
                size_hint_y: 0.1
                Button:
                    text: 'Save'
                    on_release: root.edit_save()
                Button:
                    text: 'Load'
                    on_release: root.edit_load()
                Button:
                    text: 'Help'
                    on_release: root.edit_help()

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

<EditHelp>:
    size_hint: 0.8,None
    size_y: self.height
    Label:
        text_size: self.width, None
        size_hint_x: 0.98
        size_hint_y: None
        height: (self.texture_size[1]+20)
        text: '[i][size=25]Help[/size][/i]\\nAll of the saved words are written as [word]+<space>+[translation]+<enter>. Spaces in the \\'word\\' or in the \\'translation\\' are not tolerated, use underscore instead. \\nFor example: \\"apple your_translation_for_apple\\npear your_translation_for_pear\\" An <enter> in not a neccessary after the last word with translation.'
        markup: True
''')

class Word(BoxLayout):
    word = StringProperty()
    translation = StringProperty()

class EditHelp(ModalView):
    pass

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
        self.edithelp = EditHelp()
        self.load()

    def load(self):
        with open(self.path+'/kDicts.txt','rU') as f:
           for line in f:
               (word,translation) = line.split()
               self.dictionary[str(word)] = translation
        self.ids.scrollwords.clear_widgets(children=None)
        self.words_height=0
        each_word = 0
        for i in sorted(self.dictionary):
            self.ids.scrollwords.add_widget(Word(word=str(i),translation=str(self.dictionary[i])))
            each_word = each_word+1
        self.words_height = each_word*20 + each_word*10
        self.ids.scrollwords.size = (0,int(self.words_height))

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

    def edit_save(self):
        self.backup()
        with open(self.path+'/kDicts.txt','w') as f:
            f.write(str(self.ids.EditText.text))
        self.load()
        self.ids.slides.load_previous()

    def edit_load(self):
        with open(self.path+'/kDicts.txt','rU') as f:
            self.ids.EditText.text = f.read()

    def edit_help(self):
        self.edithelp.open()

class kDicts(App):

    use_kivy_settings = False
    def open_settings(self,*largs):
        pass

    def build(self):
        return Body()

if __name__ == '__main__':
    kDicts().run()
