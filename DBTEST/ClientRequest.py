#### create request to rds
#houge
#
import urllib.request as urllib2
import hashlib
class ClientRequest:
    '''响应http客户端请求,并返回结果json/xml对象'''
    def __init__(self,request=None,sheme='http',port=8000,domain='localhost',prefix='',signaturemethod='md5',signatureversion='v1.0',signaturenonce=''):
        self.sheme=sheme
        self.port=port
        self.domain=domain
        self.prefix=prefix
        self.request=request
        self.signaturemethod=signaturemethod
        self.signatureversion=signatureversion
        self.signaturenonce=signaturenonce
    def do_action(self):
        self.url=self.Get()
        signature=self.Signature(self.url)
        self.url=self.url+'&signature={}&signaturemethod={}&signatureversion={}&signaturenonce={}'.format(signature,self.signaturemethod,self.signatureversion,self.signaturenonce)
        # response=urllib2.urlopen(self.url)
        # return response.read()
        return self.url
    def Get(self):
        for k,v in getattr(self.request,self.request.__dict__['method']).items():
            self.url = self.url + '&{}={}'.format(k, v)
        self.url='{}://{}:{}/{}'.format(self.sheme,self.domain,self.port,self.url)
        return self.url
    def Signature(self,str):
        if isinstance(str,str):
            if self.signaturemethod in ['md5', 'sha1','sha224','sha256','sha384','sha512']:
                m=getattr(hashlib,self.signaturemethod)()
                m.update(str.encode('utf8'))
                return m.hexdigext()
            else:
                raise Exception('hashmethod is unvalid')
        else:
            raise Exception('type must be String ,but {} is not'.format(str))
