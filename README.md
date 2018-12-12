# Project FloorDog
## Project Description: 
This is the repo for Duke University COMPSCI 316 Introduction to Databases's team project.
<br> It is a full-stack web project that use database with machine learning algorithms to provide searching and recommendation functionality for dressing fashion.
## License:
This repo should be under MIT license
<br>
## Brief overview of code structure:
CSVs directory stores the major data sources of FloorDog.
website directory stores the Django app website. Important files are:
	1. forms.py: sets up forms that will be sent in our browser,
	2. views.py: controls the execution and function of FloorDog.
	3. models.py: database schema
	4. urls.py: controls how each type of url's parameter, correlated views.py method, and name for reverse() function.
	5. rec_tools.py and related programs for recommendation as well as neural network training.
	6. static directory stores the images, css, javascript, fonts for our HTMLs.
	7. template/website directory stores our HTML templates.
	8. support directory stores the training weight of FloorDog's color recognition and category prediction neural network.
upload directory stores the Dropzone.js implementation of our Drag and Drop file-uploading function.
venv directory stores the nesccesry file for Django execution.
project316 directory stores the major python program that set up the Django environment, including settings.py.
<br>
## Transfer the database:
Make sure postgreSQL is already installed in your environment.
In your postgreSQL environment, type in "create database project316"
After the database have been set up, return to terminal and try to run the server by inputing "python mange.py runserver" under FloorDog directory.
If error occures, open project316/settings.py, and made related changes in the code for implementing database. In most case, delete the line of USER and PASSWORD would be sufficient.
<quote>
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project316',
        'USER': 'shunnnli',
        'PASSWORD': 'xxxxxx',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
</quote>
If the server can be run suffecessfully, open FloorDog/create.sql, change the command into your own path.
<quoate>
	copy website_modelName from '/path/to/csv/file.csv' with delimiter ',' NULL as E'\'\'' CSV;
