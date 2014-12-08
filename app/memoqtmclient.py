from suds.client import Client
import app.config
import codecs
import base64

class MemoqTMClient():
    """"provides functionality from MemoqServer WS API """


    def __init__(self, server_url):
        """expects url in form 'http://www.memoq.com'"""
        
        self.server_url = "".join([server_url,':8080/memoqservices/tm?singleWsdl'])
        self.tm_service = Client(url=self.server_url)

    def get_tm_list(self, source="", target="" ):
        """returns list of translation memories, can be filtered"""
        
        return self.tm_service.service.ListTMs(source,target)[0]
    
    def import_tmx(self, tmguid, filename):
        raise NotImplemented()
    
    def export_tmx(self, tmguid, filename):
        self.session_id = self.tm_service.service.BeginChunkedTMXExport(tmguid)

        self.fileh = codecs.open(filename, 'w', encoding='UTF16')
        while 1:
            self.chunk = self.tm_service.service.GetNextTMXChunk(self.session_id)
            if self.chunk == None:
                break
        
            self.as_str = str(base64.b64decode(self.chunk), encoding='utf-16')
        
                  
            self.fileh.write(self.as_str)
        self.tm_service.service.EndChunkedTMXExport(self.session_id)
        
    
    def create(self, params):
        raise NotImplemented

def get_next_chunk(fileh,session_id, tm_service, loop):
    chunk = tm_service.service.GetNextTMXChunk(session_id)
    if chunk:
        fileh.write(chunk)
        loop.call_later(30,functools.partial(get_next_chunk,fileh,session_id,tm_service,loop))
    else:
        fileh.close()
        loop.call_later(2,functools.partial(tm_service.service.EndChunkedTMXExport,session_id))

def download_tm(tm_guid):
    tm_service = Client(url="http://memoq-new.milengo.com:8080/memoqservices/tm?singleWsdl")
    
    session_id = tm_service.service.BeginChunkedTMXExport(tm_guid)
    fileh = codecs.open("6af51589-2c72-4036-bb7c-0bbeed1c96bb.tmx", 'w', encoding='UTF16')
    
    while 1:
        chunk = tm_service.service.GetNextTMXChunk(session_id)
        if chunk == None:
            break
        
        as_str = str(base64.b64decode(chunk), encoding='utf-16')
        print (chunk.__doc__)
                  
        fileh.write(as_str)
    tm_service.service.EndChunkedTMXExport(session_id)

def main():

    #TMClient = MemoqTMClient(config.DevelopmentConfig.MEMOQ_SERVER_URL)
    #print(len(TMClient.get_tm_list("","")))
    download_tm("6af51589-2c72-4036-bb7c-0bbeed1c96bb")

if __name__ == '__main__':
    main()
