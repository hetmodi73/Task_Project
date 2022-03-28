# Generated by Django 4.0 on 2022-03-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=25)),
                ('EMAIL', models.CharField(max_length=25)),
                ('NUMBER', models.IntegerField()),
                ('MESSAGE', models.TextField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='master_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUESTION', models.CharField(max_length=50)),
                ('ANSWER', models.CharField(max_length=50)),
                ('POINTS', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SERVICE_NAME', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='service_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SERVICE_DETAIL_NAME', models.CharField(max_length=25)),
                ('SERVICE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_detail', to='client.service')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL_ID', models.CharField(max_length=25)),
                ('PHONE_NO', models.IntegerField()),
                ('PASSWORD', models.CharField(max_length=25)),
                ('NAME', models.CharField(max_length=25)),
                ('GENDER', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=25)),
                ('ADDRESS', models.TextField(max_length=25)),
                ('ROLE', models.IntegerField()),
                ('STATUS', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='sub_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUESTION', models.CharField(max_length=50)),
                ('ANSWER', models.CharField(max_length=50)),
                ('POINTS', models.IntegerField()),
                ('QUESTION_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_question', to='client.master_question')),
                ('SD_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_question', to='client.service_detail')),
            ],
        ),
        migrations.AddField(
            model_name='master_question',
            name='SD_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_question', to='client.service_detail'),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RATINGS', models.CharField(max_length=25)),
                ('COMMENT', models.CharField(max_length=25)),
                ('L_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='client.user')),
            ],
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOCUMENT_NAME', models.CharField(max_length=20)),
                ('DOCUMENT_FILE', models.FileField(default='', upload_to='profile')),
                ('L_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to='client.user')),
                ('SERVICE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to='client.service')),
            ],
        ),
    ]