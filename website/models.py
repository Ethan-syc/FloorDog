from django.db import models


# Create your models here.

class Gender(models.Model):
    gender_choices = {
        ('M', 'man'),
        ('W', 'woman'),
    }
    gender = models.CharField(max_length=5, choices=gender_choices, primary_key=True)

    def __str__(self):
        return 'gender is' + self.gender_choices.__str__()


class Type(models.Model):
    type_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return 'type name is' + self.type_name


class Accessory(models.Model):
    accessory_url = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return 'Accessory name is' + self.accessory_url


class Clothes(models.Model):
    item_url = models.CharField(max_length=200, primary_key=True)
    pic_url = models.CharField(max_length=200)
    clothes_name = models.CharField(max_length=100)
    clothes_detail = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return 'item url is' + self.item_url + '\n' + 'clothes name is' + self.clothes_name
