### Center Web Service REST API
- #### server
    - /server [GET]
    Get all Software Servers
    - /server/\<sid> [GET]
    Get server by id
    - /server [POST]
    Register a new Server
    - /server/\<sid> [DELETE]
    Delete server by id
- #### data
    - /realtime/\<sid> [GET]
    Get realtime situation of a server by sid
    - /history/\<sid> [GET]
    Get history data of a module (current only matlab) by module name
- #### status
    - /start
    - /shutdown
    - /restart
### Data module
- #### Server
    - domain
    - web_port
    - software

### Distributed Web Service REST API
- #### server
    - /server [POST]
    Init Server Info
- #### data
    - /realtime/\<sid> [GET]
    Get realtime situation of a server by sid
    - /history/\<sid> [GET]
    Get history data of a module (current only matlab) by module name
- #### status
    - /start
    - /shutdown
    - /restart
### Data module
- #### Server
    - domain
    - flex_port
    - software
    - lmstat_lic
    - lmgrd_lic
- #### History
    - server_id
    - software
    - module
    - date
    - time
    - total
    - use
    - metadata
    - user_data
