from bs4 import BeautifulSoup

html ='''<html class="zh_CN"><head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width,initial-scale=1"> <meta property="og:type" content="website"> <meta property="og:image:type" content="image/png"> <meta property="og:image:width" content="600"> <meta property="og:image:height" content="600"> <meta name="twitter:card" content="summary_large_image"> <meta name="twitter:image:width" content="600"> <meta property="og:image" content=""> <meta name="twitter:image" content=""> <meta name="keyWords" content=""> <meta name="twitter:title" content="比特币交易平台"> <meta property="og:title" content="比特币交易平台"> <meta name="description" content=""> <meta property="og:description" content=""> <meta name="twitter:description" content=""> <link type="image/x-icon" rel="shortcut icon" href="/"> ' 
      '<title>比特币交易平台-首页</title> ' 
      '<script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script src="/static/js/es5-promise.js"></script> <script src="/fePublicInfo"></script>  <script src="/static/charting_library/charting_library.min.js?202003201111"></script> <script src="/static/js/jstz.js"></script> <script src="/static/js/security.js"></script> <script src="/static/js/echarts.min.js"></script> <!-- <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>'''


soup = BeautifulSoup(html,'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
for s in soup.findAll('meta'):
    print()