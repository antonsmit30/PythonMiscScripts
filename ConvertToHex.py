## Script to return cellId and Enode ID from ULI_ECI

import sys

def ExtractHexAndReturn(n):

    _return = (hex(n))
    print("ULI ECI to Hex: " + _return)

    # Hex digits
    enode_id_hex = '0x' + _return[2:6]
    cell_id_hex = '0x' + _return[6:8]

    #Int digits
    enode_id_int = int(enode_id_hex, 0)
    cell_id_int = int(cell_id_hex, 0)

    # tests
    print("ULI ECI :" + str(n))
    print("EnodeB ID : " + str(enode_id_int))
    print("Cell ID : " + str(cell_id_int))

def main():
    # ExtractHexAndReturn(int(sys.argv[1]))
    try:
        ExtractHexAndReturn(int(sys.argv[1]))
    except IndexError:
        print("Please specifiy a ULI ECI to use")


if __name__ == '__main__':
    main()
