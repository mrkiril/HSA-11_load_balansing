## Projector HW 11 - Load balansing

### Upstream - random
>Riga: 3312
>
>Berlin: 3351
>
>London: 3337

### Upstream - least_conn
>Riga: 3334
>
>Berlin: 3328
>
>London: 3338


### Upstream - least_conn (with weight)
```
server projector_nginx_node_berlin:80 weight=2;
server projector_nginx_node_london:80 weight=5;
server projector_nginx_node_riga:80   weight=5;
```
>Riga: 4166
>
>Berlin: 1667
>
>London: 4167


But when we apply cache after first 500 request we can see result like this
```
server projector_nginx_node_berlin:80 weight=1;
server projector_nginx_node_london:80 weight=1;
server projector_nginx_node_riga:80   weight=1;
```
>Riga: 166
>
>Berlin: 167
>
>London: 9667

This means before 501 request we have uniform distribution. 
After it, London request was added to cache, 
and all next responses has cookies `X-Node: London`.