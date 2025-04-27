# multimedia-systems

Sure! Here's the README in a format you can copy and paste:

# Video Compression and Object Removal using Motion Compensation

## Overview

This repository contains a set of Python implementations for video compression and object removal using motion compensation techniques. The work was part of a project for the "Multimedia Systems" course at the University of Piraeus (2022-2023). The project was divided into three tasks, each focusing on a different aspect of video processing: Huffman compression, motion compensation, and object removal.

## Project Structure

This project contains the following tasks:

1. **Task 1: Video Compression Using Huffman Encoding**
2. **Task 2: Motion Compensation for Video Compression**
3. **Task 3: Object Removal from Video Using Motion Compensation**

### Task 1: Video Compression Using Huffman Encoding
In this task, a video is compressed using Huffman encoding applied to the difference between consecutive video frames. The encoded video is then decoded, resulting in a noisy reconstruction due to the error accumulation in the decoding process.

#### Key Steps:
- Frame difference calculation.
- Huffman encoding of the difference.
- Decoding process with accumulated errors.

#### Requirements:
- Python 3
- OpenCV: `pip install opencv-python`
  
### Task 2: Motion Compensation for Video Compression
This task focuses on using motion compensation to compress a video. The video is split into macroblocks, and motion vectors are calculated to represent the movement between frames. A hierarchical search approach is applied to speed up the process.

#### Key Steps:
- Convert frames to grayscale.
- Macroblock division and motion vector calculation.
- Image prediction and error image calculation.
- Motion compensation for encoding and decoding.

#### Requirements:
- Python 3
- OpenCV: `pip install opencv-python`
- tqdm: `pip install tqdm`

### Task 3: Object Removal from Video Using Motion Compensation
In this task, an object is algorithmically removed from a video by utilizing motion compensation. The frames are split into macroblocks, and motion vectors are adjusted to exclude the moving object.

#### Key Steps:
- Select the first frame with minimal motion.
- Apply motion compensation across frames to exclude the moving object.
- Reconstruct the video with the object removed.

#### Requirements:
- Python 3
- OpenCV: `pip install opencv-python`
- Numpy: `pip install numpy`

## File Descriptions

- `encoder1ii.py`: Encoder for motion compensation video compression (Task 2).
- `decoder1ii.py`: Decoder for motion compensation video compression (Task 2).
- `function.py`: Utility functions for motion compensation (Task 2).
- `Thema1i.py`: Encoder for Huffman compression (Task 1).
- `Thema2.py`: Encoder for object removal (Task 3).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install required libraries:
   ```bash
   pip install opencv-python numpy tqdm
   ```

3. Run the respective Python scripts for each task:
   - Task 1: `python3 Thema1i.py`
   - Task 2: `python3 encode1_2.py` and `python3 decode1_2.py`
   - Task 3: `python3 Thema2.py`

## Examples

### Task 1: Video Compression Using Huffman Encoding
Example of an input video and its encoded/decoded versions:

**Original Video:**

![Screenshot 2025-02-28 at 1 07 08 PM](https://github.com/user-attachments/assets/780c997d-410a-4d00-9dd1-3a82c6532141)


**Encoded Video:**

![Screenshot 2025-04-27 at 4 03 38 PM](https://github.com/user-attachments/assets/d43d665d-67e8-49a1-a97c-c4564f9d1d0f)

**Decoded Video:**

![Screenshot 2025-04-27 at 4 04 28 PM](https://github.com/user-attachments/assets/a8934c32-5b5f-466d-8b44-bd524ccfab93)


### Task 2: Motion Compensation for Video Compression
Example of an input video and its encoded/decoded versions:

**Original Video:**

![Screenshot 2025-04-27 at 8 29 25 PM](https://github.com/user-attachments/assets/48d44302-e632-4922-b2d8-0e530b36caee)

**Encoded Video:**

![Screenshot 2025-04-27 at 8 29 44 PM](https://github.com/user-attachments/assets/276e7746-537a-41db-ab48-c901f7aa4284)

**Decoded Video:**

![Screenshot 2025-04-27 at 8 30 01 PM](https://github.com/user-attachments/assets/5473290a-48d6-4ba9-818d-6ba5d6eb8ca6)

### Task 3: Object Removal from Video Using Motion Compensation
Example of an input video with an object and the resulting video after object removal:

**Before Object Removal:**

![Screenshot 2025-04-27 at 8 30 21 PM](https://github.com/user-attachments/assets/fea9c515-adc0-4402-9811-4771b31f4a35)

**After Object Removal:**

![Screenshot 2025-04-27 at 8 30 42 PM](https://github.com/user-attachments/assets/5e80d2f7-781f-40d9-b4af-5c6e440b059a)

## Bibliography

- *Multimedia Systems - Algorithms, Standards, and Applications* by Parag Havaldar, Gerard Medioni
- OpenCV Documentation: [https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html](https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html)
- Numpy Documentation: [https://numpy.org/doc](https://numpy.org/doc)
- tqdm Documentation: [https://tqdm.github.io/](https://tqdm.github.io/)

## License

This project is licensed under the MIT License.
