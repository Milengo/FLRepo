from suds.client import Client
import functools
import asyncio
import codecs
import base64

class MemoqTMClient():
    def __init__(self, server_url):
        self.server_url = "".join([server_url,':8080/memoqservices/tm?singleWsdl'])

    def get_tm_list(self, source="", target="" ):
        """returns list of translation memories, can be filtered"""
        self.tm_service = Client(url=self.server_url)
        return self.tm_service.service.ListTMs(source,target)[0]
    def import_tmx(self, tmguid,filename):
        raise NotImplemented()
    def export_tmx(self, tmguid, filename):
        raise NotImplemented()
    def create(self, params):
        raise NotImplemented
def get_tm_list(source="", target=""):
    tm_service = Client(url="http://memoq-new.milengo.com")
    tm_list = tm_service.service.ListTMs(source,target)
    return tm_list[0]
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
    fileh = codecs.open("sample.export.tmx", 'w', encoding='UTF8')
    
    while 1:
        chunk = tm_service.service.GetNextTMXChunk(session_id)
        print (chunk.__doc__)
        if chunk == None:
            break
          
        fileh.write(chunk)
    tm_service.service.EndChunkedTMXExport(session_id)

def main():

    TMClient = MemoqTMClient('http://memoq-new.milengo.com')
    print(len(TMClient.get_tm_list("","")))
    #download_tm("57582ca0-a626-4848-bd26-f667d32bce09")

if __name__ == '__main__':
    main()
