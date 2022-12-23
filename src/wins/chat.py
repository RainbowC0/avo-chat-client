#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2022 rainbow <rainbow@kali>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')
from gi.repository import Gtk, Handy

class ListBoxRowWithData(Gtk.ListBoxRow):
	def __init__(self, data):
		super().__init__()
		self.data = data
		self.add(Gtk.Label(label=data))

class App(Gtk.Window):
	def __init__(self):
		super().__init__(title='Chact')
		self.set_border_width(10)
		self.set_position(Gtk.WindowPosition.CENTER)
		
		tb = self.titlebar()

		self.mb = Handy.Leaflet()
		self.mb.set_transition_type(Handy.LeafletTransitionType.SLIDE)
		
		lfb = self.sidebar()
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		box.props.hexpand = True
		sprt = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
		
		self.set_titlebar(tb)
		self.mb.add(lfb)
		self.mb.child_set(lfb, name='left_page')
		self.mb.add(sprt)
		self.mb.add(box)
		self.mb.child_set(box, name='right_page')
		
		self.mb.set_visible_child_name('left_page')
		lst = Gtk.ListBox()
		lst.set_selection_mode(Gtk.SelectionMode.NONE)
		box.pack_start(lst, True, True, 0)
		
		lsr = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		lsr.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, True, True, 0)
		
		lab1 = Gtk.Label(label='Acquirebsbsbzhxb xbdheb', xalign=0)
		lab2 = Gtk.Label(label='Posnxlanxb dhx sh  hs x', xalign=0)
		vbox.pack_start(lab1, True, True, 0)
		vbox.pack_start(lab2, True, True, 0)
		
		swh = Gtk.Switch()
		swh.props.valign = Gtk.Align.CENTER
		hbox.pack_start(swh, False, True, 0)
		
		lst.add(lsr)
		
		strs = 'List is there bug'.split()
		for i in strs:
			lst.add(ListBoxRowWithData(i))
		
		start_size_group = Gtk.SizeGroup(mode=Gtk.SizeGroupMode.HORIZONTAL)
		start_size_group.add_widget(self._lh)
		start_size_group.add_widget(lfb)
		
		end_size_group = Gtk.SizeGroup(mode=Gtk.SizeGroupMode.HORIZONTAL)
		end_size_group.add_widget(self._rh)
		end_size_group.add_widget(box)

		self.add(self.mb)

	def titlebar(self):
		header = Handy.Leaflet()
		header.set_transition_type(Handy.LeafletTransitionType.SLIDE)
		
		lh = Gtk.HeaderBar(
			title='Two Leafs',
			show_close_button=True
		)
		
		rh = Gtk.HeaderBar(
			show_close_button=True,
			hexpand=True
		)
		back_button = Gtk.Button.new_from_icon_name('go-previous-symbolic', 1)
		rh.add(back_button)
		
		self._lh = lh
		self._rh = rh

		header.add(lh)
		header.child_set(lh, name='left_page')
		header.add(Gtk.Separator(orientation=Gtk.Orientation.VERTICAL))
		header.add(rh)
		header.child_set(rh, name='right_page')
		
		self.hd_group = Handy.HeaderGroup()
		self.hd_group.add_gtk_header_bar(lh)
		self.hd_group.add_gtk_header_bar(rh)

		return header

	def sidebar(self):
		side = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		side.set_size_request(200, -1)
		return side

	#def content(self):
	#	return Gtk.Button(label='llllll')

	def button_clicked(self, widget):
		print('knc')

	def b2_clicked(self, widget):
		print('lkkkk')

if __name__ == '__main__':
	win = App()
	win.connect("destroy", Gtk.main_quit)
	win.show_all()
	Gtk.main()
