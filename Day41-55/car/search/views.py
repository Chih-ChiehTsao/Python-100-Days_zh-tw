from datetime import datetime
from json import JSONEncoder

from django import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect

from search.models import CarRecord

# 序列化/串行化/腌鹹菜 - 把對象按照某種方式處理成字節或者字符的序列
# 反序列化/反串行化 - 把字符或者字節的序列重新還原成對象
# Python實現序列化和反序列化的工具模塊 - json / pickle / shelve
# return HttpResponse(json.dumps(obj), content_type='application/json')
# return JsonResponse(obj, encoder=, safe=False)
# from django.core.serializers import serialize
# return HttpResponse(serialize('json', obj), content_type='application/json; charset=utf-8')
MAX_AGE = 14 * 24 * 60 * 60


class CarRecordEncoder(JSONEncoder):

    def default(self, o):
        del o.__dict__['_state']
        o.__dict__['date'] = o.happen_date
        return o.__dict__


def ajax_search(request):
    current_time = datetime.now().ctime()
    # Cookie是保存在浏覽器臨時文件中的用戶數據(通常是識別用戶身份的ID/token或者是用戶的偏好設置)
    # 因爲每次請求服務器時在HTTP請求的請求頭中都會攜帶本網站的Cookie數據
    # 那麽服務器就可以獲取這些信息來識別用戶身份或者了解用戶的偏好 這就是所謂的用戶跟蹤
    # 因爲HTTP本身是無狀態的 所以需要使用Cookie/隱藏域/URL重寫這樣的技術來實現用戶跟蹤
    # 從請求中讀取指定的cookie - 通過cookie的名字找到對應的值
    # 如果請求中沒有指定名字的cookie可以通過get方法的第二個參數設置一個默認的返回值
    last_visit_time = request.COOKIES.get('last_visit_time')
    if request.method == 'GET':
        response = render(request, 'search2.html',
                          {'last': last_visit_time if last_visit_time
                           else '你是第一次訪問我們的網站'})
        # 通過render渲染頁面後先用set_cookie方法設置cookie後再返回HttpResponse對象
        # 第一個參數是cookie的名字 第二個參數是cookie的值 第三個參數是過期時間(秒)
        response.set_cookie('last_visit_time', current_time, max_age=MAX_AGE)
        return response
    else:
        carno = request.POST['carno']
        record_list = list(CarRecord.objects.filter(carno__icontains=carno))
        # 第一個參數是要轉換成JSON格式(序列化)的對象
        # encoder參數要指定完成自定義對象序列化的編碼器(JSONEncoder的子類型)
        # safe參數的值如果爲True那麽傳入的第一個參數只能是字典
        # return HttpResponse(json.dumps(record_list), content_type='application/json; charset=utf-8')
        return JsonResponse(record_list, encoder=CarRecordEncoder,
                            safe=False)


def search(request):
    # 請求行中的請求命令
    # print(request.method)
    # 請求行中的路徑
    # print(request.path)
    # 請求頭(以HTTP_打頭的鍵是HTTP請求的請求頭)
    # print(request.META)
    # 查詢參數: http://host/path/resource?a=b&c=d
    # print(request.GET)
    # 表單參數
    # print(request.POST)
    if request.method == 'GET':
        ctx = {'show_result': False}
    else:
        carno = request.POST['carno']
        ctx = {
            'show_result': True,
            'record_list': list(CarRecord.objects.filter(carno__contains=carno))}
    return render(request, 'search.html', ctx)


class CarRecordForm(forms.ModelForm):
    carno = forms.CharField(min_length=7, max_length=7, label='車牌號', error_messages={'carno': '請輸入有效的車牌號'})
    reason = forms.CharField(max_length=50, label='違章原因')
    punish = forms.CharField(max_length=50, required=False, label='處罰方式')

    """
    # 執行額外的表單數據驗證
    def clean_carno(self):
        _carno = self.cleaned_data['carno']
        if not condition:
            raise forms.ValidationError('...')
        return _carno
    """

    class Meta:
        model = CarRecord
        fields = ('carno', 'reason', 'punish')


def add(request):
    if request.method == 'GET':
        f = CarRecordForm(initial={'reason': '打警察', 'punish': '牢底坐穿'})
    else:
        f = CarRecordForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/search2')
    return render(request, 'add.html', {'f': f})
