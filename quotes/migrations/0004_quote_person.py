# Generated by Django 2.2.7 on 2019-11-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20191113_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='person',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to='quotes.Person'),
            preserve_default=False,
        ),
    ]
