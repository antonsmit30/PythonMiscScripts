import base64
import sys

def encodeObject(stringobject):
    '''

    info: Accepts a string object and returns a URL safe Base64 Encoded Object.

    :param stringobject:
    :return:
    '''
    string_as_bytes = bytes(stringobject, 'utf-8')
    encoded_object = base64.urlsafe_b64encode(string_as_bytes)
    print('decoded object : {}'.format(encoded_object))

def main():
    '''

    info: Our Main function.

    :return:
    '''
    try:
        new_var = sys.argv[1]
    except IndexError:
        print('Please Specify an argument')
    else:
        encodeObject(sys.argv[1])

if __name__ == '__main__':
    main()



