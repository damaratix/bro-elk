Just an idea on how to insert [Bro Security Monitor](https://www.bro.org/ "The Bro Network Security Monitor") logs files into [Elastisearch](https://www.elastic.co/products/elasticsearch) using [Logstash](https://www.elastic.co/products/logstash)  having some maintainable configuration files (and do not get crazy with a bunch of (?<ts>(.*?))\t?<uid>(.*?))\t.... :) )


There are three main directory:
- templates
- logstash
- brolog2grok


**templates:**
contains  the files logstash uses as templates  while  loading  different
files into Elasticsearch, you require them in order to customize the data
structure stored in  elastic.


**logstash:**
contains the files logstash uses as configuration file while loading
data into elastic.
Here you define the rules for the grok parser.


**brolog2grok:**
contains  a script that generates the skeleton of the  grok pattern
required  to logstash while parsing  a bro log file.
<br />
Usage:<br />
$ cd brolog2grok<br />
$ sudo python main.py < /opt/bro/logs/current/weird.log
<br />
<br />
<br />
Output: THE GROK PATTERN
<br />
<br />
%{BRO_TS:ts}\s+%{BRO_WORD:uid}\s+%{BRO_IP:id_orig_h}\s+%{BRO_PORT:id_orig_p}\s+%{BRO_IP:id_resp_h}\s+%{BRO_PORT:id_resp_p}\s+%{BRO_WORD:name}\s+%{BRO_WORD:addl}\s+%{BRO_BOOL:notice}\s+%{BRO_WORD:peer}\s+
<br />
<br />
<br />
Warning:
Keep in mind the same data type may need to be verified by hand, that's because
es: WORD and DATA are similar but the latest is more permissive.
The script, as default, choose WORD data type


All BRO-GROK "DATA TYPE" used here, are stored at the beginning of logstash/patterns/bro
