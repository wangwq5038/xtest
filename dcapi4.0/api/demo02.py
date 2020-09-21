from mitmproxy import http



def request(flow:http.HTTPFlow):
    if "baidu.com" in flow.request.pretty_url:
    # if flow.request.pretty_url == "http://example.com/path":
        flow.response = http.HTTPResponse.make(
            200,
            b"Hello World",
            {"Content-Type":"text/html"}
        )




def request(flow:http.HTTPFlow):
    if "admin/login" in flow.request.pretty_url:
    # if flow.request.pretty_url == "http://example.com/path":
        with open("./tmp.json", encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,
                f.read(),
                {"Content-Type":"text/html"}
            )



# import _json
#
# def response(flow:http.HTTPFlow):
#     if "quote.json" in flow.request.pretty_url:
#         data = _json.loads(flow.response.content)
#         data['data']['items'][0]['quote']['name'] = "asda1545"
#         flow.response.text = json.dumps(data)