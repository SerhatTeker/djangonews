# Generated by Django 3.0.8 on 2020-08-07 19:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('upvotes', models.PositiveIntegerField(default=0, editable=False)),
                ('downvotes', models.PositiveIntegerField(default=0, editable=False)),
                ('points', models.IntegerField(default=0, editable=False)),
                ('num_comments', models.PositiveIntegerField(default=0, editable=False)),
                ('is_ask', models.BooleanField(default=False)),
                ('is_show', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.Item')),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('news.item',),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.Item')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('domain', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
            ],
            bases=('news.item',),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vote', models.SmallIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
