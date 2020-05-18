from django.db import models


# Create your models here.


class PersonalDetails(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DOB = models.DateField()
    Gender = models.enums.Choices("Male", "Female")

    Image = models.ImageField(upload_to="Images", null=True, blank=True, default="No Image Found")
    ContactNo = models.CharField(max_length=10)
    Address = models.TextField()

    def __str__(self):
        return f"{self.LastName}-{self.id}"


class Items(models.Model):
    ItemName = models.CharField(max_length=50)
    ItemPrice = models.FloatField()
    ItemColor = models.CharField(max_length=15)
    ItemCategory = models.CharField(max_length=50)


class OrderDetails(models.Model):
    OrderedItem = models.CharField(max_length=100)
    Customer_id = models.ForeignKey(PersonalDetails, on_delete=models.deletion.CASCADE)
    Item_id1 = models.ForeignKey(Items, on_delete=models.deletion.CASCADE)
    Item_id1 = models.ForeignKey(Items, on_delete=models.deletion.CASCADE, null=True, blank=True)
    Item_id1 = models.ForeignKey(Items, on_delete=models.deletion.CASCADE, null=True, blank=True)
    Item_id1 = models.ForeignKey(Items, on_delete=models.deletion.CASCADE, null=True, blank=True)
    OrderedDate = models.DateTimeField()
    Total_Price = models.FloatField()
    Description = models.TextField()
