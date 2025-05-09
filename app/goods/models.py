from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="name")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="name")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="description")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name='image')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="price")
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="discount in %")
    quantity = models.PositiveBigIntegerField(default=0, verbose_name="quantity")
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Quantity - {self.quantity}'
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        
        return self.price
