#!/usr/bin/python
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.label = Gtk.Label(label="Hello World", angle=45, halign=Gtk.Align.START)
        self.box.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button(label="Click Here", halign=Gtk.Align.START)
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        print("Hello World")


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
