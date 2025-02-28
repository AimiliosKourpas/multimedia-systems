import collections
import cv2
import pickle
from heapq import heappush, heappop, heapify
from pathlib import Path


class HuffmanCodec: # class HuffmanCodec
    def __init__(self, code_table): # the constructor
        self.code_table = code_table # the code table

    @classmethod # class method
    def from_data(cls, data): # the class method from_data
        frequencies = collections.Counter(data) # the frequencies
        return cls.from_frequencies(frequencies) # return the frequencies

    @classmethod # class method
    def from_frequencies(cls, frequencies): # the class method from_frequencies
        heap = [(f, [(s, (0, 0))]) for s, f in frequencies.items()] # the heap
        heapify(heap) # heapify
        while len(heap) > 1: # while the length of the heap is greater than 1
            a = heappop(heap) # heappop
            b = heappop(heap) # heappop
            merged = ( # merged
                a[0] + b[0],
                [(s, (n + 1, v)) for (s, (n, v)) in a[1]]
                + [(s, (n + 1, (1 << n) + v)) for (s, (n, v)) in b[1]]
            ) #here what we do is we merge the two heaps and we add the frequencies 
            heappush(heap, merged) # heappush
        table = dict(heappop(heap)[1]) # the table convert to dict 
        return cls(table) # return the table
    def encode(self, data): # the encode
        return data # return the data
    
    def decode(self, data): # the decode
        return data # return the data
    
    def save(self, path): # the save
        with open(path, 'wb') as f: # with open
            pickle.dump(self.code_table, f) # pickle.dump

    @classmethod    # class method 
    def load(cls, path): # the class method load
        with open(path, 'rb') as f: # with open
            code_table = pickle.load(f) # pickle.load
        return cls(code_table) # return the code table

def encode_video(input_path, output_path): # the encode video
    print("Encoding Started!") # print a message 
    video = cv2.VideoCapture(input_path) # the video capture
    success, first_frame = video.read() # the success and the first frame
    first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY) # the first frame
    video_codec = cv2.VideoWriter_fourcc(*'XVID') # the video codec
    output = cv2.VideoWriter(output_path, video_codec, video.get(5), (int(video.get(3)), int(video.get(4))), False) # the output
    output.write(first_frame) # the output write the first frame
    previous_frame = first_frame # the previous frame

    while True:
        success, current_frame = video.read() # the success and the current frame
        if not success: # if not success (false)
            break
        current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY) # the current frame
        diff = (current_frame - previous_frame) # the diff IS the current frame - the previous frame
        flat_diff = diff.flatten() # the flat diff
        symb2freq = collections.Counter(flat_diff) # the symb2freq 
        codec = HuffmanCodec.from_frequencies(symb2freq) # the codec 
        encoded_diff = codec.encode(diff) 
        output.write(encoded_diff) # the output write the encoded diff
        previous_frame = current_frame 
    video.release() # the video release
    output.release() # the output release
    print("Video released as 'encoding.avi'!") # print a message 
    print("Video encoding completed!") # print a message

def decode_video(input_path, output_path): # the decode video
    print("Video decoding has started") # print a message
    video = cv2.VideoCapture(input_path) # the video capture
    success, first_frame = video.read() # the success and the first frame
    first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY) # the first frame
    video_codec = cv2.VideoWriter_fourcc(*'XVID') # the video codec
    output = cv2.VideoWriter(output_path, video_codec, video.get(5), (int(video.get(3)), int(video.get(4))), False) # the output
    output.write(first_frame) # the output write the first frame
    previous_frame = first_frame

    while True: 
        success, encoded_diff = video.read() # the success and the encoded diff
        if not success: # if not success (false)
            break
        encoded_diff = cv2.cvtColor(encoded_diff, cv2.COLOR_BGR2GRAY) # the encoded diff
        flat_encoded_diff = encoded_diff.flatten()
        symb2freq = collections.Counter(flat_encoded_diff)
        codec = HuffmanCodec.from_frequencies(symb2freq)
        decoded_diff = codec.decode(encoded_diff)
        current_frame = previous_frame + decoded_diff
        output.write(current_frame) # the output write the current frame
        previous_frame = current_frame
    video.release()
    output.release()
    print("Video released as 'decoded.avi'!") # print a message
    print("Video decoding completed!") 


if __name__ == '__main__': 
    encode_video('videoThema1i.mp4', 'encoded.avi') # the encode video 
    decode_video('encoded.avi', 'decoded.avi') # the decode video
    