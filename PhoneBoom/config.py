# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019-07-10 13:59
website = [
    dict(
        website='易法通',
        url='http://m.yifatong.com/Customers/register',
        jscode='''
                document.getElementById('CustomerAccount').value='{}';
                document.getElementById('btn-sms').click();
                '''
    ),
    dict(
        website='快易出行企业管理平台',
        url='https://ems.xg-yc.com/#/login',
        jscode='''
            function timedMsg(){
            　　var t=setTimeout("document.querySelector('div.el-form-item input').value='13680260549';document.querySelector('button.btn').click()",5000)
            　　              };
            document.querySelector('ul.nav>li:nth-child(2)>a').click();
            timedMsg();
            '''
    ),
    dict(
        website='天津市企业登记全程电子化服务平台',
        url='https://ems.xg-yc.com/#/login',
        jscode='''
            document.querySelector('button.zhuce').click();
            document.querySelector('#upRphone1').value='{}';
            document.querySelector('#upRfsyzm1').click();
            '''
    ),
    dict(
        website='爱四级商城',
        url='https://www.i4season.com/html/mall/register.html',
        jscode='''
            document.getElementById('register_phone').value='{}';
            document.getElementById('mobile_id').click();
            '''
    ),
    dict(
        website='敢尚商城',
        url='http://www.gsall.cn/webApi/register',
        jscode='''
            document.getElementById('iphone').value='{}';
            document.querySelector('input.fr.yzm_btn').click();
            '''
    ),
    dict(
        website='快乐购商城',
        url='https://www.happigo.com/register/',
        jscode='''
            document.querySelector('#mobileregistermodel-mobile').value='{}';
            document.querySelector('#password').value='123@456@';
            document.querySelector('a.phonecode').click();
            '''
    ),
]
