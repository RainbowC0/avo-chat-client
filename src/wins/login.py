import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

@Gtk.Template(filename='res/ui/login.ui')
class LoginWindow(Gtk.Window):
    __gtype_name__ = 'login_window'

    provider = Gtk.CssProvider()
    provider.load_from_path('res/css/style.css')
    ety_userid = Gtk.Template.Child('ety_userid')
    ety_password = Gtk.Template.Child('ety_password')

    @Gtk.Template.Callback()
    def onDestroy(self, *args):
        Gtk.main_quit()

    @Gtk.Template.Callback()
    def onLogin(self, button):
        print(self.ety_userid.get_text())
        print(self.ety_password.get_text())

win = LoginWindow()
hd = win.get_titlebar()
hd.get_style_context().add_provider(win.provider, 600)
win.show_all()

Gtk.main()
