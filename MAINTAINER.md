requirements for making releases

```
python3 -m pip install --user --upgrade twine setuptools wheel
```

to make a new release, bump version in pyttanko.py and run

```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
