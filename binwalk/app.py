from flask import Flask, request
import subprocess
import os

'''
curl binwalk:8100/?fn={{filenale ex. DIR822B1_FW202KRb07_k4n9.bin}}
The result will be shown like this

.
.
Scan Time:     2020-12-05 11:05:26
Target File:   /root/firmwares/DIR822B1_FW202KRb07_k4n9.bin
MD5 Checksum:  bcc02bd7f5d9c874a95407d43d04438a
Signatures:    410
.
.

And Create extracted firmware to 
"/root/firmwares/_{{filename}}.extracted"(in binwalk Docker) == "/home/app/web/mediafiles/{{filename}}"(in web Docker)

example. _DIR822B1_FW202KRb07_k4n9.bin.extracted

'''
file_dir = "/root/firmwares/"


app = Flask(__name__)

@app.route("/",methods=['GET'])
def extract():
    filename = request.args.get('fn')
    if((";" in filename) or ("&" in filename) or ("../" in filename)):
        return ""
    os.chdir(file_dir)
    return subprocess.check_output(['binwalk', '-Mre', file_dir+filename])

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=8100)
