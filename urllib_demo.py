'''
urllib is a built-in Python package, so you don't need pip install.

🌐 Python urllib Module

It is used for working with URLs, including:

Opening/fetching URLs
Parsing URLs
Encoding query parameters
Building URLs
Sending HTTP requests (basic use)
'''
'''
import urllib

But normally we use its submodules:

urllib
  ├── urllib.request   → open/fetch URLs
  ├── urllib.parse     → parse/build URLs
  ├── urllib.error     → handle URL errors
  └── urllib.robotparser → robots.txt

'''
#let's start with:   urllib.parse  ---->>>>>step 1:  urlparse




from urllib.parse import urlparse

url = 'https://www.example.com/products?id=10'

result = urlparse(url)

print(result)



'''
What does urlparse() do?

It breaks a URL into its individual components.

For:

https://www.example.com/products?id=10

we have:

https://          → scheme
www.example.com   → domain/netloc
/products         → path
id=10             → query
'''




#step 2 urlencode() ---Suppose you want to create query parameters:

from urllib.parse import urlencode

data = {
    "name": "Bhavna",
    "city": "Indore"    
}

query = urlencode(data)
print(query)



'''
This is useful when constructing URLs such as:

https://example.com/search?name=Bhavna&city=Indore

It also correctly handles characters that need URL encoding.
'''




#Step 3 — urlunparse()  :: You can also construct a URL from components.

from urllib.parse import urlunparse

url = urlunparse((
    'https',
    'www.example.com',
    '/products',
    '',
    'id=90',
    ''
))
print(url)





#step: 04:   urljoin()

#very useful when combining a base URL with another path.


from urllib.parse import urljoin

base = 'https://example.com/products/'

result = urljoin(base, "laptop")

print(result)




from urllib.parse import urlparse

url = 'https://www.example.com/products?id=10'

result = urlparse(url)

print(result.scheme)     #https
print(result.netloc)    #www.example.com
print(result.path)    #/products
print(result.query)    #id=10