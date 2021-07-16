import cv2

# frameWidth and frameHeight to output
frameWidth = 640
frameHeight = 480

# We are going to use the Cascade you can create you're own module too,
# but cascade are far better to train easy and accurate modules OpenCV are many cascade for your project and,
# Today I'm going to use the haarcascade russian number plate
# Which is located in the file system
numberPlateCascade = cv2.CascadeClassifier("/home/karthik/Desktop/Python Development/OpenCV/haarcascades/haarcascade_russian_plate_number.xml")

# minArea is the Minumium Area that we allocate for the number plate
minArea = 250

# (255, 0, 255) which is purple color
color = (255, 0, 255)

##################################################
# If you are going to use webcam - uncomment the section
# cap = cv2.VideoCapture(0) # 0 is default you can enter you webcam id. Tip: Even sometimes it may present in -1
# cap.set(3, frameWidth) # 3 is the scale and we already defined frameWidth to 640
# cap.set(4, frameHeight) # 4 is the scale and we already defined frameHeight to 480
# cap.set(10,150) # To brightened the picture resolution
#################################################

count = 0

# Read the images by imread(with path) and store it to a variable

imgCar1 = cv2.imread('/home/karthik/Desktop/Python Development/OpenCV/pictures/car1.jpg')
imgCar2 = cv2.imread('/home/karthik/Desktop/Python Development/OpenCV/pictures/car2.jpg')
imgCar3 = cv2.imread('/home/karthik/Desktop/Python Development/OpenCV/pictures/car3.jpeg')
imgCar4 = cv2.imread('/home/karthik/Desktop/Python Development/OpenCV/pictures/car4.jpg')

while True:
    # Changing images to Gray. Tip: As you see OpenCV use BGR as default rather than RGB
    imgGray = cv2.cvtColor(imgCar4, cv2.COLOR_RGB2GRAY)

    # Cascading the MultiScale Array

    numberPlates = numberPlateCascade.detectMultiScale(imgGray, 1.1, 10)

    # for each in x - x axis, y - y axis, w - width, h - height (x, y, w, h) in numberPlates,
    # which is the MultiScale Array.

    for (x, y, w, h) in numberPlates:
        area = w * h  # we need to multiply width by height. as we know if we multiply w by h it is called as area
        if area > minArea:  # where the area which we need to be bellow 250 pixels

            cv2.rectangle(imgCar4, (x, y), (x + w, y + h), (255, 0, 255), 2)

            # Add text as Number Plate which can be seen above the bounded rectangle
            cv2.putText(imgCar4, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

            # And we need the number plate image to save so we can crop it.
            imgCrop = imgCar4[y:y + h, x:x + w]

            #  Use imshow to display the image with the title and image we need to display
            # Only the number plate which we need to save in a folder
            cv2.imshow("Number Plate without car", imgCrop)

            # Real image with car
            cv2.imshow("Number Plate with car", imgCar4)

            # We need to specify a waitkey and if we press the s keyword the number plate of car will be saved to a
            # directory
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # To need to save it on NumberPlates folder as jpg format
        cv2.imwrite("/home/karthik/Desktop/Python Development/OpenCV/NumberPlates/NoPlate_" + str(count) + ".jpg", imgCrop)

        # Only the number plate
        cv2.rectangle(imgCrop, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)

        # Some to output to indicate the number plate is saved or not
        cv2.putText(imgCar4, "Scan Saved", (125, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)

        # We need to show scan saved text on image for 200 milliseconds
        cv2.waitKey(200)

        # Every time we need to add a number to the images which we are saving
        count += 1
