#!/usr/bin/env python

import bugsy
import os

# Using an API key is the preferred way to authenticate to Bugzilla and as long as your operations
# don't require authentication, this code will work even without an API key.
#
# Using username and password is deprecated, as it is not compatible with two-factor authentication.
bz = bugsy.Bugsy(api_key=os.getenv("BZ_API_KEY"), bugzilla_url="https://bugzilla-dev.allizom.org/rest")

bugs = bz.search_for\
        .product('Foo')\
        .search()

for bug in bugs:
    print(f"{bug.id} - {bug.summary}")
