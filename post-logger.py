import time

def save_log(filename, chunk):
  f = open('logs/' + filename, 'a')
  f.write(chunk)
  f.close()

class LogPostRequest:
  def request(self, flow):
    if flow.request.method != 'POST':
      return

    filename = str(time.time()) + '_' + flow.request.host
    log = str(flow.request.headers) + '\n' + flow.request.raw_content
    save_log(filename, log)

def start():
  return LogPostRequest()
