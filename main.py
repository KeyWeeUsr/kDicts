# -*- coding: utf-8 -*-

__author__ = "KeyWeeUsr"
__version__ = "0.5.0"

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, BoundedNumericProperty, ListProperty

import os
import sys
import time

Builder.load_string('''
<Body>:
    canvas:
        Color:
            rgba: root.bg
        Rectangle:
            size: self.size
            pos: self.pos
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1,0.08
        BubbleButton:
            text: 'Add'
            on_release: root.newword.open()
        Label:
            text: 'kDicts v0.5'
        BoxLayout:
            BubbleButton:
                text: 'Color'
                on_release: root.color.open()
            BubbleButton:
                text: 'About'
                on_release: root.about()
    Carousel:
        id: slides
        index: 1
        StyleChooser:
            orientation: 'vertical'
        ScrollView:
            GridLayout:
                cols: 1
                id: scrollwords
                size_hint: 1,None
                size: 0,root.words_height
        BoxLayout:
            orientation: 'vertical'
            TextInput:
                background_color: 0,0,0,0
                foreground_color: 1,1,1,1
                id: EditText
                hint_text: 'Press \\'Load\\' button.'
                hint_text_color: 1,1,1,1
            BoxLayout:
                size_hint_y: 0.1
                BubbleButton:
                    text: 'Save'
                    on_release: root.edit_save()
                BubbleButton:
                    text: 'Load'
                    on_release: root.edit_load()
                BubbleButton:
                    text: 'Help'
                    on_release: root.edit_help()

<Word>
    size_hint: 1,None
    height: 30
    Label:
        text: ('[color=%s]' % root.color) + root.word + '[/color]'
        markup: True
    Label:
        text: root.translation

<NewWord>:
    size_hint: 0.6,0.8
    background: root.path+'/bg.png'
    BoxLayout:
        spacing: 10
        size_hint:0.5,0.7
        pos_hint: {'center_x':0.5,'center_y':0.5}
        orientation: 'vertical'
        Spinner:
            id: wordclass
            size_hint: 0.9,0.2
            pos_hint: {'center_x':0.5}
            text: 'Word classes'
            values: ('Nouns','Adjectives','Pronouns','Numerals','Verbs','Adverbs','Prepositions','Conjunctions','Particles')
        Label:
            text: 'Insert a word'
            size_hint: None,0.2
            size: self.texture_size
            pos_hint: {'center_x':0.5}
        TextInput:
            id: newone
            pos_hint: {'center_x':0.5}
            size_hint: 0.9,0.2
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
            size_hint: 0.9,0.2
            size:0,30
            multiline: False
        BoxLayout:
            spacing: 20
            size_hint: 1,0.2
            size: 0,50
            pos_hint: {'center_x':0.5}
            BubbleButton:
                text: 'Done'
                on_release: root.body.add()
            BubbleButton:
                text: 'Back'
                on_release: root.dismiss()
                
<AboutPopup>:
    size_hint: 0.4,0.1
    background: root.path+'/bg.png'
    BoxLayout:
        size_hint: 0.8,0.8
        orientation: 'vertical'
        Label:
            text: '(C) KeyWeeUsr\\n(P.B.) 2014\\n[i]https://github.com/KeyWeeUsr[/i]\\n[i]https://facebook.com/kDicts[/i]'
            markup: True

<EditHelp>:
    size_hint: 0.8,0.1
    background: root.path+'/bg.png'
    Label:
        text_size: self.width, None
        size_hint_x: 0.98
        size_hint_y: None
        height: (self.texture_size[1]+20)
        text: '[i][size=25]Help[/size][/i]\\nAll of the saved words are written as [word]+<space>+[prefix]+[translation]+<enter>. Spaces in the \\'word\\' or in the \\'translation\\' are not tolerated, use underscore instead. \\n\\nFor example: apple your_translation_for_apple\\n\\nAn <enter> in not a neccessary after the last word with translation.\\nBe careful with prefixes! If there is a typo, app crashes.\\nn_ adj_ pro_ num_ v_ adv_ pre_ con_ par_'
        markup: True

<ColorPopup>:
    background: root.path+'/bg.png'
    size_hint: 0.3,0.3
    BoxLayout:
        size_hint: None,None
        size: self.size
        Label:
            size_hint: None,None
            size: self.size
            id: testing
            text: """[i][color=#0290C8]Nouns[/color]\\n[color=#53BE29]Adjectives[/color]\\n[color=#A65C8B]Pronouns[/color]\\n[color=#FFD01E]Numerals[/color]\\n[color=#F42E00]Verbs[/color]\\n[color=#F997DE]Adverbs[/color]\\n[color=#B665E2]Prepositions[/color]\\n[color=#F0DC82]Conjunctions[/color]\\n[color=#20DFEB]Particles[/color][/i]"""
            markup: True

<StyleChooser>:
    orientation: 'vertical'
    size_hint: 0.5,0.5
    pos_hint: {'center_x':0.5,'center_y':0.5}
    cols: 3
    spacing: 10
    StyleItem:
        stylecolor: (0,0,0,1)
        color: 1,1,1,1
        on_release: root.changestyleitem(self.stylecolor)
    StyleItem:
        stylecolor: (0.5,0.5,0.5,1)
        on_release: root.changestyleitem(self.stylecolor)
    StyleItem:
        stylecolor: (0.8,0.5,0.5,1)
        on_release: root.changestyleitem(self.stylecolor)
    StyleItem:
        stylecolor: (0.9,0.8,0.6,1)
        on_release: root.changestyleitem(self.stylecolor)
    StyleItem:
        stylecolor: (0.5,0.3,0.5,1)
        on_release: root.changestyleitem(self.stylecolor)
    StyleItem:
        stylecolor: (0.7,0.7,0.7,1)
        on_release: root.changestyleitem(self.stylecolor)

<StyleItem>:
    stylecolor: self.stylecolor
    text: self.text
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            size: self.size
            pos: self.pos
        Color:
            rgba: root.stylecolor
        Rectangle:
            size: self.size[0]-4,self.size[1]-4
            pos: self.pos[0]+2,self.pos[1]+2
    Label:
        text: root.text
        pos: root.pos[0],root.pos[1]

<BubbleButton>:
    text: 'test'
    Image:
        source: 'data/bubblebutton.png'
        size_hint: None,None
        pos: root.pos
        size: root.size
        allow_stretch: True
        keep_ratio: False

<WarningPopup>:
    size_hint: 0.4,0.2
    background: root.path+'/bg.png'
    Label:
        text: root.text
        font_size: 16
''')

