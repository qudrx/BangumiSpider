import execjs


class BaiduFanyiHelper:
    @staticmethod
    def get_sign(keywords: str) -> str:
        with open('baidu/fanyi/fanyi.js') as f:
            ctx = execjs.compile(f.read())
        return ctx.call('a', keywords)

    @staticmethod
    def detail_translate_result(raw: dict) -> str:
        return raw['trans'][0]['dst']

    @staticmethod
    def detail_paragraph_translate_result(raw: dict) -> list:
        return [i['dst'] for i in raw['trans_result']['data']]