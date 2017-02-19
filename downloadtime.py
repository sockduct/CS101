def convert_seconds(s):
    output = ''
    #
    hours = int(s/3600)
    minutes = int((s % 3600)/60)
    seconds = s % 60
    output += str(hours)
    if hours == 1:
        output += " hour, "
    else:
        output += " hours, "
    output += str(minutes)
    if minutes == 1:
        output += " minute, "
    else:
        output += " minutes, "
    output += str (seconds)
    if seconds == 1:
        output += " second"
    else:
        output += " seconds"
    return output

def download_time(fs,fsu,bw,bwu):
    units = [ 'kb', 2**10, 'kB', 8*2**10, 'Mb', 2**20, 'MB', 8*2**20,
              'Gb', 2**30, 'GB', 8*2**30, 'Tb', 2**40, 'TB', 8*2**40 ]
    if (fsu not in units) or (bwu not in units):
        print "Error:  Invalid unit passed for file size and/or bandwidth."
        return -1
    fsize = fs * units[units.index(fsu) + 1]
    bsize = bw * units[units.index(bwu) + 1]
    result = 1.0 * fsize / bsize
    output = convert_seconds(result)
    return output
    
