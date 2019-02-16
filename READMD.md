# README
## 功能实现
- 实时信息查看
  - 通过 /status 访问，获取所有模块的信息
    - ./lmutil.exe lmstat -a
  - 通过 /status?module={module} 访问，获取某一模块的信息
    - ./lmutil.exe lmstat -f {module}
-  数据保存
   -  MongoDB （暂时）
      -  每隔一小时存储所有模块的数据
      -  由于每个模块的数据都是一个 collection，重复代码较多，暂未全部存储
   -  influxDB （未来可能）
-  踢出某用户
   - 1. 根据 user, user_host, display 踢出
     - 个别用户这三个信息不全，因此采用第二种方法
   - 2. 根据 server_host, port, handle 踢出 

## Question
- 似乎 lmutil.exe 这个东西本质上只是一个具有一定管理权限的客户端
- 实际的服务端在 matlab 自己手上
