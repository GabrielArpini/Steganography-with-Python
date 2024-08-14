# Steganography with Python
    #### Video Demo:  https://www.youtube.com/watch?v=gRY03B81uYY
    #### Description: 
    This project consists of an algorithm that takes an image and encode a message inside it. It encodes data by changing the least significant bit value of each pixel, since each pixel have a rgb value it's possible to add 3 bits of data per pixel.

    Functions:
    #get_img(path)
    Receives an image path as argument, it will check if it's a valid path, then it will read the image and save as type np.uint8, which is a type where each pixel have a rgb value. plt.imread() sometimes saves as other formats, like float numbers, thats why it's necessary to check it and assure that img is np.uint8 before returning it.

    #get_message(message, img)
    This function receives a message and check if its a '.txt' file or a typed string, if it's typed it's simply returned, if it's not, this function will run a if statement, to check if image size can support the content of the '.txt' file.

    #get_bin(s)
    Receives a string 's' as argument, it will then transform each char into an ord() number and then into binary, if binary length is smaller than 8, it will add '0' before until it's length is equal 1 byte (8 bits). After that, it will iterate into each bit and add it to a list, getting each bit value into a list and returning it with an addition of a null terminator binary number, which will let this algorithm determine if message ended or not.

    #encode(img, message)
    It's supposed to receive get_img img and get_message message as argument. Every binary number when its odd will have 1 as its last significat bit value, so to get all zeros in the end, it's necessary to transform every rgb value of each pixel into an even number, img_even does that. img_1D is a 1-dimension array of the image and message_1D is a 1-dimension array of the message with the same type as img_1D, so its possible to add each message bit into img_1D values, after the addition, its necessary to reshape img_1D into a multi dimension object with its original shape (img_reshape), use Pillow.Image to transform it back into an image and save it as encoded.png.

    #decode(enc_img)
    Receives a encoded image and get it's data by transforming enc_img into a 1-dimension array, iterating trough each value and savig every bit into a variable 'get_byte', each iteraction will check if get_byte contains 8 bits, if true it will transform get_byte into a char and add it into a list 'lst_byte' and then clear 'get_byte' and iterate again to get all bytes encoded util the null terminator (which was added with 'get_bin(s)' function).

    #load_UI()
    This function will handle user interaction, displaying program name and options at first. There are 2 options, one to encode and other to decode and user is prompted to choose one of them, if user inputs '1' it will prompt for a image path, call 'get_img(path)', then it will prompt for a message or message file, call 'get_msg(message,img)' function, if no error occured, it will then call encode to insert message inside the image.
    Option 2 will simply decode an encoded image by prompting the user for an image path and return decoded message as string.


    #main()
    Calls 'load_UI()' function to handle user interaction.

