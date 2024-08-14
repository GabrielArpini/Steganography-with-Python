import matplotlib.pyplot as plt
from PIL import Image,UnidentifiedImageError
import numpy as np
import sys
from pyfiglet import Figlet


def main():
    load_UI()


# get_img reads given path image and return img as type np.uint8
# np.uint8 is a representation of a image with 3 color channels (RGB)
# so for each pixel in a image, there will be 3 integers from 0 to 255.
def get_img(path):
    try:
        img = plt.imread(path)
        if img.dtype == np.float32 or img.dtype == np.float64:
            img = (img * 255).astype(np.uint8)

    except FileNotFoundError:
        sys.exit("No such file")
    except UnidentifiedImageError:
        sys.exit("File is not a image")
    return img


#get_message get user input, check if it is valid
# check if image can support message, etc
def get_message(message, img):

    file_message = ''
    if message.endswith(".txt"):
        try:
            with open(message) as file:
                reader = file.readlines()
                for i in reader:
                    file_message += i
        except FileNotFoundError:
            sys.exit("No such file")
        w, h, r = np.shape(img)
    if not file_message:
        return message

    #get total rgb bit value and check if image char byte quantity is supported
    if(w*h*3 < len(file_message) * 8):
        sys.exit("Message size is bigger than image least significant bit capacity")
    return file_message




#Transform a string into a binary list.
def get_bin(s):
    str_bin_total = []
    for c in s:
        # convert c(char) into ord number and then to binary
        binary = bin(ord(c))[2:]
        #add 0 padding if needed, so binary length is equal to a byte size (8 bits)
        binary_byte = str(0)*(8 - len(binary)) + binary

        #its needed to have single bit value for each position
        # instead of [00000001,00100000, ...]
        # str_bin_total is saved as: [0,0,0,0,0,0,0,1, ...]
        str_bin_total = str_bin_total + [int(i) for i in binary_byte]

    # last value is a binary null char, so our program knows when message was fully decoded.
    # performance choice, so our program don't iterate trough unecessary pixel value sequence.
    return str_bin_total + [0,0,0,0,0,0,0,0]

def encode(img, message):

    #round rgb values to even numbers to add message bits later.
    img_even = img - img % 2
    #convert image object into a 1-dimension array.
    img_1D = np.ravel(img_even)
    #transform message into binary and then convert it into a numpy array.
    message_1D = np.array(get_bin(message))
    #convert message arra into uint8 type, so its possible to do operations with img_1D.
    message_1D = message_1D.astype(np.uint8)
    #for each value of img_1D, add message_1D bit.
    img_1D[0:message_1D.size] += message_1D
    #Reshapes 1-dimension array into an multi dimensional object.
    img_reshape = np.reshape(img_even,img.shape)
    #Transform said object into a image.
    data = Image.fromarray(img_reshape)
    #Save Image
    data.save('encoded.png')
    return 'Message encoded successfully!'

    #Arbitrary return, maybe in the future it will be needed.
    #return np.reshape(img_even,img.shape)


def decode(enc_img):

    # Transform enc_img object into an 1-Dimension array, so its possible to iterate trough it.
    enc_1D = np.ravel(enc_img)
    i = 0
    lst_byte = []
    get_byte = ''

    while True:
        # Get least significant bit value.
        single_bit = str(bin(enc_1D[i])[-1])
        # Accumulate bits until it reaches 8 bits (1 byte).
        get_byte += single_bit

        i += 1

        # A char is 8 bits long, so for each byte, the converted char value is appended to a lst.
        if len(get_byte) == 8:
            # Append the character equivalent of the binary byte to the list
            lst_byte.append(chr(int(get_byte, 2)))
            get_byte = ''

            # If program reads the null terminator, the loop breaks, since our message was fully decoded
            if lst_byte[-1] == '\x00':
                break

    # Convert char list into a string
    decoded_message = ''.join(lst_byte[:-1])
    return decoded_message

# UI, options and function calls based on user choice.
def load_UI():
    f = Figlet(font='big')
    n = 'Steganography V1.0'
    print(f.renderText(n))
    print("Options: ")
    print("(1) Encode")
    print("(2) Decode")
    choice = input("Input: ").strip()

    if(choice == "1"):
        path = input("Insert image path: ")
        img = get_img(path)
        message_in = input("Insert a message to hide or a .txt path: ")
        message = get_message(message_in, img)
        print(encode(img,message))
    elif(choice == "2"):
        path = input("Insert image path: ")
        enc_img = get_img(path)
        print("Decoded text: ")
        print(decode(enc_img))
    else:
        sys.exit("Invalid choice")


if __name__ == '__main__':
    main()