class WarningPopup(ModalView):
    text = StringProperty()
    path = os.path.dirname(os.path.abspath(__file__))+'/data'

class BubbleButton(ButtonBehavior, Widget):
    path = os.path.dirname(os.path.abspath(__file__))+'/data'

class StyleItem(ButtonBehavior, Widget):
    stylecolor = ListProperty()
    text = StringProperty()
    
class StyleChooser(GridLayout):

    def changestyleitem(self, color):
        self.body.bg = color

class ColorPopup(ModalView):
    path = os.path.dirname(os.path.abspath(__file__))+'/data'

class Word(BoxLayout):
    word = StringProperty()
    translation = StringProperty()
    color = StringProperty('#FF0000')

class EditHelp(ModalView):
    path = os.path.dirname(os.path.abspath(__file__))+'/data'

class NewWord(ModalView):
    path = os.path.dirname(os.path.abspath(__file__))+'/data'

class AboutPopup(ModalView):
    path = os.path.dirname(os.path.abspath(__file__))+'/data'

class Body(BoxLayout):

    dictionary = {}
    path = os.path.dirname(os.path.abspath(__file__))+'/data'
    words_height = BoundedNumericProperty(0,min=0)
    prefix = {'n_':'#0290C8','adj_':'#53BE29','pro_':'#A65C8B','num_':'#FFD01E','v_':'#F42E00','adv_':'#F997DE','pre_':'#B665E2','con_':'#F0DC82','par_':'#20DFEB'}
    wclass = {'Word classes':'','Nouns':'n_','Adjectives':'adj_','Pronouns':'pro_','Numerals':'num_','Verbs':'v_','Adverbs':'adv_','Prepositions':'pre_','Conjunctions':'con_','Particles':'par_'}
    bg = ListProperty([0,0,0,1])

    def __init__(self, **kwargs):
        super(Body,self).__init__(**kwargs)
        self.newword = NewWord()
        self.newword.body = self
        self.aboutpopup = AboutPopup()
        self.color = ColorPopup()
        self.edithelp = EditHelp()
        self.stylechooser = StyleChooser
        self.stylechooser.body = self
        self.warning = WarningPopup()
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
            self.ids.scrollwords.add_widget(Word(color=str(self.checkprefix(str(self.dictionary[i]))),word=str(i).replace('_',' '),translation=str(str(self.removeprefix(self.dictionary[i])).replace('_',' '))))
            each_word = each_word+1
        self.words_height = each_word*20 + each_word*10
        self.ids.scrollwords.size = (0,int(self.words_height))

    def checkprefix(self, word):
        temp=''
        for i in self.prefix:
            if i in word:
                return(self.prefix[i])
            elif i not in word:
                temp='#FFFFFF'
            else:
                continue
        return temp
                
    def removeprefix(self, word):
        for i in self.prefix:
            temp=''
            if i in word:
                return str(word[len(i):]).replace('_',' ')
            elif i not in word:
                temp = str(word)
            else:
                continue
        return temp

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
        word = ''
        translation = ''
        if (word != '') and (translation != ''):
            self.backup()
            word = str(self.newword.ids.newone.text).replace(' ','_')
            translation = self.wclass[str(self.newword.ids.wordclass.text)]+str(self.newword.ids.newonetrans.text).replace(' ','_')
            self.dictionary[word] = translation
            self.save()
            self.load()
        elif (word == '') or (translation == ''):
            self.warning.text = 'Input must not be empty!!!'
            self.warning.open()
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

    def on_pause(self):
        return True

    def build(self):            
        return Body()

if __name__ == '__main__':
    kDicts().run()
