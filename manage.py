#!/usr/bin/env python
# 

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser
import time
from multiprocessing import Process

def open_browser():
    """Open the browser after a short delay."""
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:8000/")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecc.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Only open the browser on the first run, not the autoreloader
    if len(sys.argv) > 1 and sys.argv[1] == "runserver" and os.environ.get("RUN_MAIN") != "true":
        Process(target=open_browser).start()

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
