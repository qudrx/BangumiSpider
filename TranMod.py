from baidu.fanyi.fanyi_helper import BaiduFanyiHelper
from baidu.fanyi.fanyi_http import FanyiHttp


class FanyiSpider:
    token = "98945f0628cf2a4b552845b3417270cd"

    @classmethod
    def base_translate(cls, data: str, from_: str = 'jp', to: str = 'zh') -> str:
        """
        基础翻译
        :param data: 需要翻译的单词或句子
        :param from_: 从什么语言翻译
        :param to: 翻译到什么语言
        :return: 翻译的结果
        """
        url = "https://fanyi.baidu.com/basetrans"
        data = {
            'query': data,
            'from': from_,
            'to': to,
            'token': cls.token,
            'sign': BaiduFanyiHelper.get_sign(data)
        }
        res = FanyiHttp().post(url=url, data=data).json()
        return BaiduFanyiHelper.detail_base_translate_result(res)

    @classmethod
    def paragraph_translate(cls, data: str, from_: str = 'jp', to: str = 'zh') -> list:
        """
        段落翻译
        :param data: 需要翻译的文章
        :param from_: 从什么语言翻译
        :param to: 翻译到什么语言
        :return: 翻译的结果
        """
        url = "https://fanyi.baidu.com/v2transapi"
        data = {
            'query': data,
            'from': from_,
            'to': to,
            'token': cls.token,
            'sign': BaiduFanyiHelper.get_sign(data),
            'transtype': 'translang',
            'simple_means_flag': 3
        }
        res = FanyiHttp().post(url=url, data=data).json()
        return BaiduFanyiHelper.detail_paragraph_translate_result(res)


if __name__ == '__main__':
    cls = FanyiSpider()
    s = '藤宮周（あまね）の住むマンションの隣には、学校でも一番の人気を誇る愛らしい天使が居る。'
    # print(cls.base_translate(s, from_='jp', to='zh'))
    print(cls.paragraph_translate(s, from_='jp', to='zh'))