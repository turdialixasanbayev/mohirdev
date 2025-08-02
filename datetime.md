```python
from datetime import datetime
slug_time = datetime.today().strftime("%d-%m-%Y-%H-%M-%S")
# Masalan: '02-08-2025-10-55-32'
```

```python
from datetime import datetime
slug_time = datetime.now().strftime("%d-%m-%Y")
# Masalan: '02-08-2025'
```