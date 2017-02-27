
# Verification that mysql transactions are connection specific
Test mysql transaction connection localization

To run:

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the code:

```bash
python main.py
```

You should see as output `((2L, 'Hello on connection 2'),)` and NOT `((2L, 'Hello on connection 1'),)`.