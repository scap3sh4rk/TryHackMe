import os
import re

def extract_mjpeg_frames(file_path, output_dir, boundary):
    with open(file_path, 'rb') as file:
        data = file.read()

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_number = 1

    # Use the custom boundary string in regex
    boundary_pattern = boundary.encode()  # Convert the boundary to bytes

    # Split the raw data into separate parts based on the boundary string
    frames = re.split(boundary_pattern, data)

    for frame in frames:
        # Skip frames that are too small to be valid JPEGs
        if len(frame) < 100:
            continue

        # Look for the starting JPEG marker (0xFFD8) and ending marker (0xFFD9)
        jpeg_start = frame.find(b'\xff\xd8')  # JPEG start marker
        jpeg_end = frame.find(b'\xff\xd9')    # JPEG end marker

        if jpeg_start != -1 and jpeg_end != -1:
            # Extract the valid JPEG data
            valid_frame = frame[jpeg_start:jpeg_end + 2]

            # Save the valid JPEG frame
            with open(f'{output_dir}/frame_{frame_number}.jpg', 'wb') as img_file:
                img_file.write(valid_frame)

            frame_number += 1

    print(f"Extracted {frame_number - 1} frames.")

# Example usage
file_path = 'source.raw'  # Replace with your actual file path
output_dir = 'output'  # Folder to save the extracted JPEGs
boundary = 'BoundaryString'  # Replace with actual boundary string from your data

extract_mjpeg_frames(file_path, output_dir, boundary)
