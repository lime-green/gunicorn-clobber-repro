This is a reproduction of a socket clobber issue under gunicorn.

Under certain conditions:
- A request body of a sufficient size
- A response body of a sufficient size
- Not reading the requst body

The socket seems to get destroyed. What's interesting is the behaviour
is different when behind a reverse-proxy like nginx versus hitting gunicorn directly.
Hitting gunicorn directly seems to terminate the connection, whereas nginx
returns a successful but incomplete HTTP response

To reproduce this run:
```bash
./run.sh
```

You should see an output similar to:
```bash
**********
Direct Gunicorn
**********
Without reading body:
request size  successes      fails     errors
0KB               100          0          0
request size  successes      fails     errors
1KB                96          0          4
request size  successes      fails     errors
2KB               100          0          0
request size  successes      fails     errors
3KB                99          0          1
request size  successes      fails     errors
4KB                98          0          2
request size  successes      fails     errors
5KB                99          0          1
request size  successes      fails     errors
6KB                96          0          4
request size  successes      fails     errors
7KB                99          0          1
request size  successes      fails     errors
8KB                 2          0         98
request size  successes      fails     errors
9KB                 0          0        100
request size  successes      fails     errors
10KB                1          0         99
request size  successes      fails     errors
11KB                0          0        100
request size  successes      fails     errors
12KB                0          0        100
request size  successes      fails     errors
13KB                0          0        100
request size  successes      fails     errors
14KB                1          0         99
request size  successes      fails     errors
15KB                0          0        100
request size  successes      fails     errors
16KB                0          0        100
request size  successes      fails     errors
17KB                0          0        100
request size  successes      fails     errors
18KB                0          0        100
request size  successes      fails     errors
19KB                0          0        100
request size  successes      fails     errors
20KB                0          0        100


With reading body:
request size  successes      fails     errors
20KB              100          0          0


**********
Nginx proxy
**********
Without reading body:
request size  successes      fails     errors
0KB               100          0          0
request size  successes      fails     errors
1KB               100          0          0
request size  successes      fails     errors
2KB               100          0          0
request size  successes      fails     errors
3KB               100          0          0
request size  successes      fails     errors
4KB               100          0          0
request size  successes      fails     errors
5KB               100          0          0
request size  successes      fails     errors
6KB               100          0          0
request size  successes      fails     errors
7KB               100          0          0
request size  successes      fails     errors
8KB                65         35          0
request size  successes      fails     errors
9KB                66         34          0
request size  successes      fails     errors
10KB               73         27          0
request size  successes      fails     errors
11KB               62         38          0
request size  successes      fails     errors
12KB               72         28          0
request size  successes      fails     errors
13KB               69         31          0
request size  successes      fails     errors
14KB               57         43          0
request size  successes      fails     errors
15KB               77         23          0
request size  successes      fails     errors
16KB               57         43          0
request size  successes      fails     errors
17KB               65         35          0
request size  successes      fails     errors
18KB               68         32          0
request size  successes      fails     errors
19KB               34         66          0
request size  successes      fails     errors
20KB               69         31          0


With reading body:
request size  successes      fails     errors
20KB              100          0          0
```
