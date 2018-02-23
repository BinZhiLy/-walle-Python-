前提条件：
 1首先项目需要集成walle库
  implementation 'com.meituan.android.walle:library:1.1.6'
 2配置自己的签名信息，只有签名后才可以使用
 3在全局盒子或者主活动中获取相关渠道信息
 
 private void initView() {
        TextView tv = findViewById(R.id.tv_walle_pk);
        ChannelInfo channelInfo= 		  WalleChannelReader.getChannelInfo(this.getApplicationContext());
        if (channelInfo != null) {
            //渠道
            String channel = channelInfo.getChannel();
            //渠道额外信息
            Map<String, String> extraInfo = channelInfo.getExtraInfo();
            tv.setText(channel);
        }
    }


Python使用方法

切换到当前目录下，通过python3 start.py  启动程序 ，需要注意walle jar包必须在当前文件夹下
1多渠道打包  
 需要必填渠道文件路径，apk路径，生成路径选填，默认生成在当前文件夹下

2自定义渠道号打包
 需要必填apk路径和渠道名进行单个打包，填写From可以追加渠道名称
 同时填写From 和 To 为数字区间时，打这一个区间的渠道包，比如meituan1 meituan2 metuan3,这种用法要确保填写
 的都是数字，并且from<to才可以使用


======================================

直接通过命令行使用方法
显示当前apk中的渠道和额外信息：
java -jar walle-cli-all.jar show /Users/Meituan/app/build/outputs/apk/app.apk

写入信息
写入渠道
java -jar walle-cli-all.jar put -c meituan /Users/Meituan/Downloads/app.apk

写入额外信息，不提供渠道时不写入渠道
java -jar walle-cli-all.jar put -c meituan -e buildtime=20161212,hash=xxxxxxx /Users/xxx/Downloads/app.apk

指定输出文件，自定义名称。 不指定时默认与原apk包同目录。
java -jar walle-cli-all.jar put -c meituan /Users/Meituan/Downloads/app.apk /Users/xxx/Downloads/app-new-hahha.apk

批量写入
命令行指定渠道列表
java -jar walle-cli-all.jar batch -c meituan,meituan2,meituan3 /Users/walle/app/build/outputs/apk/app.apk

指定渠道配置文件
java -jar walle-cli-all.jar batch -f /Users/Meituan/walle/app/channel  /Users/Meituan/walle/app/build/outputs/apk/app.apk

配置文件示例 支持使用#号添加注释
输出目录可指定，不指定时默认在原apk包同目录下。
指定渠道&额外信息配置文件
java -jar walle-cli-all.jar batch2 -f /Users/Meituan/walle/app/config.json  /Users/Meituan/walle/app/build/outputs/apk/app.apk

配置文件示例
输出目录可指定，不指定时默认在原apk包同目录下。
更多用法
获取cli所有功能
java -jar walle-cli-all.jar -h
