#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RateAuthors_python_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

# python manage.py makemigrations BlogRater
# migrate
# startapp soundcloud_agglomerator
# createsuperuser
#   haoran  password
# deployed: haleyyew haleyyew