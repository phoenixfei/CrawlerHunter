import requests
from pyquery import PyQuery as pq


def write2txt(content):
    with open('text.txt', mode='a', encoding='utf8') as f:
        f.write(content)


if __name__ == '__main__':
    # headers = {
    #     ':authority': 'cn.bing.com',
    #     ':method': 'GET',
    #     ':path': '/search?q=voctor%20engine+language:en&count=50',
    #     ':scheme': 'https',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'cache-control': 'max-age=0',
    #     'cookie': 'DUP=Q=4_5Sz7Xgqc2l21BpdrXmpQ2&T=351336674&A=2&IG=430CD023AD8C47CC84982715530C5397; MUID=248FA1EA7F2B6B1417BDAD6B7B2B6874; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=A6E36A4418EB48E985794089064115B8&dmnchg=1; MUIDB=248FA1EA7F2B6B1417BDAD6B7B2B6874; ANON=A=C808A8551E7878B09CD707C1FFFFFFFF&E=15c6&W=1; NAP=V=1.9&E=156c&C=d_pm2UhgXcVKPfwI7iDVf_nmPxTTeJMJCluDjaB6AziXwNTWEXkjwg&W=1; ISSW=1; ENSEARCH=BENVER=1; _EDGE_S=mkt=zh-cn&SID=1276574F7CA763B815805A487D896215; BPF=X=1; ENSEARCHZOSTATUS=STATUS=0; ULC=P=553B|7:3&H=553B|7:3&T=553B|7:3; SRCHUSR=DOB=20181008&T=1550481912000; SRCHHPGUSR=CW=1519&CH=722&DPR=1.25&UTC=480&WTS=63686078712; ipv6=hit=1550485514564&t=4; _FP=hta=off; _SS=SID=1276574F7CA763B815805A487D896215&HV=1550482274&bIm=729729',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    # }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    resp = requests.get("https://cn.bing.com/search?q=vector+engine&ensearch=1", headers=headers)
    # print(resp.text)
    # print(resp.encoding)
    # resp.encoding = "utf8"
    doc = pq(resp.text)
    #
    li_items = doc('div#b_content ol#b_results li.b_algo').items()
    # print(li_items)
    # print(len(list(li_items)))
    for li in li_items:
        # print(li)
        title = li('h2').text()
        write2txt(title + '\n')
        # info = li('div.b_caption p').text()
        # write2txt(info+'\n')
        # url = li('h2 a').eq(0).attr('href')
        # print(url)
