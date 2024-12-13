# py3_brhk

The Python3 Brhk Library Developed By Guolei

# Installation

```shell
pip install py3_brhk
```

# Documentation

## [Document](https://www.yuque.com/lingdutuandui/ugcpag)

# Example
## Speaker
### voice notify
```python
from py3_brhk.speaker import Speaker

speaker = Speaker(
    token="<token>",
    id="<id>"
)
state = speaker.notify(message="小猪小猪，呼噜噜")
if state:
    print("send success")
else:
    print("send failed")
```