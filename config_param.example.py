def COS_Config_param():
    secret_id = 'SECRET_ID' # 替换为用户的 secretId
    secret_key = 'SECRET_KEY' # 替换为用户的 secretKey
    region = 'REGION' # 替换为用户的 Region
    token = None # 使用临时密钥需要传入 Token，默认为空，可不填
    scheme = 'https' # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
    Bucket = 'BUCKET',

    cos_domain = 'http://domain.com.cn/'
    viewer_domain = 'http://domain.com.cn/'

    return secret_id, secret_key, region, token, scheme, Bucket, cos_domain, viewer_domain