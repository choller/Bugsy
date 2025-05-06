import bugsy
import os

# Using an API key is the preferred way to authenticate to Bugzilla and as long as your operations
# don't require authentication, this code will work even without an API key.
#
# Using username and password is deprecated, as it is not compatible with two-factor authentication.
bz = bugsy.Bugsy(api_key=os.getenv("BZ_API_KEY"), bugzilla_url="https://bugzilla-dev.allizom.org/rest")

# Create a new bug with a comment 0 set.
bug = bugsy.Bug()
bug.summary = "I love cheese"
bug.add_comment('I do love sausages too')
bz.put(bug)

# Add another comment to that bug.
bug.add_comment('I do love eggs too')

# Add a comment to an existing bug for whom we don't
# have a bug object (and don't wish to fetch it).
bug = bz.get(123456)
bug.add_comment("I love cheese")
