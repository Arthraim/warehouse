warehouse
=========

A pyqt5 + webview + bridge

My friend is thinking about build a own cargo management software for himself. I haven't build a desktop app for many years. So I really think about his proposal deeply, and I found this solution fits all my needs.

1. no runtime environment required
2. better use HTML to build UI
3. python
4. windows / mac
5. client side database

Then I found use QWebkit is quite a good solution. Also QWebkit bridge can easily invoke QObject with javascript on page.

I chose a lightweight ORM framework peewee, chose sqlite as the database.

If add a template system to this project, it's completely MVC.

I just wanna try if this is a solution to develop desktop app in a web way. But I don't wanna continue this project any more. So put it here.
