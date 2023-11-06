from django.apps import AppConfig
from django.core.signals import request_started,request_finished

class FirstAppConfig(AppConfig):
    name = 'first_app'

    def ready(self):
        request_started.connect(self.started)
        request_finished.connect(self.finished)


    def started(self,sender,**kwargs):
        print("got request")
    def finished(self,sender,**kwargs):
        print("finished request")
