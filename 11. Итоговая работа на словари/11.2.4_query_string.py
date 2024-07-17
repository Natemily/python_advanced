def build_query_string(dict):
    res = [f"{k}={v}" for k,v in dict.items()]
    res = sorted(res)
    return "&".join(res)