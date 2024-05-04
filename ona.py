import mitmproxy.http

def request(flow: mitmproxy.http.HTTPFlow):
    if ("hoyoverse.com" in flow.request.pretty_url) or ("mihoyo.com" in flow.request.pretty_url) or ("bhsr.com" in flow.request.pretty_url) or ("starrails.com" in flow.request.pretty_url):
        flow.request.host = "127.0.0.1"
        flow.request.scheme = "http"
        flow.request.port = 21000
