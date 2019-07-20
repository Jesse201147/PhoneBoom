# PhoneBoom
短信轰炸机(玩具)

* 功能实现:  
    engine.py : 通用方法, 打开页面,输入手机号,点击发送验证码 (使用协程加速)  
    config.py : 发送验证码的站点的配置文件(包含: 页面url, 输入+点击的js代码)  

* 声明:  
    此脚本轰炸效果取决于config中站点的数量, 为防止恶意滥用, 只选取一小部分上传仅供试玩.  
    此脚本是工作之余的附带产物, 觉得有趣就保存了下来, **请勿滥用, 请勿恶意骚扰他人**
    
```flow
st=>start: Start
i=>inputoutput: 输入年份n
cond1=>condition: n能否被4整除？
cond2=>condition: n能否被100整除？
cond3=>condition: n能否被400整除？
o1=>inputoutput: 输出非闰年
o2=>inputoutput: 输出非闰年
o3=>inputoutput: 输出闰年
o4=>inputoutput: 输出闰年
e=>end
st->i->cond1
cond1(no)->o1->e
cond1(yes)->cond2
cond2(no)->o3->e
cond2(yes)->cond3
cond3(yes)->o2->e
cond3(no)->o4->e
```
