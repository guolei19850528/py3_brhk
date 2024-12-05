# py3_brhk

The Python3 Brhk Library Developed By Guolei

# Installation

```shell
pip install py3_brhk
```

# Official Documentation

## [Home](https://www.yuque.com/lingdutuandui/ugcpag)

# Example
## Speaker
### voice notify
```python
from py3_brhk.speaker import Speaker

speaker = Speaker(
    token="<token>",
    id="<id>"
)
state, _ = speaker.notify(message="测试信息")
if state:
    print("successful")
```