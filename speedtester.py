#!/usr/bin/env python2
from pyspeedtest import SpeedTest
from pyspeedtestconfig import credentials, timezone, logfilename
import twitter
import sys
import arrow

if __name__ == '__main__':
    api = twitter.Api(**credentials)
    st = SpeedTest()
    munits = "Mb/s"
    time = arrow.utcnow().to(timezone).format('YYYY/MM/DD HH:mm:ss')
    try:
        upload_speed = st.upload()
        formatted_upload_speed = "{:.02f}".format(upload_speed / 1000000)
        units1 = munits
    except:
        formatted_upload_speed = "ERR"
        units1 = ""
    try:
        download_speed = st.download()
        formatted_download_speed = "{:.02f}".format(download_speed / 1000000)
        units2 = munits
    except:
        formatted_download_speed = "ERR"
        units2 = ""

    status = "%s Upload: %s%s, Download: %s%s" % (time, formatted_upload_speed, units1, formatted_download_speed, units2)
    api.PostUpdate(status)
    with open(logfilename, 'a') as f:
        logline = ",".join(map(str, [arrow.utcnow().timestamp, upload_speed, download_speed]))
        f.write(logline+'\n')
