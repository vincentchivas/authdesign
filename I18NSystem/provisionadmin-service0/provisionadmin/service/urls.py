from django.conf.urls.defaults import patterns, include


urlpatterns = patterns('provisionadmin.service.views',
                       (r'^upload', 'apk.upload'),
                       (r'^download', 'apk.download'),
                       (r'^build', 'apk.build'),
                       )
