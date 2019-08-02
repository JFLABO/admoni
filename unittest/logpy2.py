# -*- Coding:utf-8 -*-
import apache_log_parser

LOG = '/var/log/apache2/access.log'
DATA = open(LOG, 'r')
#parser = apache_log_parser.make_parser('%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O')
parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
counter=0
for line in DATA:
      log_data = parser(line)
      #print('#' * 50)
      for k,v in log_data.items():
            s=str(v)
            if s.find('jflabo') > -1:
            #if k=="request_header_referer":
                  print(k,v)
                  counter=counter+1

                  
print(counter)
