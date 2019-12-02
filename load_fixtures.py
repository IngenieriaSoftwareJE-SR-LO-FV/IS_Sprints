from os import listdir, system
from os.path import isfile, join



system("python manage.py loaddata fixtures\\"+" fixtures\\".join(listdir("fixtures")))
