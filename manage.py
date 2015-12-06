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
#
# workflow on deployment:
# workon rater
# mv personal_proj3 personal_proj3.9.4
# git clone https://haleyyew:HHYYbbyy920617_@github.com/haleyyew/personal_proj3.git
# cd personal_proj3
# python manage.py makemigrations BlogRater
# python manage.py migrate
# python manage.py createsuperuser