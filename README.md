HoneyDoc creates a "honey" document including things like fake names and social security numbers to look appealing to would be attackers. It also includes a 1x1 pixel png file called hello.png as the tracking image so that you can see the IPs of who opens the document in your web server logs. To install the image, place it in your web servers root directory (or any other directory you want to use) and specify your URL using the --url flag when generating the document. 

usage: HoneyDoc.py [-h] [-t TITLE] [-c COUNT] [-u URL] [-e EXT]

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        Specify a custom document title. Default is Employee
                        Information
  -c COUNT, --count COUNT
                        Number of fake records to create. Default is 10
  -u URL, --url URL     URL of image. Default is http://127.0.0.1/hello.png
  -e EXT, --ext EXT     File extension. Default is doc

