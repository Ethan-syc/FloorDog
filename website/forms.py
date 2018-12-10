from django import forms
from upload.models import UploadFile
from website.models import *


GENDER = (("M", "men"), ("W", "women"))

MEN = (MenClothes.objects.values('category').distinct())
WOMEN = (WomenClothes.objects.values('category').distinct())

# get CATEGORY using this command: cat men.csv women.csv | cut -d , -f 5 | sort -u > category.txt

CATEGORY = (
    ("blazer", "blazer"),
    ("blouse", "blouse"),
    ("bodysuit", "bodysuit"),
    ("bomber", "bomber"),
    ("bustier", "bustier"),
    ("camisole", "camisole"),
    ("cape", "cape"),
    ("cardigan", "cardigan"),
    ("catsuit", "catsuit"),
    ("coat", "coat"),
    ("coatshirt", "coatshirt"),
    ("corset", "corset"),
    ("crewneck", "crewneck"),
    ("denim", "denim"),
    ("dickie", "dickie"),
    ("dress", "dress"),
    ("dresses", "dresses"),
    ("genius", "genius"),
    ("harrington", "harrington"),
    ("hoodie", "hoodie"),
    ("jacket", "jacket"),
    ("jackets-coats", "jackets-coats"),
    ("jeans", "jeans"),
    ("jumper", "jumper"),
    ("jumpsuit", "jumpsuit"),
    ("jumpsuits", "jumpsuits"),
    ("kilt", "kilt"),
    ("leggings", "leggings"),
    ("men", "men"),
    ("miniskirt", "miniskirt"),
    ("minskirt", "minskirt"),
    ("overalls", "overalls"),
    ("overcoat", "overcoat"),
    ("overshirt", "overshirt"),
    ("pant", "pant"),
    ("pants", "pants"),
    ("parka", "parka"),
    ("peacoat", "peacoat"),
    ("polo", "polo"),
    ("poncho", "poncho"),
    ("puffer", "puffer"),
    ("pullover", "pullover"),
    ("raincoat", "raincoat"),
    ("set", "set"),
    ("shirt", "shirt"),
    ("shirts", "shirts"),
    ("short", "short"),
    ("shorts", "shorts"),
    ("skirt", "skirt"),
    ("skirts", "skirts"),
    ("skort", "skort"),
    ("stole", "stole"),
    ("suit", "suit"),
    ("suits-blazers", "suits-blazers"),
    ("sweater", "sweater"),
    ("sweaters", "sweaters"),
    ("sweatershirt", "sweatershirt"),
    ("sweatpants", "sweatpants"),
    ("sweatshirt", "sweatshirt"),
    ("tights", "tights"),
    ("top", "top"),
    ("tops", "tops"),
    ("trenchcoat", "trenchcoat"),
    ("trouser", "trouser"),
    ("trousers", "trousers"),
    ("tunic", "tunic"),
    ("turtleneck", "turtleneck"),
    ("vest", "vest"),
    ("waistcoat", "waistcoat"),
)


# class MyGender(forms.Form):
#     gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER)


class FilterForm(forms.Form):
    gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER)
    category = forms.ChoiceField(widget=forms.Select(), choices=CATEGORY)


class UploadForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER)
    class Meta:
        model = UploadFile
        exclude = ()
