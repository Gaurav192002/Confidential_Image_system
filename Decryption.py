def decrypt(image):
    img = cv2.imread("message.png", 1)
    width = img.shape[0]
    height = img.shape[1]
    retrived_img = np.zeros((width, height, 3), np.uint8)
    for k in range(3):
        for j in range(height):
            for i in range(width):
                imgG = str(img[i][j][k])
                print(imgG.zfill(3), end=" ")
                img_to_bin = format(img[i][j][k], '08b')
                retrieved_img_bin = img_to_bin[4:] + chr(random.randint(0, 1) + 48) * 4
                retrived_img[i][j][k] = int(retrieved_img_bin, 2)
            print()
        print("\n")

    cv2.imwrite('retrived_image.png', retrived_img)
