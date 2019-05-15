[TOC]

# HTML简单应用

## HTML基本教程

HTML(HyperText Markup Language)，是一种用于创建网页的标准标记语言。

对于中文，需要设置`<meta charset="utf-8"> `

```html
<!DOCTYPE html> 										//声明为 HTML5 文档
<html>															//元素是 HTML 页面的根元素		
<head>															//元素包含了文档的元（meta）数据,如定义网页编码格式为 utf-8。
<meta charset="utf-8">							//
<title>菜鸟教程(runoob.com)</title>	 //元素描述了文档的标题
</head>															//结束
<body>															//	元素包含了可见的页面内容，一个主体
    <h1>我的第一个标题</h1>					 //
    <p>我的第一个段落。</p>						//
</body>															// 结束
</html>															// 结束
```

只有body中的会显示出来。

#### 标签

```html
<标签> 内容 </标签>
```

### 标题

```html
<h1>这是一个标题</h1> //数字代表字号大小
<h2>这是一个标题</h2>
<h3>这是一个标题</h3>
```

### 段落

```html
<p>这是一个段落。</p>
<p>这是另外一个段落。</p>
```

### HTML 链接

```html
<a href="http://www.runoob.com">这是一个链接</a>
```

### HTML 图像

```html
<img src="/images/logo.png" width="258" height="39" />
```

### HTML 元素

```html
<p> 这是一个段落 </p>
<a herf="..."> 这是一个链接 </a>
<br> 换行
<hr> 创建水平线
<!-- 这是一个注释 -->

# 文本格式化
<b> 加粗字体 </b>
<i> 斜体文本 </i>
<code> code </code>
<sub> 下标 </sub>
<sup> 上标 </sup>


```

[小结](https://www.runoob.com/html/html-formatting.html)

### CCS 为渲染元素的格式

```html
例如：
<body style="background-color:yellow;">
<h2 style="background-color:red;">这是一个标题</h2>
<p style="background-color:green;">这是一个段落。</p>
</body>
```



### 速查表格

[速查表格](https://www.runoob.com/html/html-quicklist.html)



### 参考文献

1. [HTML教程](https://www.runoob.com/html/html-intro.html)
2. 

