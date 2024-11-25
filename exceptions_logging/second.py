def main():
    d = {'website': 'google', 'url': 'google.ru'}
    try:
        data = d['url']
    except:
        data = 'https://'
    else:
        data = data.upper()
    finally:
        print('Very important action')
    print(data)


main()
