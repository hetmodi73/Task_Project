# Generated by Django 4.0 on 2022-03-30 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('client', '0005_remove_master_question_sd_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='master_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUESTION', models.CharField(max_length=50)),
                ('ANSWER', models.CharField(max_length=50)),
                ('POINTS', models.IntegerField()),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_question', to='services.service_details')),
            ],
        ),
        migrations.CreateModel(
            name='sub_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUESTION', models.CharField(max_length=50)),
                ('ANSWER', models.CharField(max_length=50)),
                ('POINTS', models.IntegerField()),
                ('QUESTION_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_question', to='blog.master_question')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_question', to='services.service_details')),
            ],
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOCUMENT_NAME', models.CharField(max_length=20)),
                ('DOCUMENT_FILE', models.FileField(default='', upload_to='profile')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to='client.user')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to='services.service')),
            ],
        ),
    ]
