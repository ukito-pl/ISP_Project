# ISP_Project
Goal of this project is to display and control position of servomechanism using REST API. <br />
Arduino posts measurments to /pozycja_aktualna and gets requested position from /pozycja_zadana. Both values are stored in json files.<br />
<pre>
+---------+          +---------+                                                                     +---------+
|         |          |         |    POST     +------------------+     +-----------------------+      |         |
|         |          |         | ==========> | /pozycja_aktualna| ==> | pozycja_aktualna.json | ==>  |         |
|         |   TCP    |         |             +------------------+     +-----------------------+      |         |
| Arduino | <======> |   PC    |                                                                     | Web UI  |
|         |          |         |     GET     +------------------+     +-----------------------+      |         |
|         |          |         | <========== | /pozycja_zadana  | <== | Pozycja_zadana.json   | <==  |         |
|         |          |         |             +------------------+     +-----------------------+      |         | 
+---------+          +---------+                                                                     +---------+
</pre>
## Set up
First, run rest_server.py and tcp_server.py, install packages as needed. You may need to copy folders from flask_googlecharts folder to location of the package.
Then connect arduino to power and network.
<br />
**Make sure that all ip addresses are correct**
<br />
Chart will be displayed at http://127.0.0.1:5000/
