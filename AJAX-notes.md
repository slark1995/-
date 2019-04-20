## AJAX

### AJAX简介
AJAX = Asynchronous JavaScript (and XML)（异步的 JavaScript (和 XML)）。

- AJAX 不是新的编程语言，而是一种使用现有标准的新方法。

- AJAX 就是可以在不重新加载整个页面的情况下，**与服务器交换数据**并更新部分网页内容。

- 传统的网页（不使用 AJAX）如果需要更新内容，必需重载整个网页面。

- AJAX 不需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。

- AJAX DISADVANTAGES (缺点) ：
   - You have to manage History, Back button, Bookmarks in JS
   - Security: browsers heavily restrict AJAX to prevent abuse
      - Same-Origin Policy
   - Even more HTTP requests, CPU and RAM

---

### AJAX实例：

```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
function loadXMLDoc()
{
var xmlhttp;
if (window.XMLHttpRequest)
{
//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
xmlhttp=new XMLHttpRequest();
}
else
{
// IE6, IE5 浏览器执行代码
xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
xmlhttp.onreadystatechange=function()
{
if (xmlhttp.readyState==4 && xmlhttp.status==200)
{
document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
}
}
xmlhttp.open("GET","/try/ajax/ajax_info.txt",true);
xmlhttp.send();
}
</script>
</head>
<body>

<div id="myDiv"><h2>使用 AJAX 修改该文本内容</h2></div>
<button type="button" onclick="loadXMLDoc()">修改内容</button>

</body>
</html>
```

上面一段代码中，当我点击按钮，就调用名为 loadXMLDoc() 的函数，从服务器获取数据，更新并且显示在<myDiv>中

```
<head>
<script>
function loadXMLDoc()
{
.... AJAX 脚本执行 ...
}
</script>
</head>
```
接下里将这个函数中，AJAX具体如何实现的，以及它的工作原理

----

### MAKING REQUESTS
Use JS to make an HTTP request and get the content

Old school: new XMLHttpRequest()
Modern: Fetch API
new Request("some-url");
Promises!
https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

* 做http请求来获取数据，以前的方法是用XMLHttpRequest()，现在用Fetch API 



### AJAX 创建 XMLHttpRequest 对象 
XMLHttpRequest 是 AJAX 的基础。

#### XMLHttpRequest 对象

所有现代浏览器均支持 XMLHttpRequest 对象（IE5 和 IE6 使用 ActiveXObject。

XMLHttpRequest 用于在后台与服务器交换数据。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新

#### 创建 XMLHttpRequest 对象
所有现代浏览器均内建 XMLHttpRequest 对象。
***创建 XMLHttpRequest 对象的语法：***

variable=new XMLHttpRequest();

