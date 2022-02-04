def app(amb , start_response):
    arq=open('index.html','rb')
    data = arq.read()
    status = "200 OK"
    headers = [('Content-type',"text/html")]
    start_response(status,headers)
    return [data]