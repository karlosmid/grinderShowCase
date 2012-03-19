# The Grinder 3.7.1
# HTTP script recorded by TCPProxy at Mar 19, 2012 9:16:40 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Language', 'en-us,en;q=0.5'),
    NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:11.0) Gecko/20100101 Firefox/11.0'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers1= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://codeatsix.infinum.hr/'), ]

headers2= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://codeatsix.infinum.hr/'), ]

headers3= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://codeatsix.infinum.hr/'), ]

headers4= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'), ]

url0 = 'http://codeatsix.infinum.hr:80'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET /').wrap(request101)

request102 = HTTPRequest(url=url0, headers=headers1)
request102 = Test(102, 'GET application-c35bf8b70dcd468d7da6ef3f7ffbbfbf.css').wrap(request102)

request103 = HTTPRequest(url=url0, headers=headers2)
request103 = Test(103, 'GET application-8b5601a04076b23a7aeac3b8993f6825.js').wrap(request103)

request104 = HTTPRequest(url=url0, headers=headers2)
request104 = Test(104, 'GET modernizr-6cacb47520d952f832018bc1610e5e0c.js').wrap(request104)

request105 = HTTPRequest(url=url0, headers=headers3)
request105 = Test(105, 'GET banner2-002664d054138b6c5f2ffe64f2e3ce04.png').wrap(request105)

request106 = HTTPRequest(url=url0, headers=headers3)
request106 = Test(106, 'GET gmaps-1e5b6bbecee2b934617b11b1f9820777.png').wrap(request106)

request107 = HTTPRequest(url=url0, headers=headers4)
request107 = Test(107, 'GET favicon.ico').wrap(request107)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET / (requests 101-107)."""
    result = request101.GET('/')

    grinder.sleep(45)
    request102.GET('/assets/application-c35bf8b70dcd468d7da6ef3f7ffbbfbf.css')

    request103.GET('/assets/application-8b5601a04076b23a7aeac3b8993f6825.js')

    request104.GET('/assets/modernizr-6cacb47520d952f832018bc1610e5e0c.js')

    request105.GET('/assets/banner2-002664d054138b6c5f2ffe64f2e3ce04.png')

    grinder.sleep(12)
    request106.GET('/assets/gmaps-1e5b6bbecee2b934617b11b1f9820777.png')

    grinder.sleep(612)
    request107.GET('/favicon.ico')

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET / (requests 101-107)

def instrumentMethod(test, method_name, c=TestRunner):
  """Instrument a method with the given Test."""
  unadorned = getattr(c, method_name)
  import new
  method = new.instancemethod(test.wrap(unadorned), None, c)
  setattr(c, method_name, method)

# Replace each method with an instrumented version.
# You can call the unadorned method using self.page1.__target__().
instrumentMethod(Test(100, 'Page 1'), 'page1')
