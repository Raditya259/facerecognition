import cv2

def capture_image_from_camera(camera_index=0):
    # Initialize the camera
    cap = cv2.VideoCapture(camera_index)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open video device")
        return None

    # Read a frame from the camera
    ret, img = cap.read()
    
    # Release the camera
    cap.release()
    
    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame from the camera")
        return None
    
    if img is None:
        print("Error: Captured image is None")
        return None

    print(f"Captured image shape: {img.shape}")
    return img

def main():
    img = capture_image_from_camera()
    
    # Check if the image is valid before resizing
    if img is not None:
        # Display the captured image to verify
        cv2.imshow("Captured Image", img)
        cv2.waitKey(1000)  # Display for 1 second
        cv2.destroyAllWindows()
        
        try:
            # Resize the image
            imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
            print("Image resized successfully")
            print(f"Captured image shape: {img.shape}")
        except cv2.error as e:
            print(f"Error during resizing: {e}")
    else:
        print("No image to resize")

if __name__ == "__main__":
    main()
