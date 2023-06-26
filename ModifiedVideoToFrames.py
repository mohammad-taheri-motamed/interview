import cv2
import os

video_path = 'interview_28_material.mp4' # Replace with your video file path
interval = 5 #desired interval

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frames_to_skip = int(fps * interval)

frame_counter = 0
output_folder = 'images'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    if frame_counter % frames_to_skip == 0:
        # Save the frame as an image file inside the output folder
        cv2.imwrite(os.path.join(output_folder, f'{frame_counter}.jpg'), frame)

    frame_counter += 1

cap.release()
cv2.destroyAllWindows()
