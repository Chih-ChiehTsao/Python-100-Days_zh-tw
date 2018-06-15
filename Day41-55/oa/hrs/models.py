from django.db import models

# ORM - 對象關係映射
# 對象模型  <--->   關係模型
# 實體類    <--->   二維表
# 屬性      <--->   列
# 對象      <--->   記錄


class Dept(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='部門編號')
    name = models.CharField(max_length=20, verbose_name='部門名稱')
    location = models.CharField(max_length=10, verbose_name='部門所在地')
    excellent = models.BooleanField(default=0, verbose_name='是否優秀')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_dept'


class Emp(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=10)
    mgr = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    # mgr = models.IntegerField(null=True, blank=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2)
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    dept = models.ForeignKey(Dept, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_emp'
