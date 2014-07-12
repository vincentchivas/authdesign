from provisionadmin.utils.json import json_response_error, json_response_ok
from provisionadmin.utils.respcode import DATA_ERROR
from django.http import HttpResponse, HttpResponseNotFound
from django.core.servers.basehttp import FileWrapper
from provisionadmin.service.utils.common_op import upload_apk, download_apk, build_apk


def upload(request):
    post = request.POST
    print 'into upload'

    if request.FILES:
        print 'got upload file'
        for file_name in request.FILES.keys():
            file_obj = request.FILES[file_name]
            file_data = file_obj.read()
            print 'upload xml file %s' % file_name
            upload_apk(file_data)
    else:
        print 'not found upload FILES!'

    return json_response_ok({})



def download(request):
    post = request.POST
    print 'into download'

    apk_data = download_apk()

    if apk_data:
        response = HttpResponse(apk_data, mimetype='application/vnd.android.package-archive')
        response['Content-Type'] = 'application/vnd.android.package-archive'
        response['Content-Disposition'] = 'attachment; filename=dolphin.apk' 

        return response

    else:
        return HttpResponseNotFound('<h1>Not Found Apk</h1>')


def build(request):
    post = request.POST
    print 'into build'

    ret = build_apk()

    if ret:
        return json_response_ok({})
    else:
        return json_response_error(DATA_ERROR, 'apk')
        

