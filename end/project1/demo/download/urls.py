from django.conf.urls import url
from django.http import FileResponse
app_name="download"

def load(request,filename):
   return FileResponse(open(filename+".txt", "rb"), content_type="application/msword", filename=filename+".txt",
                 as_attachment=True)


urlpatterns=[

    url(r'^(\w+)/$',load)
]