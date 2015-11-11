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

        self.pack(fill=BOTH, expand=1)

        # Create a menubar
        mnuMenu = Menu(self.parent)
        self.parent.config(menu=mnuMenu)

        # Create menubar
        mnuFileMenu = Menu(mnuMenu)

        # Add File menu items
        mnuFileMenu.add_command(label='Open', command=self.quit)
        mnuFileMenu.add_command(label='Exit', command=self.quit)

        # Add File menu items to File menu
        mnuMenu.add_cascade(label='File', menu=mnuFileMenu)

        # Create frame for all the widgets
        frame = Frame(self)
        frame.pack(anchor=N, fill=BOTH, expand=1)

        # Create decode button
        btnDecode = Button(frame, text='Decode', command=self.quit)
        btnDecode.pack(side=RIGHT)

        # Create file open dialog
        btnOpenFile = Button(frame, text="Load file", command=self.onBtnOpenFile)
        btnOpenFile.pack(side=RIGHT)

        # Create filename label
        lblFilename = Label(frame, text='No filename chosen...')
        lblFilename.pack(side=LEFT)

        # Create the text widget for the results
        self.txtResults = Text()
        self.txtResults.pack(fill=BOTH, expand=1)

    def onBtnOpenFile(self):
        ftypes = [('XML files', '*.xml'), ('All Files', '*')]
        filename = filedialog.askopenfilename(initialdir='~', title='Choose the file', filetypes=ftypes)

        if filename != '':
            text = self.readFile(filename)
            self.txtResults.insert(END, text)

    def readFile(self, filename):
        fd = open(filename, 'r')
        text = fd.read()

        return text

    def decode(self):
        # Parse the sitemanager.xml file
        doc = parse(sys.argv[1])

        # Loop over Server keys
        for server in doc.getElementsByTagName('Server'):
            for pword in server.getElementsByTagName('Host'):
                print('Host:\t\t%s' % pword.firstChild.nodeValue)

            for pword in server.getElementsByTagName('Pass'):
                # base64 decode the password before printing
                print('Password:\t%s\n' % base64.b64decode(pword.firstChild.nodeValue))


def main():
    root = Tk()
    root.geometry('300x300+300+300')
    app = PyZilla(root)
    root.mainloop()

if __name__ == '__main__':
    main()
