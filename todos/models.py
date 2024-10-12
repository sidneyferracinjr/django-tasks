from django.db import models

# essa classe 'models.py' possui ligação direta com as entidades do python
# toda classe model para ser reconhecida precisa herdar a model principal


class Todo(models.Model):  # herdando model principal
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True)
