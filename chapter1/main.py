SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple

        if size < multiple:
            return f'{size:.2f} {suffix}'

    raise ValueError('number too large')

if __name__ == '__main__':
    bytes_from_user = int(input('Type bytes: '))

    print(approximate_size(bytes_from_user))
    print(approximate_size(bytes_from_user, False))
