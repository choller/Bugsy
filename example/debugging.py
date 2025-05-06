import bugsy
import os

# Using an API key is the preferred way to authenticate to Bugzilla and as long as your operations
# don't require authentication, this code will work even without an API key.
#
# Using username and password is deprecated, as it is not compatible with two-factor authentication.
bz = bugsy.Bugsy(api_key=os.getenv("BZ_API_KEY"), bugzilla_url="https://bugzilla-dev.allizom.org/rest")

# The following code can greatly help to debug issues with the REST API as you will be able to see
# the raw data that is being sent and received to and from the server.
import logging
import contextlib
from http.client import HTTPConnection

HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
# End of debug code

# The actual code follows
bug = bugsy.Bug()
bug.type = "enhancement"
bug.summary = "I love debugging"
bz.put(bug)
