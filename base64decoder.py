import base64
import sys

def decodeObject(stringobject):
    decoded_object = base64.urlsafe_b64decode(stringobject)
    print('decoded object : {}'.format(decoded_object))

def main():
    try:
        new_var = sys.argv[1]
    except IndexError:
        print('Please Specify an argument')
    else:
        decodeObject(sys.argv[1])

if __name__ == '__main__':
    main()



