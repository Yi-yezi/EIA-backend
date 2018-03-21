# Generated by Django 2.0.2 on 2018-03-19 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=255, null=True, unique=True, verbose_name='公司名称')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('supermanager', '超级管理者'), ('manager', '管理者'), ('worker', '编写员'), ('agency', '中介'), ('firstParty', '甲方'), ('noPosition', '无职')], default='worker', max_length=15, verbose_name='职位')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyMembership', to='company.Company')),
            ],
        ),
    ]
