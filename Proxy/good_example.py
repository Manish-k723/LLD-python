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

class ImageProxy:
    def __init__(self, path: str):
        self._path = path
        self._image = None

    def display(self):
        if self._image is None:
            self._image = HighResolutionImage(self._path)
        return self._image.display()

class PhotoGallery:
    def __init__(self):
        self._images: List[ImageProxy] = []

    def add_image(self, image_path):
        self._images.append(ImageProxy(image_path))

    def display_images(self):
        for image in self._images:
            image.display()
timee = time.time()
photo_gallery = PhotoGallery()
image1 = HighResolutionImage("image1.jpg")
image2 = HighResolutionImage("image2.jpg")
# image1 = ImageProxy("image1.jpg")
# image2 = ImageProxy("image2.jpg")
photo_gallery.add_image(image1)
print(time.time() - timee)
# photo_gallery.add_image(image1)
# photo_gallery.add_image(image2)
# photo_gallery.display_images()
