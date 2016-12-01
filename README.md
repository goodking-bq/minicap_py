# minicap
### 获取设备的CPU版本
```
adb shell getprop ro.product.cpu.abi
```
### 获取设备的系统版本
```
adb shell getprop ro.build.version.sdk
```
### 上传相应文件
```
adb push mydevice/* /data/local/tmp
```
### 添加执行权限
```
adb shell chmod +x /data/local/tmp/minicap
```
### 测试 是否返回 ok?
```
adb shell LD_LIBRARY_PATH=/data/local/tmp/mydevice /data/local/tmp/mydevice/minicap -P 1080x1920@1080x1920/0 -t
```
### 执行程序
```
adb shell LD_LIBRARY_PATH=/data/local/tmp/mydevice /data/local/tmp/mydevice/minicap -P 1080x1920@1080x1920/0
```
### 端口转发
```
adb forward tcp:1717 localabstract:minicap
```
