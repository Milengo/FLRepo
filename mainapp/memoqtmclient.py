from suds.client import Client
import codecs
import base64


class MemoqTMClient():

    """"provides functionality from MemoqServer WS API """

    def __init__(self, server_url):
        """expects url in form 'http://www.memoq.com'"""

        self.server_url = "".join(
            [server_url,
            ':8080/memoqservices/tm?singleWsdl'])
        self.tm_service = Client(url=self.server_url)

    def get_tm_list(self, source="", target=""):
        """returns list of translation memories, can be filtered"""

        return self.tm_service.service.ListTMs(source, target)[0]

    def import_tmx(self, tmguid, filename):
        raise NotImplemented()

    def export_tmx(self, tmguid, filename):
        session_id = self.tm_service.service.BeginChunkedTMXExport(tmguid)

        fileh = codecs.open(filename, 'w', encoding='UTF16')
        while 1:
            chunk = self.tm_service.service.GetNextTMXChunk(session_id)
            if chunk is None:
                break

            as_str = str(base64.b64decode(chunk), encoding='utf-16')

            fileh.write(as_str)
        self.tm_service.service.EndChunkedTMXExport(self.session_id)

    def create(self, params):
        raise NotImplemented
