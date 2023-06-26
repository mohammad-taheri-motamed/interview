import cv2

video_path = 'interview_28_material.mp4' # Replace with your video file path
interval = 5 # Replace n with your desired interval

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frames_to_skip = int(fps * interval)

frame_counter = 0
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    if frame_counter % frames_to_skip == 0:
        # Save the frame as an image file
        cv2.imwrite(f'frame_{frame_counter}.jpg', frame)

    frame_counter += 1

cap.release()
cv2.destroyAllWindows()
