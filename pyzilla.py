#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Decode Filezilla locally stored passwords from sitemanager.xml

author: Claude Müller
website: http://unschooled.life

"""

import sys
import base64
from xml.dom.minidom import parse
from tkinter import Tk, Frame, Button, Text, Menu, Label, BOTH, RIGHT, LEFT, END, N
from tkinter import filedialog

class PyZilla(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title('PyZilla')
        self.padding = 5

        self.pack(fill=BOTH, expand=1)

        # Create a menubar
        mnuMenu = Menu(self.parent)
        self.parent.config(menu=mnuMenu)

        # Create menubar
        mnuFileMenu = Menu(mnuMenu)

        # Add File menu items
        mnuFileMenu.add_command(label='Open', command=self.onBtnOpenFile)
        mnuFileMenu.add_command(label='Exit', command=self.quit)

        # Add File menu items to File menu
        mnuMenu.add_cascade(label='File', menu=mnuFileMenu)

        # Create frame for all the widgets
        frame = Frame(self)
        frame.pack(anchor=N, fill=BOTH)

        # Create file open dialog
        btnOpenFile = Button(frame, text="Load file", command=self.onBtnOpenFile)
        btnOpenFile.pack(side=RIGHT, pady=self.padding)

        # Create filename label
        self.lblFilename = Label(frame, text='No filename chosen...')
        self.lblFilename.pack(side=LEFT, pady=self.padding, padx=self.padding)

        # Create the text widget for the results
        self.txtResults = Text(self)
        self.txtResults.pack(fill=BOTH, expand=1, pady=self.padding, padx=self.padding)

    def onBtnOpenFile(self):
        ftypes = [('XML files', '*.xml'), ('All Files', '*')]
        filename = filedialog.askopenfilename(initialdir='~', title='Choose the file', filetypes=ftypes)

        # If a file was selected
        if filename != '':
            self.lblFilename.config(text=filename)
            text = self.decode(filename)
            self.txtResults.insert(END, text)

    def decode(self, filename):
        # Parse the sitemanager.xml file
        doc = parse(filename)
        text = ''

        # Loop over Server keys
        for server in doc.getElementsByTagName('Server'):
            for pword in server.getElementsByTagName('Host'):
                text += 'Host:     %s\n' % pword.firstChild.nodeValue

            for pword in server.getElementsByTagName('Pass'):
                # base64 decode the password before printing
                text += 'Password: %s\n\n' % base64.b64decode(pword.firstChild.nodeValue)

        return text


def main():
    root = Tk()
    root.geometry('800x600+300+300')
    app = PyZilla(root)
    root.mainloop()

if __name__ == '__main__':
    main()