</quoate>
Either run the changed create.sql, or just open the postgreSQL shell, and copy each command into the shell. Sucessful transferation should be visibale through the prompt.
<br>
## Adjust the neural network:
If you want to adjust the training weight of FloorDog's neural network, you can find it in website/support directory.
<br>
## Open FloorDog
To open FloorDog, firstly make sure the uploaded_files directory at FloorDog/website/uploaded_files is being emptyed. 
Then, open the terminal/pyCharm, make sure the current directory is FloorDog, and typed in the commend "python manage.py runserver".
Open the local host address provided in the prompt, which should be http://127.0.0.1:8000/
FloorDog should now be opened and ready to use in your browser.
<br>
## Limitation of current implementation:
The most significant limitation is that we still run FloorDog on local host, which hugely limites its capabilities.
The database on postgreSQL is also not shared. We need to create a new project316 database on each new computer that runs FloorDog.
<br>
## Tree of FloorDog directory:
Documents/GitHub/FloorDog
├── CSVs <br>
│   ├── description.txt <br>
│   ├── men.csv
│   ├── men_color.csv
│   ├── men_des_dict.csv
│   ├── women.csv
│   ├── women_color.csv
│   └── women_mat_dict.csv
├── README.md
├── __pycache__
│   └── manage.cpython-37.pyc
├── category.txt
├── create.sql
├── manage.py
├── project316
│   ├── Scrapping
│   │   ├── color_recognition.py
│   │   ├── comb_scrapping.py
│   │   ├── des_dict.py
│   │   ├── encode_comb.py
│   │   ├── get_comb_url.py
│   │   ├── get_img_url.py
│   │   ├── get_product_description.py
│   │   ├── get_product_url.py
│   │   ├── item_scrapping.py
│   │   ├── merge_csv.py
│   │   ├── scrape.py
│   │   ├── scrapping_tools.py
│   │   ├── ssense.py
│   │   ├── ssense_with_comb.py
│   │   └── test.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── templates
├── upload
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── admin.cpython-37.pyc
│   │   ├── forms.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-37.pyc
│   │       └── __init__.cpython-37.pyc
│   ├── models.py
│   ├── recommend.py
│   ├── static
│   │   └── upload
│   │       ├── css
│   │       │   ├── basic.css
│   │       │   ├── dropzone.css
│   │       │   └── stylus
│   │       ├── images
│   │       └── js
│   │           ├── dropzone-amd-module.js
│   │           ├── dropzone-amd-module.min.js
│   │           ├── dropzone.js
│   │           └── dropzone.min.js
│   ├── templates
│   │   └── upload
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── venv
│   ├── bin
│   │   ├── __pycache__
│   │   │   └── django-admin.cpython-37.pyc
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── django-admin
│   │   ├── django-admin.py
│   │   ├── easy_install
│   │   ├── easy_install-3.7
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.7
│   │   ├── python
│   │   ├── python3
│   │   └── python3.7
│   ├── include
│   ├── lib
│   │   └── python3.7
│   │       └── site-packages
│   │           ├── Django-2.1.3.dist-info
│   │           ├── django
│   │           ├── easy-install.pth
│   │           ├── pip-10.0.1-py3.7.egg
│   │           ├── psycopg2
│   │           ├── psycopg2-2.7.5.dist-info
│   │           ├── psycopg2_binary-2.7.6.1.dist-info
│   │           ├── pytz
│   │           ├── pytz-2018.7.dist-info
│   │           ├── setuptools-39.1.0-py3.7.egg
│   │           └── setuptools.pth
│   ├── pip-selfcheck.json
│   └── pyvenv.cfg
└── website
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── admin.cpython-37.pyc
    │   ├── apps.cpython-37.pyc
    │   ├── color_recognition_tool.cpython-37.pyc
    │   ├── fas_resnet_pred.cpython-37.pyc
    │   ├── forms.cpython-37.pyc
    │   ├── models.cpython-37.pyc
    │   ├── rec_tools.cpython-37.pyc
    │   ├── recommend.cpython-37.pyc
    │   ├── urls.cpython-37.pyc
    │   └── views.cpython-37.pyc
    ├── admin.py
    ├── apps.py
    ├── color_recognition_tool.py
    ├── fas_resnet_pred.py
    ├── forms.py
    ├── id_lists
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_auto_20181205_2057.py
    │   ├── 0003_auto_20181205_2057.py
    │   ├── 0004_auto_20181205_2101.py
    │   ├── 0005_auto_20181205_2104.py
    │   ├── 0006_auto_20181205_2109.py
    │   ├── 0007_auto_20181205_2148.py
    │   ├── 0008_auto_20181205_2150.py
    │   ├── 0009_auto_20181206_0535.py
    │   ├── 0010_auto_20181207_2347.py
    │   ├── 0011_auto_20181207_2348.py
    │   ├── 0012_uploadfile.py
    │   ├── 0013_delete_uploadfile.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-37.pyc
    │       ├── 0002_auto_20181205_2057.cpython-37.pyc
    │       ├── 0003_auto_20181205_2057.cpython-37.pyc
    │       ├── 0004_auto_20181205_2101.cpython-37.pyc
    │       ├── 0005_auto_20181205_2104.cpython-37.pyc
    │       ├── 0006_auto_20181205_2109.cpython-37.pyc
    │       ├── 0007_auto_20181205_2148.cpython-37.pyc
    │       ├── 0008_auto_20181205_2150.cpython-37.pyc
    │       ├── 0009_auto_20181206_0535.cpython-37.pyc
    │       ├── 0010_auto_20181207_2347.cpython-37.pyc
    │       ├── 0011_auto_20181207_2348.cpython-37.pyc
    │       ├── 0012_uploadfile.cpython-37.pyc
    │       ├── 0013_delete_uploadfile.cpython-37.pyc
    │       └── __init__.cpython-37.pyc
    ├── models.py
    ├── rec_tools.py
    ├── recommend.py
    ├── static
    │   ├── css
    │   │   ├── animate.css
    │   │   ├── bootstrap.min.css
    │   │   ├── classy-nav.min.css
    │   │   ├── core-style.css
    │   │   ├── core-style.css.map
    │   │   ├── customize.css
    │   │   ├── font-awesome.min.css
    │   │   ├── jquery-ui.min.css
    │   │   ├── magnific-popup.css
    │   │   ├── nice-select.css
    │   │   ├── owl.carousel.css
    │   │   └── style.css
    │   ├── fonts
    │   │   ├── FontAwesome.otf
    │   │   ├── fontawesome-webfont.eot
    │   │   ├── fontawesome-webfont.svg
    │   │   ├── fontawesome-webfont.ttf
    │   │   ├── fontawesome-webfont.woff
    │   │   ├── fontawesome-webfont.woff2
    │   │   ├── helvetica_neu_bold-webfont.ttf
    │   │   ├── helvetica_neu_bold-webfont.woff
    │   │   ├── helvetica_neu_bold-webfont.woff2
    │   │   ├── helveticaneue_medium-webfont.ttf
    │   │   ├── helveticaneue_medium-webfont.woff
    │   │   └── helveticaneue_medium-webfont.woff2
    │   ├── img
    │   │   ├── bg-img
    │   │   │   ├── 1.jpg
    │   │   │   ├── 2.jpg
    │   │   │   ├── 3.jpg
    │   │   │   ├── 4.jpg
    │   │   │   ├── 5.jpg
    │   │   │   ├── 6.jpg
    │   │   │   ├── 7.jpg
    │   │   │   ├── 8.jpg
    │   │   │   ├── 9.jpg
    │   │   │   ├── cart1.jpg
    │   │   │   ├── cart2.jpg
    │   │   │   └── cart3.jpg
    │   │   ├── core-img
    │   │   │   ├── favicon.ico
    │   │   │   ├── logo.png
    │   │   │   ├── logo2.png
    │   │   │   └── search.png
    │   │   ├── hover-img
    │   │   │   ├── product1.jpeg
    │   │   │   ├── product1.jpg
    │   │   │   ├── product2.jpeg
    │   │   │   ├── product2.jpg
    │   │   │   ├── product3.jpeg
    │   │   │   ├── product3.jpg
    │   │   │   ├── product4.jpg
    │   │   │   ├── product41.jpg
    │   │   │   ├── product5.jpg
    │   │   │   └── product6.jpg
    │   │   ├── icon-img
    │   │   │   ├── cole.png
    │   │   │   └── dress.png
    │   │   └── product-img
    │   │       ├── pro-big-1.jpg
    │   │       ├── pro-big-2.jpg
    │   │       ├── pro-big-3.jpg
    │   │       ├── pro-big-4.jpg
    │   │       ├── product1.jpeg
    │   │       ├── product1.jpg
    │   │       ├── product2.jpg
    │   │       ├── product2.png
    │   │       ├── product3.jpeg
    │   │       ├── product3.jpg
    │   │       ├── product41.jpg
    │   │       ├── product5.jpeg
    │   │       ├── product5.jpg
    │   │       └── product6.jpg
    │   ├── js
    │   │   ├── active.js
    │   │   ├── bootstrap.min.js
    │   │   ├── classy-nav.min.js
    │   │   ├── jquery
    │   │   │   └── jquery-2.2.4.min.js
    │   │   ├── map-active.js
    │   │   ├── plugins.js
    │   │   ├── popper.min.js
    │   │   └── upload.js
    │   ├── scss
    │   │   ├── _mixin.scss
    │   │   ├── _responsive.scss
    │   │   ├── _theme_color.scss
    │   │   ├── _variables.scss
    │   │   ├── style.scss
    │   │   └── upload.scss
    │   └── website
    │       └── images
    ├── support
    │   ├── fas_resnet101_men_100000.pt
    │   ├── fas_resnet101_women_100000.pt
    │   ├── men_complete_coding.csv
    │   └── women_complete_coding.csv
    ├── templates
    │   └── website
    │       ├── detail_page.html
    │       ├── filter_page.html
    │       ├── filter_result.html
    │       ├── index.html
    │       ├── upload_gender.html
    │       ├── upload_page.html
    │       └── upload_result.html
    ├── templatetags
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   ├── proper_pagination.cpython-37.pyc
    │   │   └── url_replace.cpython-37.pyc
    │   ├── proper_pagination.py
    │   └── url_replace.py
    ├── tests.py
    ├── uploaded_files
    ├── urls.py
    └── views.py
<br>
58 directories, 229 files
