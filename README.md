这个是一个python平台
采用django框架的项目


python文件上传下载程序开发问题和状况

现状
实验楼 试验过了 可以正常部署 显示 上传 下载  linux环境下 无法成功安装sqlite3
windows环境下可以使用sqlite3但是试验楼的db.sqlite3无法下载下来检验      ok
家里的环境下  可以显示，上传可以(file文件夹里面有上传的文件)但是网页不能显示上传的文件信息 我估计是sqlite3的问题。     ok


解决方案
实验楼的sqlite3数据库下载 然后查看数据库表的内容。 应该内容是正确的，因为网页显示正常。 测试一下如果修改了models文件里面的表结构，       ok
然后重新 makemigrations  migrate会不会正常更新数据库结构
python3 manage.py makemigrations Share   注意 加入installed_apps里面添加的应用程序名字。
python3 manage.py migrate


家里的环境下，应该是sqlite3的连接问题，重点检查一下连接然后做一个连接后的状态输出。    ok
在views.py文件的查询SearchView（View）模块中插入输出 同时查看后台的log日志输出如果数据库连接有问题会停在某一个位置上面       ok
查看是不是连接有问题。


需要修改增加的功能
家里的环境下，改成mysql 连接然后修改程序加入   ok
大文件 上传 下载 5M以上     https://www.tuicool.com/articles/bUnMfu   ok
中文文件名或者文件内容是中文的乱码问题     ok
sqlite3  已经解决乱码问题  ok
点击文件名作为详细信息入口     ok
FileLink 需要真实的ip地址输入     ok
删除功能  加入再次确定对话框   ok
搜索功能 加入模糊搜索    ok
文件上传的时候检测是否有相同文件名文件已经上传，如果有就停止操作，显示提示框    ok
显示上传文件信息功能    ok


django-env-filemanage.ap-northeast-1.elasticbeanstalk.com
eb-FileManage-dev.ap-northeast-1.elasticbeanstalk.com
aa15zybgfzpb0bz.cqnfpkbdck9a.ap-northeast-1.rds.amazonaws.com