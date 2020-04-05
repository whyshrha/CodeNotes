[TOC]



# XML和JSON区别

## 定义

### XML

可扩展标记语言（英语：Extensible Markup Language，简称：XML）.用来传输及存储数据信息，不用来表现或展示数据。

### JSON

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。易于人阅读和编写。同时也易于机器解析和生成。它基于JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999的一个子集。

与XML 相比，JSON是在JS中读写结构化数据更好的 方式，因为它可以把JSON 直接传给eval(),而不必创建 DOM 对象。

## 优缺点

### XML

* 优点
  * 格式统一，符合标准
  * 容易与其他系统进行远程交互，数据共享比较方便

* 缺点
  * XML文件庞大，文件格式复杂，传输占带宽
  * 服务器端和客户端都需要花费大量代码来解析XML，导致服务器端和客户端代码变得异常复杂且不易维护
  * 客户端不同浏览器之间解析XML的方式不一致，需要重复编写很多代码
  * 服务器端和客户端解析XML花费较多的资源和时间

### JSON

* 优点
  * 数据格式比较简单，易于读写，格式都是压缩的，占用带宽小
    易于解析，客户端JavaScript可以简单的通过eval()进行JSON数据的读取
  * 支持多种语言，包括ActionScript, C, C#, ColdFusion, Java, JavaScript, Perl, PHP, Python, Ruby等服务器端语言，便于服务器端的解析
  * 因为JSON格式能直接为服务器端代码使用，大大简化了服务器端和客户端的代码开发量，且完成任务不变，并且易于维护
* 缺点
  * 没有XML格式这么推广的深入人心和喜用广泛，没有XML那么通用性
  * 数据描述性不如XML

## 样例

### XML样例

```xml
<?xml version="1.0" encoding="utf-8" ?>
<country>
  <name>中国</name>
  <province>
    <name>黑龙江</name>
    <citys>
      <city>哈尔滨</city>
      <city>大庆</city>
    </citys>  　　
  </province>
  <province>
    <name>广东</name>
    <citys>
      <city>广州</city>
      <city>深圳</city>
      <city>珠海</city>
    </citys> 　　
  </province>
</country>
```

### JSON样例

```json
var country =
        {
            name: "中国",
            provinces: [
            { name: "黑龙江", citys: { city: ["哈尔滨", "大庆"]} },
            { name: "广东", citys: { city: ["广州", "深圳", "珠海"]} }
            ]
        }
```

JSON 的速度要远远快于 XML。



# Python读写json数据

```python
import json
with open('../data/SSD1.json', 'r') as f:
    data = json.load(f)
# define variable
fp_qdxx_sum = float(data['content']['CGSPFX']['fpxxVo']['fp_qdxx_sum'])
fp_qdxx_count = float(data['content']['CGSPFX']['fpxxVo']['fp_qdxx_count'])
# compute
sums_a = fp_qdxx_sum + fp_qdxx_count
sums_b = fp_qdxx_sum * fp_qdxx_count
# print format & save
res = {'sums_a':sums_a,'sums_b':sums_b}
with open('../data/submit.json', 'w') as f:
    json.dump(res, f)
```

