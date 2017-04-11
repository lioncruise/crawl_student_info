# crawl_student_info

1. Using pip to install Scrapy

```
pip install scrapy -U --user
```

2. Verify whether Scrapy has been installed

```
scrapy version
```

If the scrapy command is not found in your path, run `sudo /usr/bin/easy_install scrapy`

3. The demo's mysql user and password is 'root' and 'admin', please modify them using your user and password and set the user authority writable.

4. run the following command to crawl students's information:

```
scrapy runspider download_infos.py
```