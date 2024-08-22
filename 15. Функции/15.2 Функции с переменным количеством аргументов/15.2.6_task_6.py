def info_kwargs(**kwargs):
  sorted_kwargs = dict(sorted(kwargs.items()))
  for key, value in sorted_kwargs.items():
    print(f"{key}: {value}")