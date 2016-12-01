# minicap
### 获取设备的CPU版本
```
PS D:\minicap\adb> .\adb.exe shell getprop ro.product.cpu.abi
arm64-v8a
```
### 获取设备的系统版本
```
PS D:\minicap\adb> .\adb.exe shell getprop ro.build.version.sdk
23
```
### 获取设备分辨率
```
PS D:\minicap\adb> .\adb.exe shell dumpsys window | grep -Eo 'init=[0-9]+x[0-9]+' | head -1 | cut -d= -f 2
1080x1920
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
PS D:\minicap\adb> .\adb.exe shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@1080x1920/0 -t
no config
PID: 4303
INFO: Using projection 1080x1920@1080x1920/0
INFO: (external/MY_minicap/src/minicap_M.cpp:240) Creating SurfaceComposerClient
INFO: (external/MY_minicap/src/minicap_M.cpp:243) Performing SurfaceComposerClient init check
INFO: (external/MY_minicap/src/minicap_M.cpp:250) Creating virtual display
INFO: (external/MY_minicap/src/minicap_M.cpp:256) Creating buffer queue
INFO: (external/MY_minicap/src/minicap_M.cpp:261) Creating CPU consumer
INFO: (external/MY_minicap/src/minicap_M.cpp:265) Creating frame waiter
INFO: (external/MY_minicap/src/minicap_M.cpp:269) Publishing virtual display
INFO: (jni/minicap/JpgEncoder.cpp:64) Allocating 6268932 bytes for JPG encoder
INFO: (external/MY_minicap/src/minicap_M.cpp:284) Destroying virtual display
OK
```
### 执行程序
```
PS D:\minicap\adb> .\adb.exe shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1080x1920@1080x1920/0
no config
PID: 4315
INFO: Using projection 1080x1920@1080x1920/0
INFO: (external/MY_minicap/src/minicap_M.cpp:240) Creating SurfaceComposerClient
INFO: (external/MY_minicap/src/minicap_M.cpp:243) Performing SurfaceComposerClient init check
INFO: (external/MY_minicap/src/minicap_M.cpp:250) Creating virtual display
INFO: (external/MY_minicap/src/minicap_M.cpp:256) Creating buffer queue
INFO: (external/MY_minicap/src/minicap_M.cpp:261) Creating CPU consumer
INFO: (external/MY_minicap/src/minicap_M.cpp:265) Creating frame waiter
INFO: (external/MY_minicap/src/minicap_M.cpp:269) Publishing virtual display
INFO: (jni/minicap/JpgEncoder.cpp:64) Allocating 6268932 bytes for JPG encoder
INFO: (jni/minicap/minicap.cpp:585) ===E===
```
## 但是检查缺没有那个进程  这是为啥
```
PS D:\minicap\adb> .\adb.exe shell ps -ef|grep 4315
PS D:\minicap\adb> .\adb.exe shell ps -ef|grep mini
```
### 端口转发
```
adb forward tcp:1717 localabstract:minicap
```
### 检查端口
```
PS D:\minicap\adb> netstat -an|findstr 1717
  TCP    127.0.0.1:1717         0.0.0.0:0              LISTENING
```
###