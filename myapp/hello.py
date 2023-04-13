import fire

def hello(name="World"):
  return "Hello %s! From Python" % name

if __name__ == '__main__':
  fire.Fire(hello)
