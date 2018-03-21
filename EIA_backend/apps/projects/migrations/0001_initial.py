# Generated by Django 2.0.2 on 2018-03-19 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=255, null=True, unique=True, verbose_name='项目名称')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('projectType', models.CharField(blank=True, max_length=10, null=True, verbose_name='项目性质')),
                ('constructionCompanyName', models.CharField(max_length=255, null=True, verbose_name='建设单位名称')),
                ('nameAbbreviation', models.CharField(max_length=255, null=True, verbose_name='名称缩写')),
                ('NEIType', models.CharField(max_length=255, null=True, verbose_name='国民经济行业类别及代码')),
                ('environmentalEffectclassification', models.CharField(max_length=255, null=True, verbose_name='环境影响评价行业类别')),
                ('EAcompanyName', models.CharField(max_length=255, null=True, verbose_name='环评公司名称')),
                ('EAcompanyCertificatenumber', models.CharField(max_length=255, null=True, verbose_name='环评单位证书编号')),
                ('EAcompanyTelephone', models.CharField(max_length=255, null=True, verbose_name='环评单位联系电话')),
                ('EAcompanyAddress', models.CharField(max_length=255, null=True, verbose_name='环评单位联系地址')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='项目地址')),
                ('postalCode', models.CharField(max_length=6, null=True, verbose_name='邮政编码')),
                ('corporateName', models.CharField(max_length=10, null=True, verbose_name='法人代表姓名')),
                ('corporateId', models.CharField(max_length=18, null=True, verbose_name='法人身份证')),
                ('constructionScale', models.CharField(max_length=50, null=True, verbose_name='项目规模')),
                ('societyCreditcode', models.CharField(max_length=20, null=True, verbose_name='统一社会信用代码')),
                ('businessRange', models.CharField(max_length=20, null=True, verbose_name='营业执照经营范围')),
                ('contacts', models.CharField(max_length=10, null=True, verbose_name='联系人')),
                ('telephone', models.CharField(max_length=20, null=True, verbose_name='联系电话')),
                ('totalInvestment', models.FloatField(null=True, verbose_name='项目总投资（万元）')),
                ('environmentalProtectionInvestment', models.FloatField(null=True, verbose_name='环保投资（万元）')),
                ('floorSpace', models.FloatField(null=True, verbose_name='占地面积（m2)')),
                ('managementSpace', models.FloatField(null=True, verbose_name='经营面积(m2)')),
                ('nonAccommodationNum', models.IntegerField(null=True, verbose_name='职工非住宿人数')),
                ('accommodationNum', models.IntegerField(null=True, verbose_name='职工住宿人数')),
                ('dinningNum', models.IntegerField(null=True, verbose_name='员工吃饭人数（人）')),
                ('dayWorkTime', models.FloatField(null=True, verbose_name='日工作时间')),
                ('yearWorkTime', models.FloatField(null=True, verbose_name='年工作时间')),
                ('investmentTime', models.CharField(max_length=50, null=True, verbose_name='投产时间(年)')),
                ('annualPowerConsumption', models.FloatField(null=True, verbose_name='电年耗量(万kwh/a)')),
                ('east', models.CharField(max_length=50, null=True, verbose_name='东 ')),
                ('south', models.CharField(max_length=50, null=True, verbose_name='南')),
                ('west', models.CharField(max_length=50, null=True, verbose_name='西')),
                ('north', models.CharField(max_length=50, null=True, verbose_name='北')),
                ('longtitude', models.FloatField(null=True, verbose_name='经度')),
                ('latitude', models.FloatField(null=True, verbose_name='纬度')),
                ('township', models.CharField(max_length=50, null=True, verbose_name='所在区镇')),
                ('specialOptionForSewageTreatmentWorks', models.CharField(max_length=50, null=True, verbose_name='污水处理厂特别选项')),
                ('pollutantHoldingWaterBody', models.CharField(max_length=50, null=True, verbose_name='纳污水体')),
                ('surfaceWaterQualityStandard', models.CharField(max_length=50, null=True, verbose_name='地表水质量标准')),
                ('surfaceWaterFunction', models.CharField(max_length=50, null=True, verbose_name='地表水功能')),
                ('soundEnvironmentStandard', models.CharField(max_length=50, null=True, verbose_name='声环境质量标准')),
                ('groundwaterArea', models.CharField(max_length=50, null=True, verbose_name='地下水区域')),
                ('groundwaterType', models.CharField(max_length=50, null=True, verbose_name='地下水类型')),
                ('groundwaterQualityStandard', models.CharField(max_length=50, null=True, verbose_name='地下水质量标准')),
                ('groundwaterBodyNumber', models.CharField(max_length=50, null=True, verbose_name='地下水水体编号')),
                ('besideWaterTreatmentPlant', models.CharField(max_length=5, null=True, verbose_name='是否污水处理厂纳污范围')),
                ('domesticSewageGo', models.CharField(max_length=5, null=True, verbose_name='生活污水去向')),
                ('domesticSewageEnvironmentImpactAnalysis', models.CharField(max_length=5, null=True, verbose_name='生活污水环境影响分析')),
                ('domesticSewageEmissionStandards', models.CharField(max_length=5, null=True, verbose_name='生活污水环境影响分析')),
                ('environmentalProtectionInvestmentProportion', models.FloatField(null=True, verbose_name='生活污水排放标准')),
                ('sensitivePointDistance', models.CharField(max_length=5, null=True, verbose_name='敏感点距离')),
                ('waterSourceDistance', models.CharField(max_length=5, null=True, verbose_name='水源保护地距离')),
                ('product', models.TextField(null=True, verbose_name='产品')),
                ('material', models.TextField(null=True, verbose_name='材料')),
                ('equipment', models.TextField(null=True, verbose_name='设备')),
                ('energyUse', models.CharField(max_length=255, null=True, verbose_name='能源使用情况')),
                ('noiseEquipment', models.CharField(max_length=50, null=True, verbose_name='噪声污染源设备')),
                ('noiseMonitoringPoints', models.IntegerField(null=True, verbose_name='噪声监测点数目')),
                ('annualSolidWasteOutput', models.FloatField(null=True, verbose_name='包装袋年产量(t/a)')),
                ('projectState', models.CharField(blank=True, max_length=10, null=True, verbose_name='项目状态')),
                ('intermediarySourcesCompleted', models.CharField(blank=True, max_length=5, null=True, verbose_name='')),
                ('intermediaryRemark', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('writerRemark', models.CharField(blank=True, max_length=255, null=True, verbose_name='')),
                ('multi_project', models.IntegerField(blank=True, null=True, verbose_name='')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_project', to='company.Company')),
            ],
        ),
    ]