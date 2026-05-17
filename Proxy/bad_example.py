import time
from typing import List

class HighResolutionImage:
    def __init__(self, image_path):
        self._file_path = image_path
        self._image = None

        self.load_from_disk()

    def load_from_disk(self):
        time.sleep(1)
        self._image = f"Image from disk: {self._file_path}"
        print(f"Loaded {self._image}")

    def display(self):
        print(f"Displaying {self._image}")

class PhotoGallery:
    def __init__(self):
        self._images: List[HighResolutionImage] = []

    def add_image(self, image_path):
        self._images.append(HighResolutionImage(image_path))

    def display_images(self):
        for image in self._images:
            image.display()

photo_gallery = PhotoGallery()
image1 = HighResolutionImage("image1.jpg")
image2 = HighResolutionImage("image2.jpg")
# photo_gallery.add_image(image1)
# photo_gallery.add_image(image2)
# photo_gallery.display_images()
