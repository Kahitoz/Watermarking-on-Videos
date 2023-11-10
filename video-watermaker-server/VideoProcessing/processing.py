import cv2
import os

def add_watermark(video_path, watermark_path, position_case):
    output_dir = "video-watermaker-server/Processed/"
    os.makedirs(output_dir, exist_ok=True)

    # Extract the file name without extension
    file_name_without_extension = os.path.splitext(os.path.basename(video_path))[0]

    # Append 'Processed' to the file name and add the extension '.mp4'
    output_file_name = f"{file_name_without_extension}Processed.mp4"
    output_path = os.path.join(output_dir, output_file_name)

    video_capture = cv2.VideoCapture(video_path)

    width = int(video_capture.get(3))
    height = int(video_capture.get(4))
    fps = int(video_capture.get(5))

    watermark_image = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

    position_dict = {
        1: (10, 10),  # Top-Left
        2: (width - watermark_image.shape[1] - 10, 10),  # Top-Right
        3: (10, height - watermark_image.shape[0] - 10),  # Bottom-Left
        4: (
            width - watermark_image.shape[1] - 10,
            height - watermark_image.shape[0] - 10,
        ),  # Bottom-Right
        5: ((width - watermark_image.shape[1]) // 2, 10),  # Top-Center
        6: (10, (height - watermark_image.shape[0]) // 2),  # Left-Center
        7: (
            (width - watermark_image.shape[1]) // 2,
            (height - watermark_image.shape[0]) // 2,
        ),  # Middle of the Screen
        8: (
            width - watermark_image.shape[1] - 10,
            (height - watermark_image.shape[0]) // 2,
        ),  # Right-Center
    }

    position = position_dict.get(
        position_case, (10, 10)
    )  # Default to Top-Left if case is not found

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        # Create a region of interest for the watermark
        roi = frame[
            position[1] : position[1] + watermark_image.shape[0],
            position[0] : position[0] + watermark_image.shape[1],
        ]

        # Add the watermark to the ROI
        cv2.addWeighted(watermark_image, 0.5, roi, 0.5, 0, roi)

        video_writer.write(frame)

    video_capture.release()
    video_writer.release()
    print("Processing Finished")


# Example usage: add_watermark(video_path, watermark_path, position_case)
add_watermark(
    r"video-watermaker-server/Uploads/sample1.mp4",
    "video-watermaker-server/Logos/logo.jpg",
    position_case=2,  # Change this value to select the desired position
)
