class Cleaner:

    @staticmethod
    def replace( fs ):
        ''' logstash doesn't like '.' in the field name. so let's transform it '''
        fs_buf = fs[:]
        cleaned = []
        for idx in range(1,len(fs_buf)):
            if '.' in fs_buf[idx]:
                cleaned.append(idx) 
                fs_buf[idx] = fs_buf[idx].replace('.','_')
        
        fs_before = ''
        fs_after = ''
        if len(cleaned) > 0 : 
            for idx in cleaned: 
                fs_before = "%s %s" % (fs_before, fs[idx])
                fs_after  = "%s %s" % (fs_after, fs_buf[idx])
            print "====================================================="
            print "WARNING:\tThose fields name have been rewritten to avoid '.' "
            print "from:\t\t%s" % fs_before
            print "to:\t\t%s" %   fs_after
            print "====================================================="
            print 
        return fs_buf
