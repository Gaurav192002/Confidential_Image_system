def encrypt(image1, image2, extension):
    imga1 = cv2.imread(image1, 1)
    imga2 = cv2.imread(image2, 1)
    width = 600
    height = 800
    dimen = (width, height)
    img1 = cv2.resize(imga1, dimen, interpolation=cv2.INTER_AREA)
    img2 = cv2.resize(imga2, dimen, interpolation=cv2.INTER_AREA)
    for k in range(3):
        for j in range(600):
            for i in range(800):
                img1g = str(img1[i][j][k])
                print(img1g.zfill(3), end=" ")
                #all_bits1 = format(img1[i][j][k], '08b')
                #all_bits2 = format(img2[i][j][k], '08b')
                #new_pixel = all_bits1[:4] + all_bits2[:4]
            print()
        print("\n")
    print("VALUES FOR SECOND IMAGE")
    print("\n")
    for k in range(3):
        for j in range(600):
            for i in range(800):
                img2g = str(img2[i][j][k])
                print(img2g.zfill(3), end=" ")
                all_bits1 = format(img1[i][j][k], '08b')
                all_bits2 = format(img2[i][j][k], '08b')
                new_pixel = all_bits1[:4] + all_bits2[:4]
                img1[i][j][k] = int(new_pixel, 2)
            print()
        print("\n")

    cv2.imwrite('message.png', img1)
    return 1
