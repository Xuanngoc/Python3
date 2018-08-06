# virtual environments
---
Virtual Environment thiết lập một môi trường ảo, cho phép bạn thử nghiệm với các packages của Python mà không làm ảnh hưởng đến những packages đã được cài đặt sẵn trên Python. 

## install 
```$ pip install virtualenv```

## Tạo Virtual Environment
```$ virtualenv [project_name]```

__virtualenv__ sẽ tạo ra một thư mục có tên là [project_name] chứa tất cả những gì cần thiết.

Nếu trên server có nhiều phiên bản Python (2.x, 3.x) bạn hoàn toàn có thể khởi tạo Virtual Environment với một phiên bản chỉ định:

`virtualenv -p /usr/bin/python2.7 [project_name]`

Hoặc bạn có thể tạo một Virtual Environment mà không có các packages đã được cài đặt sẵn (trong trường hợp bạn muốn làm mọi thứ từ đầu:

`virtualenv --no-site-packages [project_name]`

## Sử dụng Virtual Environment
Khởi động Virtual Environment bằng câu lệnh:

```$ source [project_name]/bin/activate```
Tên của Virtual Environment sẽ xuất hiện ở phía trước command prompt, cho ta thấy Python đang sử dụng Virtual Environment. Từ đây tất cả những packages được cài đặt mới sẽ nằm trong thư mục [project_name]

## Thoát khỏi Virtual Environment
Sử dụng câu lệnh

```$ deactivate```