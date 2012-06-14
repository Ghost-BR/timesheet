import os
import sys


PROJECT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

if os.path.isdir(PROJECT_DIR):
    sys.path.insert(0, PROJECT_DIR)

from timesheet.mainwindow import main
main()
