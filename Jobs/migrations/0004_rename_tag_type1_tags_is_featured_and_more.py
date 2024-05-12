# Generated by Django 5.0.3 on 2024-05-12 18:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0003_remove_tags_tag_tags_tag_type1_tags_tag_type2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='tag_type1',
            new_name='is_featured',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='tag_type2',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='tag_type3',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='tags',
        ),
        migrations.AddField(
            model_name='tags',
            name='Tagss',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='category_flags',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
    ]
