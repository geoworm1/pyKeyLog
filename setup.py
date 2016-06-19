from distutils.core import setup
import py2exe
setup(options = {'py2exe':{'bundle_files': 1, 'compressed': True}}, windows = [{"script":"install.pyw", "icon_resources": [(1, "r.ico")], "dest_base":"myprogram"}], zipfile = None)
