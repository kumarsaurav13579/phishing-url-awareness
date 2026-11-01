#  test result
Python version used :3.14       |  Operating system: Windows 11    |  Date: 31.10.2026


|#   |   input | Expected result | Actual result  | Pass/fail |
|.. .| ........|..................|................|...........|..............
|1   |   https://www.example.com/login | No listed warning sign |  - No listed warning signs found. This does not prove safety. |  Pass |       
|2   |   http://192.0.2.10/account  |  IP address + HTTP |  uses an IP address instead of a  familiar domain .
 - uses HTTP.  HTTPS alone does not prove trust. |  Pass |
|3   | http://example.com@sample.invalid/login | @ symbol + HTTP | - contains an '@' symbol; inspect carefully.
 - uses HTTP.  HTTPS alone does not prove trust. | pass |
|4   |https://a.b.c.d.e.example.invalid/path | Many hostname segments | - contains many hostname segment/subdomains. |  pass  |
|5   | https://xn--example.invalid/  | Punycode-style hostname  |  - contains a punnycode-style hostname. |  pass |



## Notes
  "Learned how text-based inspection tools check URL components like hostnames and schemes without visiting sites. Surprised to learn that a clean link with zero warnings does not guarantee safety."