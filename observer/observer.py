class Observer:
    def __init__(self):
        self.observers = []
        self.msg = ""
        
    def notify(self, data):
        for observer in self.observers:
            observer.notify(data)
    
    def register(self, observer):
        self.observers.append(observer)
    
    def unregister(self, observer):
        self.observers.remove(observer)

class SMSNotifier:
    def notify(self, data):
        print(data, 'received..')
        print('send sms')

class EmailNotifier:
    def notify(self, data):
        print(data, 'received..')
        print('send email')        

class PushNotifier:
    def notify(self, data):
        print(data, 'received..')
        print('send push notification')                
        
        
if __name__ == '__main__':
    notifier = Observer()
    
    sms_noti = SMSNotifier()
    email_noti = EmailNotifier()
    push_noti = PushNotifier()
    
    notifier.register(sms_noti)
    notifier.register(email_noti)
    notifier.register(push_noti)
    
    notifier.notify('user activation event')

        