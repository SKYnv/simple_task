from django.db import models
from datetime import timedelta

# Create your models here.


class MyTask(models.Model):
    u"""
    Модель задачи
    """
    STATUSES = (
        (1, 'Started'),
        (2, 'Stopped'),
        (3, 'Paused'),
        (4, 'Unknown')
    )

    id = models.PositiveIntegerField(verbose_name='Task id', null=False,
                                     primary_key=True)
    title = models.CharField(verbose_name='Task\'s title', max_length=64)
    status = models.SmallIntegerField(verbose_name='Task\'s status',
                                      choices=STATUSES)
    created_at = models.DateTimeField(verbose_name='Task created at.')
    time_elapsed = models.DurationField(default=timedelta)
    is_complete = models.BooleanField(verbose_name='Task ended.', default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Task'
        verbose_name_plural = 'Task\'s'

    def __str__(self):
        return self.title

