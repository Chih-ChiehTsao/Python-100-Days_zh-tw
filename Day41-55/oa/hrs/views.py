from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import ObjectDoesNotExist

from json import dumps

from hrs.models import Dept, Emp


def index(request):
    ctx = {
        'greeting': '你好，世界！'
    }
    return render(request, 'index.html', context=ctx)


def del_dept(request, no='0'):
    try:
        Dept.objects.get(pk=no).delete()
        ctx = {'code': 200}
    except (ObjectDoesNotExist, ValueError):
        ctx = {'code': 404}
    return HttpResponse(
        dumps(ctx), content_type='application/json; charset=utf-8')
    # 重定向 - 給浏覽器一個URL, 讓浏覽器重新請求指定的頁面
    # return redirect(reverse('depts'))
    # return depts(request)


def emps(request, no='0'):
    # no = request.GET['no']
    # dept = Dept.objects.get(no=no)
    # ForeignKey(Dept, on_delete=models.PROTECT, related_name='emps')
    # dept.emps.all()
    # emps_list = dept.emp_set.all()
    # all() / filter() ==> QuerySet
    # QuerySet使用了惰性查詢 - 如果不是非得取到數據那麽不會發出SQL語句
    # 這樣做是爲了節省服務器內存的開銷 - 延遲加載 - 節省空間勢必浪費時間
    emps_list = list(Emp.objects.filter(dept__no=no).select_related('dept'))
    ctx = {'emp_list': emps_list, 'dept_name': emps_list[0].dept.name} \
        if len(emps_list) > 0 else {}
    return render(request, 'emp.html', context=ctx)


def depts(request):
    ctx = {'dept_list': Dept.objects.all()}
    return render(request, 'dept.html', context=ctx)
