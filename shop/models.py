from django.db import models

# Create your models here.
class product(models.Model):
	productId=models.AutoField
	productName=models.CharField(max_length=30)
	category=models.CharField(max_length=40,default="")
	subCategory=models.CharField(max_length=40,default="")
	desc=models.CharField(max_length=200)
	pubDate=models.DateField()
	price=models.IntegerField(default=0)
	image=models.ImageField(upload_to="shop/images",default="")

	def __str__(self):
		return self.productName
