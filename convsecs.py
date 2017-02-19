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
