warehouse
=========

A pyqt5 + webview + bridge

My friend is thinking about building a personal cargo management software for himself. I haven't built a desktop app for many years. Hence, I contemplated his proposal seriously, and I found out this solution fits all my needs.

1. no runtime environment required
2. better use HTML to build UI
3. python
4. windows / mac
5. client side database

Then I figured out using QWebkit is a quite good solution. Also QWebkit bridge can easily invoke QObject with javascript in pages.

I chose a lightweight ORM framework named peewee, as well as chose sqlite as the database.

<del>If add a template system to this project, it's completely MVC.</del>
I added angular instead of template system. So all works can be done in one single HTML file. `$scope.qObject = qObject` can easily map QObject to angular controller. (unfortunately `$scope = qObject` doesn't work.)

I just wanna try whether this is a solution to develop desktop app in a web way. But I don't wanna continue developing this project any more. So just leave it here.