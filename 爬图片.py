import requests
# 引入请求模块
url='https://ts1.tc.mm.bing.net/th/id/R-C.71898564bdd1b16591b7e22bc3f0fa6b?rik=W%2fauGfPcPO4v4g&riu=http%3a%2f%2fimg95.699pic.com%2fphoto%2f60078%2f3881.jpg_wh300.jpg&ehk=9aDFhGAZQkjY4TB8v%2fNDF%2bmRZK5%2b80Tayaq3RvWLcTI%3d&risl=&pid=ImgRaw&r=0'
# 将网址装入变量
response =requests.get(url)
#向变量中的网址发送一个请求，get设置对应是这个网址的，返回的数据存在response这个变量中

print(response.content)
# 二进制内容用content
with open('图片.png','wb')as f:
    # with是上下文管理器，无论写入是否失败都会关闭文件，open是打开文件，里面是名字，wb是二进制使用，外面是起一个方便调用的名字
    f.write(response.content)
#     把response里的内容‘写’进f的这个文件里，用content二进制格式，适用视频，音频

