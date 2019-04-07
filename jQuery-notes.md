## jQuery 语法
通过 jQuery，您可以选取（查询，query） HTML 元素，并对它们执行"操作"（actions）。
***

### jQuery 语法
jQuery 语法是通过选取 HTML 元素，并对选取的元素执行某些操作。

基础语法： **$(selector).action()**

- 美元符号定义 jQuery
- 选择符（selector）"查询"和"查找" HTML 元素
- jQuery 的 action() 执行对元素的操作


实例:

- $(this).hide() - 隐藏当前元素

- $("p").hide() - 隐藏所有 <p> 元素

- $("p.test").hide() - 隐藏所有 class="test" 的 <p> 元素

- $("#test").hide() - 隐藏所有 id="test" 的元素


### 文档就绪事件
你也许已经注意到在我们的实例中的所有 jQuery 函数位于一个 document ready 函数中：
```javascript
$(document).ready(function(){

    // 开始写 jQuery 代码...

});
```
这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码，即在 DOM 加载完成后才可以对 DOM 进行操作。

如果在文档没有完全加载之前就运行函数，操作可能失败。下面是两个具体的例子：

- 试图隐藏一个不存在的元素
- 获得未完全加载的图像的大小

**提示**：简洁写法（与以上写法效果相同）:
```javascript
$(function(){

// 开始写 jQuery 代码...

});
```
以上两种方式你可以选择你喜欢的方式实现文档就绪后执行 jQuery 方法。


***



<br>
<br>


## jQuery 选择器
jQuery 选择器允许您对 HTML 元素组或单个元素进行操作。
***

### jQuery 选择器
jQuery 选择器允许您对 HTML 元素组或单个元素进行操作。

jQuery 选择器基于元素的 id、类、类型、属性、属性值等"查找"（或选择）HTML 元素。 它基于已经存在的 CSS 选择器，除此之外，它还有一些自定义的选择器。

jQuery 中所有选择器都以美元符号开头：$()。


### 元素选择器
jQuery 元素选择器基于元素名选取元素。

在页面中选取所有 <p> 元素:
$("p")

实例:
用户点击按钮后，所有 <p> 元素都隐藏：
```javascript
$(document).ready(function(){
    $("button").click(function(){
        $("p").hide();
    });
});
```

### #id 选择器
jQuery #id 选择器通过 HTML 元素的 id 属性选取指定的元素。

页面中元素的 id 应该是唯一的，所以您要在页面中选取唯一的元素需要通过 #id 选择器。

通过 id 选取元素语法如下：
$("#test")

实例:
当用户点击按钮后，有 id="test" 属性的元素将被隐藏：
```javascript
$(document).ready(function(){
    $("button").click(function(){
        $("#test").hide();
    });
});
```

.class 选择器
jQuery 类选择器可以通过指定的 class 查找元素。
语法如下：
$(".test")

实例
用户点击按钮后所有带有 class="test" 属性的元素都隐藏：
```javascript
$(document).ready(function(){
    $("button").click(function(){
        $(".test").hide();
    });
});
```

更多实例


语法  |  描述
---|---
$("*")|选取所有元素
$(this)|选取当前HTML元素
$("p.intro")| 选取class 为 intro 的 <p> 元素
$("p:first")|选取第一个 <p> 元素
$("ul li:first")|选取第一个 <ul> 元素的第一个 《li》 元素
$("ul li:first-child")  | 选取每个 <ul> 元素的第一个 《li》 元素
$("[href]") | 选取带有 href 属性的元素
$(":button")  |  选取所有 type="button" 的 <input> 元素 和 <button> 元素
$("tr:even")  |  选取偶数位置的 《tr》 元素



### 独立文件中使用 jQuery 函数
如果您的网站包含许多页面，并且您希望您的 jQuery 函数易于维护，那么请把您的 jQuery 函数放到独立的 .js 文件中。

当我们在教程中演示 jQuery 时，会将函数直接添加到 <head> 部分中。不过，把它们放到一个单独的文件中会更好，就像这样（通过 src 属性来引用文件）：
实例:
```javascript
<head>
<script src="http://cdn.static.runoob.com/libs/jquery/1.10.2/jquery.min.js">
</script>
<script src="my_jquery_functions.js"></script>
</head>
```
***


<br>
<br>

## jQuery 事件
jQuery 是为事件处理特别设计的。
***

**什么是事件?**
页面对不同访问者的响应叫做事件。

事件处理程序指的是当 HTML 中发生某些事件时所调用的方法。

实例：
 - 在元素上移动鼠标。
 - 选取单选按钮
  - 点击元素

在事件中经常使用术语"触发"（或"激发"）例如： "当您按下按键时触发 keypress 事件"。

常见 DOM 事件：

鼠标事件  |  键盘事件 |  表单事件  |  文档/窗口事件
---|---|---|---
click  |  keypress  |  submit  |  load
dblclick  |  keydown  |  change  |  resize
mouseenter  |  keyup  |  focus  |  scroll
mouseleave  |  hover  |  blur  |  unload（已废除）


### jQuery 事件方法语法

在 jQuery 中，大多数 DOM 事件都有一个等效的 jQuery 方法。

页面中指定一个点击事件：
