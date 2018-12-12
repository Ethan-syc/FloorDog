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
Documents/GitHub/FloorDog <br>
├── CSVs <br>
│   ├── description.txt <br>
│   ├── men.csv <br>
│   ├── men_color.csv <br>
│   ├── men_des_dict.csv <br>
│   ├── women.csv <br>
│   ├── women_color.csv <br>
│   └── women_mat_dict.csv <br>
├── README.md <br>
├── __pycache__ <br>
├── category.txt <br>
├── create.sql <br>
├── manage.py <br>
├── project316 <br>
│   ├── Scrapping <br>
│   │   ├── color_recognition.py <br>
│   │   ├── comb_scrapping.py <br>
│   │   ├── des_dict.py <br>
│   │   ├── encode_comb.py <br>
│   │   ├── get_comb_url.py <br>
│   │   ├── get_img_url.py <br>
│   │   ├── get_product_description.py <br>
│   │   ├── get_product_url.py <br>
│   │   ├── item_scrapping.py <br>
│   │   ├── merge_csv.py <br>
│   │   ├── scrape.py <br>
│   │   ├── scrapping_tools.py <br>
│   │   ├── ssense.py <br>
│   │   ├── ssense_with_comb.py <br>
│   │   └── test.py <br>
│   ├── __init__.py <br>
│   ├── __pycache__ <br>
│   ├── settings.py <br>
│   ├── urls.py <br>
│   └── wsgi.py <br>
├── requirements.txt <br>
├── templates <br>
├── upload <br>
│   ├── __init__.py <br>
│   ├── __pycache__ <br>
│   ├── admin.py <br>
│   ├── apps.py <br>
│   ├── forms.py <br>
│   ├── migrations <br>
│   ├── models.py <br>
│   ├── recommend.py <br>
│   ├── static <br>
│   │   └── upload <br>
│   │       ├── css <br>
│   │       │   ├── basic.css <br>
│   │       │   ├── dropzone.css <br>
│   │       │   └── stylus <br>
│   │       ├── images <br>
│   │       └── js <br>
│   │           ├── dropzone-amd-module.js <br>
│   │           ├── dropzone-amd-module.min.js <br>
│   │           ├── dropzone.js <br>
│   │           └── dropzone.min.js <br>
│   ├── templates <br>
│   │   └── upload <br>
│   │       └── index.html <br>
│   ├── tests.py <br>
│   ├── urls.py <br>
│   └── views.py <br>
├── venv <br>
│   ├── bin <br>
│   │   ├── __pycache__ <br>
│   │   │   └── django-admin.cpython-37.pyc <br>
│   │   ├── activate <br>
│   │   ├── activate.csh <br>
│   │   ├── activate.fish <br>
│   │   ├── django-admin <br>
│   │   ├── django-admin.py <br>
│   │   ├── easy_install <br>
│   │   ├── easy_install-3.7 <br>
│   │   ├── pip <br>
│   │   ├── pip3 <br>
│   │   ├── pip3.7 <br>
│   │   ├── python <br>
│   │   ├── python3 <br>
│   │   └── python3.7 <br>
│   ├── include <br>
│   ├── lib <br>
│   │   └── python3.7 <br>
│   │       └── site-packages <br>
│   ├── pip-selfcheck.json <br>
│   └── pyvenv.cfg <br>
└── website <br>
    ├── __init__.py <br>
    ├── __pycache__ <br>
    ├── admin.py <br>
    ├── apps.py <br>
    ├── color_recognition_tool.py <br>
    ├── fas_resnet_pred.py <br>
    ├── forms.py <br>
    ├── id_lists <br>
    ├── migrations <br>
    ├── models.py <br>
    ├── rec_tools.py <br>
    ├── recommend.py <br>
    ├── static <br>
    │   ├── css <br>
    │   │   ├── animate.css <br>
    │   │   ├── bootstrap.min.css<br>
    │   │   ├── classy-nav.min.css<br>
    │   │   ├── core-style.css<br>
    │   │   ├── core-style.css.map<br>
    │   │   ├── customize.css<br>
    │   │   ├── font-awesome.min.css<br>
    │   │   ├── jquery-ui.min.css<br>
    │   │   ├── magnific-popup.css<br>
    │   │   ├── nice-select.css<br>
    │   │   ├── owl.carousel.css<br>
    │   │   └── style.css<br>
    │   ├── fonts<br>
    │   ├── img<br>
    │   │   ├── bg-img<br>
    │   │   ├── core-img<br>
    │   │   ├── hover-img<br>
    │   │   ├── icon-img<br>
    │   │   └── product-img<br>
    │   ├── js<br>
    │   ├── scss<br>
    │   └── website<br>
    │       └── images<br>
    ├── support<br>
    │   ├── fas_resnet101_men_100000.pt<br>
    │   ├── fas_resnet101_women_100000.pt<br>
    │   ├── men_complete_coding.csv<br>
    │   └── women_complete_coding.csv<br>
    ├── templates<br>
    │   └── website<br>
    │       ├── detail_page.html<br>
    │       ├── filter_page.html<br>
    │       ├── filter_result.html<br>
    │       ├── index.html<br>
    │       ├── upload_gender.html<br>
    │       ├── upload_page.html<br>
    │       └── upload_result.html<br>
    ├── templatetags<br>
    ├── tests.py<br>
    ├── uploaded_files<br>
    ├── urls.py<br>
    └── views.py<br>
<br>
58 directories, 229 files
