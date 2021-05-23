from flask import Flask,render_template
from config_param import COS_Config_param

app = Flask(__name__)

@app.route('/')
@app.route('/<prefix>')
def navigate(prefix=''):
    from qcloud_cos import CosConfig
    from qcloud_cos import CosS3Client
    import sys
    import logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    secret_id, secret_key, region, token, scheme, bucket, cos_domain, viewer_domain = COS_Config_param()
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)

    client = CosS3Client(config)

    response = client.list_objects(
        Bucket=bucket,
        Prefix=prefix
    )

    files_list = []

    for rec in response['Contents']:
        key = rec['Key']
        loc = key.split('/')
        files_list.append(loc)

    current_list = []
    if prefix == '':
        for files in files_list:
            if len(files) == 2:
                if files[1] == '': current_list.append(files[0])
            if len(files) == 1:
                current_list.append(files[0])
    else:
        compat = prefix.split('/')
        deep = len(compat)
        for files in files_list:
            if files[:deep] == compat and files[deep] != '':
                current_list.append(files[deep])
    current_list = list(set(current_list))

    webdir = []
    for dirs in current_list:
        if '.' in dirs:
            webdir.append(cos_domain + prefix + '/' +dirs)
        else:
            webdir.append(viewer_domain + ((prefix + '/') if prefix else '') + dirs)

    return render_template('list.html',abbrlist = list(zip(current_list,webdir)))


if __name__ == '__main__':
    app.run()
