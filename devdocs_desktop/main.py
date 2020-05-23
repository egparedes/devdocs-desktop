#! /usr/bin/env python
import signal

import dbus

from devdocs_desktop import BUS_NAME, DBusGMainLoop, DevdocsDesktop, DevdocsDesktopService


def run():
  DBusGMainLoop(set_as_default=True)
  signal.signal(signal.SIGINT, signal.SIG_DFL)

  if dbus.SessionBus().request_name(BUS_NAME) != dbus.bus.REQUEST_NAME_REPLY_PRIMARY_OWNER:
    devdocs = dbus.SessionBus().get_object(BUS_NAME, BUS_PATH)
    method  = devdocs.get_dbus_method('search')
    method(sys.argv)
  else:
    devdocs = DevdocsDesktop()
    service = DevdocsDesktopService(devdocs)
    devdocs.run()

if __name__ == "__main__":
  run()
