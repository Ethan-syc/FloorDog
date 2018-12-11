from django import forms
from upload.models import UploadFile
from website.models import *


GENDER = (("M", "men"), ("W", "women"))

CATEGORY = (
    ("All", "All"),
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
    ("corset", "corset"),
    ("crewneck", "crewneck"),
    ("denim", "denim"),
    ("dickie", "dickie"),
    ("dress", "dress"),
    ("genius", "genius"),
    ("harrington", "harrington"),
    ("hoodie", "hoodie"),
    ("jacket", "jacket"),
    ("jean", "jean"),
    ("jumper", "jumper"),
    ("jumpsuit", "jumpsuit"),
    ("kilt", "kilt"),
    ("leggings", "leggings"),
    ("miniskirt", "miniskirt"),
    ("overalls", "overalls"),
    ("overcoat", "overcoat"),
    ("overshirt", "overshirt"),
    ("pant", "pant"),
    ("parka", "parka"),
    ("peacoat", "peacoat"),
    ("polo", "polo"),
    ("poncho", "poncho"),
    ("puffer", "puffer"),
    ("pullover", "pullover"),
    ("raincoat", "raincoat"),
    ("set", "set"),
    ("shirt", "shirt"),
    ("short", "short"),
    ("skirt", "skirt"),
    ("stole", "stole"),
    ("suit", "suit"),
    ("sweater", "sweater"),
    ("sweatpants", "sweatpants"),
    ("sweatshirt", "sweatshirt"),
    ("tights", "tights"),
    ("top", "top"),
    ("trenchcoat", "trenchcoat"),
    ("trouser", "trouser"),
    ("tunic", "tunic"),
    ("turtleneck", "turtleneck"),
    ("vest", "vest"),
    ("waistcoat", "waistcoat"),
)

MATERIAL = (
    ("All", "All"),
    ("cotton", "cotton"),
    ("polyester", "polyester"),
    ("wool", "wool"),
    ("elastane", "elastane"),
    ("polyamide", "polyamide"),
    ("leather", "leather"),
    ("silk", "silk"),
    ("polyurethane", "polyurethane"),
    ("acrylic", "acrylic"),
    ("cashmere", "cashmere"),
    ("cupro", "cupro"),
    ("mohair", "mohair"),
    ("spandex", "spandex"),
    ("acetate", "acetate"),
    ("alpaca", "alpaca"),
    ("rayon", "rayon"),
    ("leather", "leather"),
    ("merino", "merino"),
    ("linen", "linen"),
    ("lamb", "lamb"),
    ("lyocell", "lyocell"),
    ("calfskin", "calfskin"),
    ("modal", "modal"),
    ("lycra", "lycra"),
    ("fiber", "fiber"),
    ("cupra", "cupra"),
    ("angora", "angora"),
    ("triacetate", "triacetate"),
    ("camel", "camel"),
    ("recycled", "recycled"),
    ("pima", "pima"),
    ("modacrylic", "modacrylic"),
    ("lambswool", "lambswool"),
)

DESIGN = (
    ("All", "All"),
    ("Collar", "Collar"),
    ("Long sleeve", "Long sleeve"),
    ("Short sleeve", "Short sleeve"),
    ("Slim-fit", "Slim-fit"),
    ("Relaxed-fit", "Relaxed-fit"),
    ("Skinny-fit", "Skinny-fit"),
    ("Button closure", "Button closure"),
    ("Zip closure", "Zip closure"),
    ("Mid-rise", "Mid-rise"),
    ("logo", "logo"),
    ("Spread collar", "Spread collar"),
    ("Four-pocket", "Four-pocket"),
    ("embroidered", "embroidered"),
    ("Five-pocket", "Five-pocket"),
    ("Three-pocket", "Three-pocket"),
    ("Straight-leg", "Straight-leg"),
    ("lapel collar", "lapel collar"),
    ("stand collar", "stand collar"),

)


class GenderForm(forms.Form):
    gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER)


class FilterForm(forms.Form):
    category = forms.ChoiceField(widget=forms.Select(), choices=CATEGORY)


class MaterialForm(forms.Form):
    material = forms.ChoiceField(widget=forms.Select(), choices=MATERIAL)


class DesignForm(forms.Form):
    design = forms.ChoiceField(widget=forms.Select(), choices=DESIGN)


class UploadForm(forms.ModelForm):
    # gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER)
    class Meta:
        model = UploadFile
        exclude = ()


