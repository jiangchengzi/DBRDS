#### create request to rds
#houge
#

class ClientRequest:
    '''响应http客户端请求,并返回结果json/xml对象'''
    def __init__(self,url=None):
        pass
class GetUrl:
    ''' 用于各个数据库请求生成对应的url'''
    def __init__(self,request):
        self.url=''
        self.request=request
    def Get(self):
        for k,v in getattr(self.request,self.request.__dict__['method']).items():
            self.url = self.url + '&{}={}'.format(k, v)
        return self.url
class Signature:
    '''对生成的url进行加密处理,生成signature字符串'''
    def __init__(self, signaturemethod,signatureversion,signaturenonce):
        self.signaturemethod=signaturemethod
        self.signatureversion=signatureversion
        self.signaturenonce=signaturenonce