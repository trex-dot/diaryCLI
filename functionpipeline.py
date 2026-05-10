def pipeline(*functions):
    def apply(value):
        for func in functions:
            value = func(value)
        return value
    return apply


result = pipeline(str.strip, str.lower, str.title)('  hello world  ')
print(result)