import sys
from Cleaner import Cleaner 
from mappa import mappa


def readline(raw_line, buf):
    '''load data in 'fields' and 'types' buffer to be transformed later ... '''
    line = raw_line.strip()

    if  line.startswith('#fields') :
        fields = raw_line.split('\t')
        fields[len(fields) - 1 ] = fields[len(fields) - 1].rstrip()
        fields = Cleaner.replace(fields)
        buf['fields'] = fields

    if  line.startswith('#types') :
        types = raw_line.split('\t')
        types[len(types) - 1 ] = types[len(types) - 1].rstrip()
        buf['types'] = types


if __name__ == "__main__":
    buf = {}
    out = ''
    grok_fmt = "#{%s:%s}\s+"
    
    for raw_line in sys.stdin:
        if  raw_line.startswith('#') :
            readline(raw_line, buf)
        else:
            break

    try:
        for idx  in range(1,len(buf['fields'])):
            out = out +  grok_fmt % (mappa[buf['types'][idx]] , buf['fields'][idx] )     
    except KeyError, e:
        print "Found unknwon datatype to be included into mappa: %s" % e
        print "Abort."
        sys.exit()

    print buf['fields'] 
    print buf['types']
    print 
    print "TRANSFORMED FOR GROK: "
    print out.replace('#','%').rstrip('\s+')
