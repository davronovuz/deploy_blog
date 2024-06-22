from django.db import models



class Blog(models.Model):
    title=models.CharField(max_length=250)
    body=models.TextField()
    image=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=17)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

